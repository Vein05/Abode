import discord
from discord.ext import commands



class vein10(commands.Cog, name='shop'):
    def __init__(self, Bot):
        self.Bot= Bot




def setup (Bot):
    Bot.add_cog(vein10(Bot))
    print("Shop cog is working.")
