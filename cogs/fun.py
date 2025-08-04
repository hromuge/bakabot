import discord
from discord.ext import commands
import random
import os
import wikipedia


intents = discord.Intents.default()
intents.members = True
intents.guilds = True


class FunCommands(commands.Cog, name='Fun Commands'):

    def __init__(self, bot):
        self.bot = bot
        self.images = []
        self.loadimages()

    def loadimages(self):
        files = os.listdir('/home/neko/discord/bakabot/images/')
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'):
                self.images.append(discord.File('/home/neko/discord/bakabot/images/' + file))

    @commands.command()
    # Asks, who asked.
    async def who(self, ctx, *args):
        if len(args) == 0:
            raise commands.BadArgument
        elif args[0] == 'asked':
            await ctx.send(f'Now Playing: Who asked (Feat: Nobody) \n ───────────⚪────── \n◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊')
        else:
            raise commands.BadArgument

    @commands.command(aliases=['8ball'])
    # Answers your yes or no question.
    async def _8ball(self, ctx, *args):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        if len(args) == 0:
            raise commands.BadArgument
        elif ctx.author.id == 580083680878395411:
            await ctx.send('nah, don\'t feel like it')
        elif len(args) != 0:
            await ctx.send(random.choice(responses))

    @commands.command()
    # Sends a random image or wikipedia article.
    async def random(self, ctx, *args):
        if len(args) == 0 or (args[0] != 'image' and args[0] != 'wiki'):
            raise commands.BadArgument
        elif args[0] == 'image':
            await ctx.send(file=random.choice(self.images))
        elif args[0] == 'wiki':
            wikia = wikipedia.random(1)
            summary = wikipedia.summary(wikia, sentences=10)
            await ctx.send(f'{wikia}\n{summary}')

    @commands.command()
    # Roasts you!
    async def roast(self, ctx, *args):
        roasts = [
            "one day you’ll meet a nice young gentleman with a Neanderthal fetish.",
            "you look like you're scared of birds because you think they're government drones.",
            "you've been swiped left so many times your nose permanently goes in that direction.",
            "you look like Harry styles if Harry styles was put in a blender.",
            "if they made generic store brand humans, you would be in the discount bin in the Asian aisle.",
            "that Hello Kitty rubber is the closest you'll ever get to pussy in your life.",
            "you look like you’re tired of disappointing yourself.",
            "on the bright side, if you want the touch of another person you can always go through airport security.",
            "you look and smell like STDs.",
            "Oh no, 2020 has manifested in physical form.",
            "if I roast you, it'll smell like burnt garbage in here.",
            "no need to roast because your parents do it already.",
            "the only thing you will ever be rich in is chromosomes.",
            "you look like you push kids of their bicycle to sniff on the saddle.",
            "your forehead is bigger than the great wall of China.",
            "people like you make stuff like 9/11 understandable.",
            "how long you been on the register?",
            "people only notice you when you're a problem.",
            "you look like a rejected Pixar character drawn by an artist with Parkinson's."
        ]
        if len(args) == 0:
            raise commands.BadArgument
        elif args[0] == 'me':
            await ctx.send(f'{ctx.author.mention}, {random.choice(roasts)}')
        elif ctx.author.id == 580083680878395411:
            await ctx.send('nah, don\'t feel like it')
        else:
            await ctx.send(f'{args[0]}, {random.choice(roasts)}')


def setup(bot):
    bot.add_cog(FunCommands(bot))
