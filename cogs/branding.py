import discord
from discord.ext import commands
from discord import app_commands
import config

class Branding(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="post", description="Post message to channel")
    async def post(self, interaction, channel: discord.TextChannel, message: str):
        await channel.send(message)
        await interaction.response.send_message("✅ Posted", ephemeral=True)

    @app_commands.command(name="announcement", description="Announcement")
    async def announcement(self, interaction, title: str, message: str):
        embed = discord.Embed(title=f"📢 {title}", description=message, color=0xe67e22)
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message("✅ Announcement sent", ephemeral=True)

    @app_commands.command(name="banner", description="Show banner")
    async def banner(self, interaction, image_url: str):
        embed = discord.Embed(color=0x1abc9c)
        embed.set_image(url=image_url)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="links", description="Important links")
    async def links(self, interaction):
        embed = discord.Embed(title="🔗 Links", color=0x7289da)
        embed.add_field(name="Website", value=config.WEBSITE_LINK, inline=False)
        embed.add_field(name="Panel", value=config.PANEL_LINK, inline=False)
        embed.add_field(name="Billing", value=config.BILLING_LINK, inline=False)
        embed.add_field(name="Support", value=config.SUPPORT_LINK, inline=False)
        embed.add_field(name="Discord", value=config.DISCORD_INVITE, inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Branding(bot))
