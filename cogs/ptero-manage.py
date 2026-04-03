import discord
from discord.ext import commands, tasks
from discord import app_commands
import requests
import time
import asyncio
import config

# ================= CONFIG =================
SESSION_TIMEOUT = 30 * 60  # 30 minutes
CONSOLE_POLL_INTERVAL = 5  # seconds

# discord_id -> { api_key, last_active }
SESSIONS = {}

# ================= HELPERS =================
def client_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Accept": "Application/vnd.pterodactyl.v1+json",
        "Content-Type": "application/json"
    }

def session_valid(discord_id):
    session = SESSIONS.get(discord_id)
    if not session:
        return False
    if time.time() - session["last_active"] > SESSION_TIMEOUT:
        del SESSIONS[discord_id]
        return False
    session["last_active"] = time.time()
    return True

# ================= LOGIN MODAL =================
class LoginModal(discord.ui.Modal, title="Server Manager Login"):
    api_key = discord.ui.TextInput(
        label="Pterodactyl Client API Key",
        placeholder="ptlc_...",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        r = requests.get(
            f"{config.PTERO_PANEL_URL}/api/client",
            headers=client_headers(self.api_key.value)
        )
        if r.status_code != 200:
            await interaction.response.send_message(
                "❌ Invalid Client API Key",
                ephemeral=True
            )
            return

        SESSIONS[interaction.user.id] = {
            "api_key": self.api_key.value,
            "last_active": time.time()
        }

        await interaction.response.send_message(
            "✅ Logged in successfully. Run `/manage-server` again.",
            ephemeral=True
        )

# ================= SERVER SELECT =================
class ServerSelect(discord.ui.Select):
    def __init__(self, servers, api_key):
        self.api_key = api_key
        options = [
            discord.SelectOption(
                label=s["attributes"]["name"],
                value=s["attributes"]["identifier"]
            )
            for s in servers
        ]
        super().__init__(placeholder="Select a server", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"🎮 Managing server `{self.values[0]}`",
            view=ServerControls(self.api_key, self.values[0]),
            ephemeral=True
        )

# ================= SERVER CONTROLS =================
class ServerControls(discord.ui.View):
    def __init__(self, api_key, server_id):
        super().__init__(timeout=300)
        self.api_key = api_key
        self.server_id = server_id

    # ---------- POWER ----------
    async def power(self, interaction, action):
        requests.post(
            f"{config.PTERO_PANEL_URL}/api/client/servers/{self.server_id}/power",
            headers=client_headers(self.api_key),
            json={"signal": action}
        )
        await interaction.response.send_message(
            f"✅ `{action}` signal sent",
            ephemeral=True
        )

    @discord.ui.button(label="▶ Start", style=discord.ButtonStyle.green)
    async def start(self, interaction, _):
        await self.power(interaction, "start")

    @discord.ui.button(label="⏹ Stop", style=discord.ButtonStyle.red)
    async def stop(self, interaction, _):
        await self.power(interaction, "stop")

    @discord.ui.button(label="🔁 Restart", style=discord.ButtonStyle.blurple)
    async def restart(self, interaction, _):
        await self.power(interaction, "restart")

    # ---------- STATUS / IP / PLAYERS ----------
    @discord.ui.button(label="📊 Status", style=discord.ButtonStyle.gray)
    async def status(self, interaction, _):
        r = requests.get(
            f"{config.PTERO_PANEL_URL}/api/client/servers/{self.server_id}/resources",
            headers=client_headers(self.api_key)
        )
        data = r.json()["attributes"]

        r2 = requests.get(
            f"{config.PTERO_PANEL_URL}/api/client/servers/{self.server_id}",
            headers=client_headers(self.api_key)
        )
        alloc = r2.json()["attributes"]["relationships"]["allocations"]["data"][0]["attributes"]

        await interaction.response.send_message(
            f"""
**Server Status**
State: `{data['current_state']}`
CPU: `{data['resources']['cpu_absolute']}%`
RAM: `{round(data['resources']['memory_bytes']/1024/1024)} MB`
Disk: `{round(data['resources']['disk_bytes']/1024/1024)} MB`
IP: `{alloc['ip']}:{alloc['port']}`
""",
            ephemeral=True
        )

    # ---------- SEND COMMAND ----------
    @discord.ui.button(label="⌨ Command", style=discord.ButtonStyle.secondary)
    async def command(self, interaction, _):
        class CommandModal(discord.ui.Modal, title="Send Console Command"):
            cmd = discord.ui.TextInput(label="Command", required=True)

            async def on_submit(self, modal_interaction):
                requests.post(
                    f"{config.PTERO_PANEL_URL}/api/client/servers/{self.view.server_id}/command",
                    headers=client_headers(self.view.api_key),
                    json={"command": self.cmd.value}
                )
                await modal_interaction.response.send_message(
                    "✅ Command sent",
                    ephemeral=True
                )

        await interaction.response.send_modal(CommandModal())

    # ---------- CONSOLE (POLLING) ----------
    @discord.ui.button(label="📜 Console", style=discord.ButtonStyle.secondary)
    async def console(self, interaction, _):
        await interaction.response.defer(ephemeral=True)

        r = requests.get(
            f"{config.PTERO_PANEL_URL}/api/client/servers/{self.server_id}/resources",
            headers=client_headers(self.api_key)
        )

        state = r.json()["attributes"]["current_state"]
        await interaction.followup.send(
            f"```Console Snapshot\nState: {state}\n(Realtime streaming limited by Discord)```",
            ephemeral=True
        )

# ================= MAIN COG =================
class PteroManage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="manage-server", description="Manage your servers")
    async def manage_server(self, interaction: discord.Interaction):
        if not session_valid(interaction.user.id):
            await interaction.response.send_modal(LoginModal())
            return

        api_key = SESSIONS[interaction.user.id]["api_key"]

        r = requests.get(
            f"{config.PTERO_PANEL_URL}/api/client",
            headers=client_headers(api_key)
        )

        servers = r.json()["data"]
        if not servers:
            await interaction.response.send_message(
                "❌ No servers found",
                ephemeral=True
            )
            return

        view = discord.ui.View()
        view.add_item(ServerSelect(servers, api_key))

        await interaction.response.send_message(
            "Select a server to manage:",
            view=view,
            ephemeral=True
        )

    @app_commands.command(name="logout-server", description="Logout from server manager")
    async def logout(self, interaction: discord.Interaction):
        SESSIONS.pop(interaction.user.id, None)
        await interaction.response.send_message(
            "✅ Logged out",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(PteroManage(bot))
