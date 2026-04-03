import discord
from discord.ext import commands, tasks

class CustomStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0

        self.status_list = [
            "Best Hosting • RyinClouds",
            "The New Era of Hosting",
            "Best Minecraft Servers",
            "Affordable VPS Plans",
            "Limitless Hosting Solutions"
        ]

        self.rotate_status.start()

    @tasks.loop(seconds=5)
    async def rotate_status(self):
        try:
            await self.bot.change_presence(
                status=discord.Status.online,
                activity=discord.CustomActivity(
                    name=self.status_list[self.index]
                )
            )
            print("custom status set:", self.status_list[self.index])

            self.index = (self.index + 1) % len(self.status_list)

        except Exception as e:
            print("failed to set custom status:", e)

    @rotate_status.before_loop
    async def before_rotate(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(CustomStatus(bot))
