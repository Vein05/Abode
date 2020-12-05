import discord
from discord.ext import commands



class vein11(commands.Cog, name='battle'):
    def __init__(self, client):
        self.client= client

    @commands.command()
    @commands.guild_only()
    async def battle(self, ctx, member: discord.Member):
        print("check")



def setup (client):
    client.add_cog(vein11(client))
    print("Battle cog is working.")
