import discord
from discord.ext import commands
from discord import app_commands

def admin_only():
    async def check(interaction: discord.Interaction):
        if interaction.user.guild_permissions.administrator:
            return True
        await interaction.response.send_message(
            "❌ Only server admins can use this command.",
            ephemeral=True
        )
        return False
    return app_commands.check(check)

class Client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="client-add",
        description="Add a client and assign plan role"
    )
    @admin_only()
    async def client_add(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        client_role: discord.Role,
        plan_role: discord.Role
    ):
        # Safety checks
        if client_role >= interaction.guild.me.top_role or plan_role >= interaction.guild.me.top_role:
            await interaction.response.send_message(
                "❌ I cannot assign roles higher than my role.",
                ephemeral=True
            )
            return

        # Add roles
        await user.add_roles(client_role, plan_role)

        await interaction.response.send_message(
            f"✅ **Client Added Successfully**\n"
            f"User: {user.mention}\n"
            f"Client Role: {client_role.mention}\n"
            f"Plan Role: {plan_role.mention}",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Client(bot))
