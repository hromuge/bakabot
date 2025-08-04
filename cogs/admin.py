import discord
from discord.ext import commands


class AdminCommands(commands.Cog, name='Admin Commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    # Kick a user.
    async def kick(self, ctx, *args):
        member_found = False
        for member in ctx.guild.members:
            if member.mention == args[0].replace("!", ""):
                await ctx.send(f'{member.mention} has been kicked from the server.')
                await member.kick()
                member_found = True
        if not member_found:
            await ctx.send(f'{ctx.author.mention}, please specify a user!')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    # Clears x amount of messages.
    async def clear(self, ctx, amount: int = 1):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(content=f'{amount} message(s) have been deleted.', delete_after=3)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    # Ban a user.
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned from the server.')

    # Give a role to a user.
    @commands.command(aliases=['g'])
    @commands.is_owner()
    async def give(self, ctx, given_role: discord.Role, member: discord.Member):
        if given_role is not None and given_role in ctx.guild.roles:
            await member.add_roles(given_role)
            await ctx.send(f'Given {given_role} role to {member.mention}.')

    # Remove/Take a role from a user.
    @commands.command(aliases=['t'])
    @commands.is_owner()
    async def take(self, ctx, given_role: discord.Role, member: discord.Member):
        if given_role is not None and given_role in ctx.guild.roles:
            await member.remove_roles(given_role)
            await ctx.send(f'Taken {given_role} role from {member.mention}.')


def setup(bot):
    bot.add_cog(AdminCommands(bot))
