from discord.ext import commands
import discord


class PublicCommands(commands.Cog, name='Public Commands'):

    def __init__(self, bot):
        self.bot = bot
        self.embed_help = {}
        self.embed_admin_help = {}
        self.thumbnail_url = ""

    def set_embed_help(self):
        self.embed_help = discord.Embed(
            title='''╔══════ ≪ °❈° ≫ ══════╗
                        Help Menu
╚══════ ≪ °❈° ≫ ══════╝

        ''',
            color=discord.Colour.magenta(),
        )
        self.embed_help.set_thumbnail(url='https://cdn.discordapp.com/avatars'
                                          '/766635489674788884/42fd6c0681304ce9863bdcfff83510e1.png?size=128')
        self.embed_help.add_field(name='\u200b', value='\u200b', inline=False)
        self.embed_help.add_field(name='Public Commands', value='≫ ──── ≪•◦ ❈ ◦•≫ ──── ≪', inline=False)
        self.embed_help.add_field(name='help', value='| Shows this help message.'
                                                     '\nUsage: .help', inline=True)
        self.embed_help.add_field(name='ping', value='| Pong! (Shows the Bots latency in ms)'
                                                     '\nUsage: .pong', inline=True)
        self.embed_help.add_field(name='\u200b', value='\u200b', inline=False)
        self.embed_help.add_field(name='Fun Commands', value='≫ ──── ≪•◦ ❈ ◦•≫ ──── ≪', inline=False)
        self.embed_help.add_field(name='who', value='| Who asked?'
                                                    '\nUsage: .who asked', inline=True)
        self.embed_help.add_field(name='8ball', value='| Answers your yes or no question.'
                                                      '\nUsage: .8ball "question"', inline=True)
        self.embed_help.add_field(name='random', value='| Sends a random image or wikipedia article.'
                                                       '\nUsage: .random image/wiki', inline=True)
        self.embed_help.add_field(name='roast', value='| Roasts you!'
                                                      '\nUsage: .roast @user or .roast "me"', inline=True)
        self.embed_help.add_field(name='\u200b', value='≫ ──── ≪•◦ ❈ ◦•≫ ──── ≪' + '\n\u200b', inline=False)
    
    def set_embed_admin_help(self):
        self.embed_admin_help = discord.Embed(
            title='''╔══════ ≪ °❈° ≫ ══════╗
                        Admin Help
╚══════ ≪ °❈° ≫ ══════╝

                ''',
            color=discord.Colour.magenta(),
        )
        self.embed_admin_help.set_thumbnail(url='https://cdn.discordapp.com/avatars/'
                                                '766635489674788884/42fd6c0681304ce9863bdcfff83510e1.png?size=128')
        self.embed_admin_help.add_field(name='\u200b', value='\u200b', inline=False)
        self.embed_admin_help.add_field(name='clear', value='| Clears x amount of messages.'
                                                            '\nUsage: .clear {x} (number of messages)', inline=True)
        self.embed_admin_help.add_field(name='load/unload/\nreload(r)', value='| Load/unload or reload a specific Cog.'
                                                                              '\nUsage: .r (cog)', inline=True)
        self.embed_admin_help.add_field(name='kick/ban', value='| Kick or ban a user.'
                                                               '\nUsage: .kick/ban @user', inline=True)
        self.embed_admin_help.add_field(name='give/take', value='| Give or Take a role to/from a user.'
                                                                '\nUsage: .g/t (role name/id) @user', inline=False)

    @commands.command()
    # Sends the bots ping.
    async def ping(self, ctx):
        await ctx.send(f'Pong! ({round(self.bot.latency * 1000)}ms)')

    @commands.command()
    # Shows help message.
    async def help(self, ctx, *args):
        self.set_embed_help()
        self.set_embed_admin_help()
        if len(args) == 0:
            await ctx.send(embed=self.embed_help)
        if args[0] == 'admin':
            if ctx.message.author.guild_permissions.administrator:
                await ctx.send(embed=self.embed_admin_help)
            else:
                raise commands.MissingPermissions(('administrator',))
        else:
            raise commands.BadArgument


def setup(bot):
    bot.add_cog(PublicCommands(bot))
