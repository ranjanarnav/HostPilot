import discord
from discord.ext import commands
import config
import os
import asyncio

# ------------------ INTENTS ------------------
intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",   # prefix exists but we only use slash
    intents=intents
)

# ------------------ READY EVENT ------------------
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Slash sync failed: {e}")

# ------------------ LOAD COGS ------------------
async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{file[:-3]}")
                print(f"✅ Loaded cog: {file}")
            except Exception as e:
                print(f"❌ Failed to load {file}: {e}")

# ------------------ STARTUP ------------------
async def main():
    async with bot:
        await load_cogs()
        await bot.start(config.DISCORD_TOKEN)

asyncio.run(main())
