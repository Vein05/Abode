import discord
from discord.ext import commands


class vein6(commands.Cog, name= "custom"):
    def __init__(self, client):
        self.client = client 


    @commands.command()
    async def token(self, ctx):
        await ctx.send(f'https://pbs.twimg.com/media/EUqVvbQUcAAtL1H.jpg:large')

    @commands.command()
    async def vein2(self, ctx):
        await ctx.send(f'Why call the lord?')

    @commands.command()
    async def sap(self, ctx):
        await ctx.send(f'https://tenor.com/view/lotta-sap-christmas-vacation-christmas-tree-pine-tree-gif-16521866')

    @commands.command()
    async def vein(self,ctx):
        await ctx.send(f'https://media.discordapp.net/attachments/705447271285784578/722838393075007558/vein_orig.gif?width=1152&height=648')
        await ctx.message.delete()

    @commands.command()
    async def mortal(self,ctx):
        await ctx.send(f'https://media1.tenor.com/images/31411b30062cb1ca41e38c33e7d04840/tenor.gif?itemid=4331350')

    @commands.command()
    async def fate(self,ctx):
        await ctx.send(f'Fate knows no bound')

    @commands.command()
    async def leery(self,ctx):
        await ctx.send(f'https://tenor.com/view/party-pooper-everything-sucks-scott-pilgrim-vs-the-world-gif-6015471')


def setup (client):
    client.add_cog (vein6(client))
    print("Custom cog is working.")
