import discord
from discord.ext import commands
from discord import app_commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverinfo", description="Show server information")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild

        embed = discord.Embed(
            title=f"{guild.name}",
            description=" ",
            color=discord.Color.green()
        )

        embed.add_field(
            name="📄 General Info",
            value=(
                f"**Server ID:** {guild.id}\n"
                f"**Owner:** <@{guild.owner_id}>\n"
                f"**Created:** <t:{int(guild.created_at.timestamp())}:R>"
            ),
            inline=False
        )

        embed.add_field(
            name="👥 Members",
            value=(
                f"Members: {guild.member_count}\n"
                f"Roles: {len(guild.roles)}\n"
                f"Verification Level: {guild.verification_level}"
            ),
            inline=True
        )

        embed.add_field(
            name="🚀 Boost Status",
            value=(
                f"Level: {guild.premium_tier}\n"
                f"Boosts: {guild.premium_subscription_count}"
            ),
            inline=True
        )

        embed.add_field(
            name="📁 Channels",
            value=(
                f"Text: {len(guild.text_channels)}\n"
                f"Voice: {len(guild.voice_channels)}\n"
                f"Categories: {len(guild.categories)}"
            ),
            inline=False
        )

        embed.set_footer(
            text=f"Requested by {interaction.user}",
            icon_url=interaction.user.display_avatar.url
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
