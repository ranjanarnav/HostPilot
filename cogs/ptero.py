import discord
from discord.ext import commands
from discord import app_commands
import requests
import config

# ---------------- NODE MAP ----------------
NODE_MAP = {
    "AMD EPYC-01": 1,
    "SGP-01": 2,
    "TW-01": 3
}

class Ptero(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ---------------- HEADERS ----------------
    def headers(self):
        return {
            "Authorization": f"Bearer {config.PTERO_API_KEY}",
            "Accept": "Application/vnd.pterodactyl.v1+json",
            "Content-Type": "application/json"
        }

    # ---------------- GET USER ID ----------------
    def get_user_id(self, email: str):
        r = requests.get(
            f"{config.PTERO_PANEL_URL}/api/application/users?per_page=100",
            headers=self.headers()
        )
        if r.status_code != 200:
            return None

        for u in r.json()["data"]:
            if u["attributes"]["email"].lower() == email.lower():
                return u["attributes"]["id"]
        return None

    # ---------------- GET FREE ALLOCATION ----------------
    def get_free_allocation(self, node_id: int):
        r = requests.get(
            f"{config.PTERO_PANEL_URL}/api/application/nodes/{node_id}/allocations",
            headers=self.headers()
        )
        if r.status_code != 200:
            return None

        for alloc in r.json()["data"]:
            if not alloc["attributes"]["assigned"]:
                return alloc["attributes"]["id"]
        return None

    # ---------------- CREATE SERVER ----------------
    @app_commands.command(
        name="createserver",
        description="Create Pterodactyl server (node & limits dropdown)"
    )
    async def createserver(
        self,
        interaction: discord.Interaction,
        email: str,
        node: str,              # ✅ NORMAL TYPE
        name: str,
        ram_mb: int,
        disk_mb: int,
        cpu_percent: int,
        allocations: int,       # ✅ NORMAL TYPE
        databases: int,         # ✅ NORMAL TYPE
        backups: int            # ✅ NORMAL TYPE
    ):
        await interaction.response.defer(ephemeral=True)

        user_id = self.get_user_id(email)
        if not user_id:
            await interaction.followup.send(
                "❌ User email not found in panel.",
                ephemeral=True
            )
            return

        node_id = NODE_MAP.get(node)
        if not node_id:
            await interaction.followup.send(
                "❌ Invalid node selected.",
                ephemeral=True
            )
            return

        allocation_id = self.get_free_allocation(node_id)
        if not allocation_id:
            await interaction.followup.send(
                f"❌ No free allocation available on {node}.",
                ephemeral=True
            )
            return

        payload = {
            "name": name,
            "user": user_id,
            "nest": 1,
            "egg": 2,
            "docker_image": "ghcr.io/pterodactyl/yolks:java_17",
            "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar server.jar",
            "environment": {
            "SERVER_JARFILE": "server.jar",
            "BUILD_NUMBER": "latest"
            },

            "limits": {
                "memory": ram_mb,
                "swap": 0,
                "disk": disk_mb,
                "io": 500,
                "cpu": cpu_percent
            },
            "feature_limits": {
                "allocations": allocations,
                "databases": databases,
                "backups": backups
            },
            "allocation": {
                "default": allocation_id
            }
        }

        r = requests.post(
            f"{config.PTERO_PANEL_URL}/api/application/servers",
            headers=self.headers(),
            json=payload
        )

        if r.status_code == 201:
            await interaction.followup.send(
                f"✅ **Server Created Successfully**\n"
                f"**Name:** {name}\n"
                f"**User:** {email}\n"
                f"**Node:** {node}\n"
                f"**Allocation ID:** {allocation_id}\n"
                f"**RAM:** {ram_mb} MB\n"
                f"**Disk:** {disk_mb} MB\n"
                f"**CPU:** {cpu_percent}%\n"
                f"**Allocations:** {allocations}\n"
                f"**Databases:** {databases}\n"
                f"**Backups:** {backups}",
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                f"❌ Server creation failed\n```{r.text}```",
                ephemeral=True
            )

    # ---------------- AUTOCOMPLETE ----------------
    @createserver.autocomplete("node")
    async def node_autocomplete(self, interaction, current):
        return [
            app_commands.Choice(name=name, value=name)
            for name in NODE_MAP.keys()
        ]

    @createserver.autocomplete("allocations")
    async def allocations_autocomplete(self, interaction, current):
        return [app_commands.Choice(name=str(i), value=i) for i in range(0, 6)]

    @createserver.autocomplete("databases")
    async def databases_autocomplete(self, interaction, current):
        return [app_commands.Choice(name=str(i), value=i) for i in range(0, 6)]

    @createserver.autocomplete("backups")
    async def backups_autocomplete(self, interaction, current):
        return [app_commands.Choice(name=str(i), value=i) for i in range(0, 6)]

async def setup(bot):
    await bot.add_cog(Ptero(bot))
