import discord
from discord.ext import commands, tasks
intents = discord.Intents.all()
import asyncio
from datetime import datetime
import sys
import os
import traceback
import discord.utils
import re
import json
import platform
import jishaku
import pymongo
from pymongo import MongoClient
import ago

import time
import random
from random import randint
import aiohttp
from aiohttp import request, ClientSession

import requests
import disputils
from discord.utils import get


prefix = '.'

bot = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), case_insensitive=True, intents=intents, owner_id=427436602403323905 )
bot.DEFAULT_PREFIX = prefix
bot.remove_command("help")
bot.color= 0xa100f2
bot.guild_id = 757098499836739594


#async def create_db_pool():
    #bot.pg_con= await asyncpg.create_pool(database='db1crf5i3vgvh2', user='lkznvsbittpdyx', password='bb434c5fa9c5d40aade4d3147855b6dd31e59b9fa569a04b3af95282644435ce')
    #pool= await asyncpg.create_pool('postgres://lkznvsbittpdyx:bb434c5fa9c5d40aade4d3147855b6dd31e59b9fa569a04b3af95282644435ce@ec2-3-216-89-250.compute-1.amazonaws.com:5432/db1crf5i3vgvh2')
    #con= await asyncpg.connect('postgres://lkznvsbittpdyx:bb434c5fa9c5d40aade4d3147855b6dd31e59b9fa569a04b3af95282644435ce@ec2-3-216-89-250.compute-1.amazonaws.com:5432/db1crf5i3vgvh2')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('.help if you are lost '))
    print("Bot is running.")
    ch = bot.get_channel(783715160833523722)
    await ch.send("Let's go!")

'''@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=">help | >invite"))
    print(f'Bot iz Ready\n................\n{bot.user.name}\n................\n{bot.user.id}')'''



@bot.event
async def on_command_error(ctx, error):
    #if isinstance(error, commands.MissingRequiredArgument):
        #await ctx.send(f'{ctx.message.author.mention} <:xmark:773959363379462184> The mandator suggests sending the correct command.', delete_after=5)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} <:xmark:773959363379462184> You don't meet all the requirements to use this command.")
    if isinstance(error, commands.CommandOnCooldown):
         msg = " The command is on **Cooldown!** Try again after **{:.2f}s!**".format(error.retry_after)
         await ctx.send(f'{ctx.message.author.mention}, {msg}')
    '''if isinstance(error, commands.CommandNotFound):
        emojy = '❓'
        await ctx.message.add_reaction(emojy)'''

    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
        helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
        await ctx.send(f'{ctx.author.name} The correct way of using that commands is: ')
        await ctx.send_help(helper)




bot.colors = {
    "WHITE": 0x26fcff,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "DARK_GREEN": 0x1F8B4C,
    "DARK_BLUE": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "DARK_ORANGE": 0xA84300,
    "DARK_RED": 0x992D22,
    "DARK_NAVY": 0xe8c02a,
    "Hm" : 0xebf54c
}
bot.color_list = [c for c in bot.colors.values()]


























extensions= [
            'cogs.mod_commands',
            'cogs.fun_commands',
            'cogs.api_commands',
            'cogs.admin',
            'cogs.games',
            'cogs.custom',
            'cogs.db',
            'cogs.leveling',
            'cogs.help',
            'cogs.shop',
            'cogs.battle',
            'cogs.cultivation',
            'cogs.owner',
            'misc.fist',
            'cogs.events'



]
if __name__ == "__main__" :
    for extension in extensions:
        try :
            bot.load_extension(extension)
        except Exception as e:
             print (f"Error loading the {extension}", file=sys.stderr)
             traceback.print_exc()




bot.load_extension("jishaku")
#bot.loop.create_task(create_db_pool())






bot.run('NzU5Nzg0MDY0MzYxMjk5OTg5.X3CiDQ.-ey8zjqE8emrZQQfEDk_AS1IyCo')
