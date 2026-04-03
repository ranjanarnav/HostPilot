import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PTERO_API_KEY = os.getenv("PTERO_API_KEY")

ALLOWED_ROLE_ID = int(os.getenv("ALLOWED_ROLE_ID"))
MONEY_LOG_CHANNEL_ID = int(os.getenv("MONEY_LOG_CHANNEL_ID"))
REPORT_CHANNEL_ID = int(os.getenv("REPORT_CHANNEL_ID"))

WEBSITE_LINK = os.getenv("WEBSITE_LINK")
PANEL_LINK = os.getenv("PANEL_LINK")
BILLING_LINK = os.getenv("BILLING_LINK")
DISCORD_INVITE = os.getenv("DISCORD_INVITE")
SUPPORT_LINK = os.getenv("SUPPORT_LINK")

PTERO_PANEL_URL = os.getenv("PTERO_PANEL_URL")
PTERO_ALLOCATION_ID = int(os.getenv("PTERO_ALLOCATION_ID"))

TIMEZONE = os.getenv("TIMEZONE")