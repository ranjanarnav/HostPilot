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

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="remind", description="Set renewal reminder")
    @role_only()
    async def remind(self, interaction: discord.Interaction, date: str):
        await interaction.response.send_message(
            f"⏰ **Reminder Set**\nYou should renew your server by **{date}**"
        )

async def setup(bot):
    await bot.add_cog(Reminder(bot))
