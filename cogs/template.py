import discord
from discord.ext import commands


class InsertClassHere(commands.Cog, name=''):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(InsertClassHere(bot))
