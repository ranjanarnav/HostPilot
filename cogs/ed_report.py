import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import pytz
import re
import io
import config

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

IST = pytz.timezone("Asia/Kolkata")

class EndOfDayReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.scheduler = AsyncIOScheduler(timezone=IST)
        self.scheduler.add_job(
            self.auto_daily_report,
            "cron",
            hour=23,
            minute=59
        )
        self.scheduler.start()

        print("✅ EOD Report Scheduler started (IST 23:59)")

    # ---------- COLLECT TODAY SALES (IST SAFE) ----------
    async def collect_sales(self):
        channel = await self.bot.fetch_channel(config.MONEY_LOG_CHANNEL_ID)

        today_ist = datetime.now(IST).date()
        entries = []
        total = 0

        async for msg in channel.history(limit=300):
            # Discord time is UTC → convert to IST
            msg_time_ist = msg.created_at.replace(tzinfo=pytz.utc).astimezone(IST)

            if msg_time_ist.date() != today_ist:
                continue

            if not msg.embeds:
                continue

            embed = msg.embeds[0]
            amount = None
            user = None

            for field in embed.fields:
                if field.name.lower() == "amount":
                    amount = int(re.sub(r"[^\d]", "", field.value))
                elif field.name.lower() == "from":
                    user = field.value

            if amount and user:
                total += amount
                entries.append((amount, user))

        return today_ist, entries, total

    # ---------- PDF GENERATOR ----------
    def generate_pdf(self, date, entries, total):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)

        y = 800
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "End Of The Day Sales Report")

        y -= 30
        c.setFont("Helvetica", 12)
        c.drawString(50, y, date.strftime("%d-%m-%Y"))

        y -= 40

        for amt, user in entries:
            c.drawString(50, y, f"₹{amt} Received From {user}")
            y -= 20
            if y < 50:
                c.showPage()
                y = 800

        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, f"Total Revenue : ₹{total:.2f}")

        c.save()
        buffer.seek(0)
        return buffer

    # ---------- MANUAL COMMAND ----------
    @app_commands.command(name="ed-report", description="Generate today's sales report")
    async def ed_report(self, interaction: discord.Interaction):
        await interaction.response.defer()

        date, entries, total = await self.collect_sales()

        if not entries:
            await interaction.followup.send("❌ No sales found today.")
            return

        text = "\n".join([f"₹{a} Recieved From {u}" for a, u in entries])
        report = (
            "**End Of The Day Sales Report**\n"
            f"{date.strftime('%d-%m-%Y')}\n\n"
            f"{text}\n\n"
            f"**Total Revenue : ₹{total:.2f}**"
        )

        pdf = self.generate_pdf(date, entries, total)

        await interaction.followup.send(
            content=report,
            file=discord.File(pdf, filename=f"EOD_Report_{date}.pdf")
        )

    # ---------- AUTO DAILY REPORT (IST 23:59) ----------
    async def auto_daily_report(self):
        try:
            date, entries, total = await self.collect_sales()
            if not entries:
                return

            channel = await self.bot.fetch_channel(config.REPORT_CHANNEL_ID)

            text = "\n".join([f"₹{a} Recieved From {u}" for a, u in entries])
            report = (
                "**📊 End Of The Day Sales Report**\n"
                f"{date.strftime('%d-%m-%Y')}\n\n"
                f"{text}\n\n"
                f"**Total Revenue : ₹{total:.2f}**"
            )

            pdf = self.generate_pdf(date, entries, total)

            await channel.send(
                content=report,
                file=discord.File(pdf, filename=f"EOD_Report_{date}.pdf")
            )

            print("✅ Auto EOD Report sent at 23:59 IST")

        except Exception as e:
            print("❌ EOD Report Error:", e)

async def setup(bot):
    await bot.add_cog(EndOfDayReport(bot))
