import discord
from discord.ext import commands
from discord import app_commands
import config

def role_only():
    async def check(interaction):
        if any(r.id == config.ALLOWED_ROLE_ID for r in interaction.user.roles):
            return True
        await interaction.response.send_message("❌ Not allowed", ephemeral=True)
        return False
    return app_commands.check(check)

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a user")
    @role_only()
    async def ban(self, interaction, user: discord.Member, reason: str = "No reason"):
        await user.ban(reason=reason)
        await interaction.response.send_message(f"🔨 **{user} banned**")

    @app_commands.command(name="kick", description="Kick a user")
    @role_only()
    async def kick(self, interaction, user: discord.Member, reason: str = "No reason"):
        await user.kick(reason=reason)
        await interaction.response.send_message(f"👢 **{user} kicked**")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
