import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import pytz
import config

IST = pytz.timezone("Asia/Kolkata")

def role_only():
    async def check(interaction: discord.Interaction):
        if any(r.id == config.ALLOWED_ROLE_ID for r in interaction.user.roles):
            return True
        await interaction.response.send_message("❌ Not allowed", ephemeral=True)
        return False
    return app_commands.check(check)

class Money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="moneylog", description="Add money log")
    @role_only()
    async def moneylog(
        self,
        interaction: discord.Interaction,
        amount: int,
        user: str,
        method: str
    ):
        channel = await self.bot.fetch_channel(config.MONEY_LOG_CHANNEL_ID)

        # ✅ IST → UTC (Discord-safe)
        ist_now = datetime.now(IST)
        utc_time = ist_now.astimezone(pytz.utc)

        embed = discord.Embed(
            title="💰 Payment Received",
            color=0x2ecc71,
            timestamp=utc_time
        )
        embed.add_field(name="Amount", value=f"₹{amount}", inline=False)
        embed.add_field(name="From", value=user, inline=False)
        embed.add_field(name="Method", value=method, inline=False)
        embed.set_footer(text=f"Logged by {interaction.user}")

        await channel.send(embed=embed)
        await interaction.response.send_message(
            "✅ Money log added.",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Money(bot))
