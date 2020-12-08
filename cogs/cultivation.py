import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import asyncio



class cultivation(commands.Cog, name='Cultivation'):
    def __init__(self, Bot):
        self.Bot = Bot




def setup (Bot):
    Bot.add_cog (cultivation(Bot))
    print("Cultivation cog is working.")
