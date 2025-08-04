import discord
from discord.ext import commands


class Reactions(commands.Cog, name=''):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Reactions(bot))
