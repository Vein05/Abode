import discord
import datetime
from datetime import datetime
from discord.ext import commands

starttime = datetime.utcnow()
class owner(commands.Cog, name='owner'):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(hidden=True)
    @commands.is_owner()

    async def runtime(self,ctx):
        now = datetime.utcnow()
        elapsed = now - starttime
        seconds = elapsed.seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        embed = discord.Embed(color = self.Bot.color,timestamp=starttime ,description=f'**Abode has been running for ``{elapsed.days}`` days ``{hours}`` hours ``{minutes}`` mminutes and ``{seconds}`` seconds**')
        embed.set_author(name='Runtime', icon_url=ctx.me.avatar_url)
        embed.set_footer(text=f'Last restart')

        await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.guild_only()
    @commands.command(hidden=True)
    async def sayin(self, ctx, channel: discord.TextChannel, *, text: str):
        x = await channel.send(text)
        await x.add_reaction('<:phoCheck:786720919845994526>')


    '''@commands.command(aliases=['mc'])
    @commands.is_owner()
    async def messagecount(self, ctx):
        channel = ctx.channel
        a = 0
        msg = ctx.message
        await msg.add_reaction(':arrow_forward:')
        async for msg in channel.history(limit = None):
            a+= 1

        await msg.add_reaction(":white_check_mark: ")
        await ctx.send(f'{a} messages.')'''

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def emojilist(self, ctx):
        emojis = sorted([e for e in ctx.guild.emojis if len(e.roles) == 0 and e.available], key=lambda e: e.name.lower())
        paginator = commands.Paginator(suffix='', prefix='')
        channel = ctx.channel

        for emoji in emojis:
            paginator.add_line(f'{emoji} -- `{emoji}`')

        for page in paginator.pages:
            await channel.send(page)

        await ctx.send(ctx.tick(True))



def setup (Bot):
    Bot.add_cog(owner(Bot))
    print("Owner command is working.")
