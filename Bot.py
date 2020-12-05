import discord
from discord.ext import commands
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
from ago import human
import time
import random
from random import randint
import aiohttp
from aiohttp import request, ClientSession
from discord.ext.commands import command, cooldown
import requests


client = commands.Bot(command_prefix = commands.when_mentioned_or('.'), case_insensitive=True, intents=intents )

client.remove_command("help")

#async def create_db_pool():
    #client.pg_con= await asyncpg.create_pool(database='db1crf5i3vgvh2', user='lkznvsbittpdyx', password='bb434c5fa9c5d40aade4d3147855b6dd31e59b9fa569a04b3af95282644435ce')
    #pool= await asyncpg.create_pool('postgres://lkznvsbittpdyx:bb434c5fa9c5d40aade4d3147855b6dd31e59b9fa569a04b3af95282644435ce@ec2-3-216-89-250.compute-1.amazonaws.com:5432/db1crf5i3vgvh2')
    #con= await asyncpg.connect('postgres://lkznvsbittpdyx:bb434c5fa9c5d40aade4d3147855b6dd31e59b9fa569a04b3af95282644435ce@ec2-3-216-89-250.compute-1.amazonaws.com:5432/db1crf5i3vgvh2')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help if you are lost '))
    print("Bot is running.")

'''@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=">help | >invite"))
    print(f'Bot iz Ready\n................\n{client.user.name}\n................\n{client.user.id}')'''



@client.event
async def on_command_error(ctx, error):
    #if isinstance(error, commands.MissingRequiredArgument):
        #await ctx.send(f'{ctx.message.author.mention} <:xmark:773959363379462184> The mandator suggests sending the correct command.', delete_after=5)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} <:xmark:773959363379462184> You don't meet all the requirements to use this command.", delete_after=5)
    if isinstance(error, commands.CommandOnCooldown):
         msg = " The command is on **Cooldown!** Try again after **{:.2f}s!**".format(error.retry_after)
         await ctx.send(f'{ctx.message.author.mention}, {msg}', delete_after = 5)
    '''if isinstance(error, commands.CommandNotFound):
        emojy = '❓'
        await ctx.message.add_reaction(emojy)'''

    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
        helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
        await ctx.send(f'{ctx.author.name} The correct way of using that commands is: ')
        await ctx.send_help(helper)





@client.command(aliases=['Hi', 'Namaste'])
@commands.guild_only()
async def hello(ctx):
    greetings = ['Hello', 'Hiya', 'nĭ hăo', 'Namaste', 'Konichiwa', 'Zdravstvuyte', 'Bonjour', 'Guten tag',
                 'Anyoung haseyo', 'Asalaam alaikum', 'Goddag', 'Selamat siang','hola', 'marhabaan	', 'hyālō',
                 'Sata srī akāla', 'Nggoleki', 'Vandanalu', '	Xin chào', 'Namaskār', 'Vaṇakkam', 'Salām', 'Merhaba', 'Ciao'
                 , 'Sà-wàt-dii', 'Kaixo', 'Cześć’', 'Namaskāra', 'Prannam', 'Kamusta', 'Hallo', 'Yasou', 'Hej', 'oi', 'Wazza', 'kem cho',
                 'Hai', 'doki-doki', 'meow meow ', 'Lí-hó', 'Vitaju' , 'Bok', 'Hej', 'Moi', 'Sveika /Sveiks ', 'God dag',
                 'Moïen ', 'Vitayu ', 'Aloha ', 'Wassup', 'Howdy!']
    reply = random.choice(greetings)
    await ctx.send(f'{reply}, {ctx.message.author.mention} How is it going for you? No need to ask me, but I am mostly good.')



@client.command()
@commands.guild_only()
async def ping (ctx):

        latency = round(client.latency *1000)
        await ctx.send  ( f'{ctx.message.author.name}, Pong! ``{latency}``ms')
        await ctx.message.delete()





@client.command(aliases= ['pmuser'])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def DMuser (ctx, user: discord.User, *, msg ):
    try:
     await user.send(f'**{ctx.message.author}** has a message for you, \n {msg}')
     await ctx.message.delete()

    except:
        await ctx.send(f'The user has his/her DMs turned off.')



















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
            'cogs.battle'

]
if __name__ == "__main__" :
    for extension in extensions:
        try :
            client.load_extension(extension)
        except Exception as e:
             print (f"Error loading the {extension}", file=sys.stderr)
             traceback.print_exc()




client.load_extension("jishaku")
#client.loop.create_task(create_db_pool())






client.run('NzU5Nzg0MDY0MzYxMjk5OTg5.X3CiDQ.f28fSsGzW98IKWeKnWQ81TPWt-c')
