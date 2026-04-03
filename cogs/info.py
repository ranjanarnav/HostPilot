import discord
from discord.ext import commands
from discord import app_commands
import platform

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="botinfo", description="Bot info")
    async def botinfo(self, interaction):
        embed = discord.Embed(title="🤖 Bot Info", color=0x3498db)
        embed.add_field(name="Library", value="discord.py")
        embed.add_field(name="Python", value=platform.python_version())
        embed.add_field(name="Servers", value=len(self.bot.guilds))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="servericon", description="Server icon")
    async def servericon(self, interaction):
        if interaction.guild.icon:
            await interaction.response.send_message(interaction.guild.icon.url)
        else:
            await interaction.response.send_message("No server icon")

async def setup(bot):
    await bot.add_cog(Info(bot))
