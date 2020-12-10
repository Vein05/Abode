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
        await ctx.send("Abode has been running for ``{}`` days ``{}`` hours ``{}`` mminutes and ``{}`` seconds".format(elapsed.days, hours, minutes, seconds))


def setup (Bot):
    Bot.add_cog(owner(Bot))
    print("Owner command is working.")
