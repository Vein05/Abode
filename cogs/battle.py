import discord
from discord.ext import commands

color = 0xa100f2
guild = 757098499836739594
battle = ("put battle chnl id here")

class vein11(commands.Cog, name='battle'):
    def __init__(self, client):
        self.client= client

    @commands.command(aliases=['battle'])
    @commands.guild_only()
    async def challenge(self, ctx, member: discord.Member):
        if ctx.guild.id != (guild):
            return
        if ctx.channel.id != (757941959796195484):
            return
        if member.id == ctx.author.id:
            msg = ctx.message
            await msg.add_reaction('<:WeirdChamp:757112297096216627>')
            return
        if member.bot:
            return
        print('ok')



def setup (client):
    client.add_cog(vein11(client))
    print("Battle cog is working.")
