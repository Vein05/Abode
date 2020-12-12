import discord
import datetime
from datetime import datetime
from discord.ext import commands

starttime = datetime.utcnow()
class owner(commands.Cog, name='owner'):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
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


def setup (Bot):
    Bot.add_cog(owner(Bot))
    print("Owner command is working.")
