import discord
from discord.ext import commands
from discord import app_commands
import config
from datetime import timedelta

def role_only():
    async def check(interaction: discord.Interaction):
        if any(r.id == config.ALLOWED_ROLE_ID for r in interaction.user.roles):
            return True
        await interaction.response.send_message("❌ Not allowed", ephemeral=True)
        return False
    return app_commands.check(check)

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ---------- MESSAGE MANAGEMENT ----------
    @app_commands.command(name="clear", description="Clear messages")
    @role_only()
    async def clear(self, interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"🧹 Cleared {amount} messages", ephemeral=True)

    @app_commands.command(name="clearchannel", description="Clear entire channel")
    @role_only()
    async def clearchannel(self, interaction):
        channel = interaction.channel
        await channel.clone()
        await channel.delete()

    # ---------- CHANNEL CONTROL ----------
    @app_commands.command(name="lock", description="Lock channel")
    @role_only()
    async def lock(self, interaction):
        await interaction.channel.set_permissions(
            interaction.guild.default_role,
            send_messages=False
        )
        await interaction.response.send_message("🔒 Channel locked")

    @app_commands.command(name="unlock", description="Unlock channel")
    @role_only()
    async def unlock(self, interaction):
        await interaction.channel.set_permissions(
            interaction.guild.default_role,
            send_messages=True
        )
        await interaction.response.send_message("🔓 Channel unlocked")

    @app_commands.command(name="slowmode", description="Set slowmode")
    @role_only()
    async def slowmode(self, interaction, seconds: int):
        await interaction.channel.edit(slowmode_delay=seconds)
        await interaction.response.send_message(f"🐢 Slowmode set to {seconds}s")

    # ---------- USER MODERATION ----------
    @app_commands.command(name="timeout", description="Timeout a user")
    @role_only()
    async def timeout(self, interaction, user: discord.Member, minutes: int, reason: str = "No reason"):
        await user.timeout(timedelta(minutes=minutes), reason=reason)
        await interaction.response.send_message(f"⏱️ {user.mention} timed out for {minutes} minutes")

    @app_commands.command(name="untimeout", description="Remove timeout")
    @role_only()
    async def untimeout(self, interaction, user: discord.Member):
        await user.timeout(None)
        await interaction.response.send_message(f"✅ Timeout removed for {user.mention}")

    # ---------- CHANNEL MANAGEMENT ----------
    @app_commands.command(name="createchannel", description="Create channel")
    @role_only()
    async def createchannel(self, interaction, name: str):
        channel = await interaction.guild.create_text_channel(name)
        await interaction.response.send_message(f"📁 Channel created: {channel.mention}")

    @app_commands.command(name="deletechannel", description="Delete channel")
    @role_only()
    async def deletechannel(self, interaction, channel: discord.TextChannel):
        await channel.delete()
        await interaction.response.send_message("🗑️ Channel deleted", ephemeral=True)

    @app_commands.command(name="renamechannel", description="Rename channel")
    @role_only()
    async def renamechannel(self, interaction, channel: discord.TextChannel, new_name: str):
        await channel.edit(name=new_name)
        await interaction.response.send_message("✏️ Channel renamed")

    # ---------- UTILITIES ----------
    @app_commands.command(name="say", description="Bot says message")
    @role_only()
    async def say(self, interaction, message: str):
        await interaction.channel.send(message)
        await interaction.response.send_message("✅ Sent", ephemeral=True)

    @app_commands.command(name="ping", description="Bot latency")
    async def ping(self, interaction):
        await interaction.response.send_message(f"🏓 Pong! `{round(self.bot.latency*1000)}ms`")

    @app_commands.command(name="userinfo", description="User info")
    async def userinfo(self, interaction, user: discord.Member):
        embed = discord.Embed(title="👤 User Info", color=0x3498db)
        embed.add_field(name="Username", value=user)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y"))
        embed.set_thumbnail(url=user.avatar.url)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="User avatar")
    async def avatar(self, interaction, user: discord.Member):
        await interaction.response.send_message(user.avatar.url)

    @app_commands.command(name="poll", description="Create a poll")
    @role_only()
    async def poll(self, interaction, question: str, option1: str, option2: str, option3: str = None):
        embed = discord.Embed(title="📊 Poll", description=question, color=0x9b59b6)
        embed.add_field(name="1️⃣", value=option1, inline=False)
        embed.add_field(name="2️⃣", value=option2, inline=False)
        if option3:
            embed.add_field(name="3️⃣", value=option3, inline=False)

        msg = await interaction.channel.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        if option3:
            await msg.add_reaction("3️⃣")

        await interaction.response.send_message("✅ Poll created", ephemeral=True)

    @app_commands.command(name="embed", description="Create embed")
    @role_only()
    async def embed(self, interaction, title: str, description: str):
        embed = discord.Embed(title=title, description=description, color=0x2ecc71)
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message("✅ Embed sent", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Utilities(bot))
