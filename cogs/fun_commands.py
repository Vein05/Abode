import discord
from discord.ext import commands, tasks
intents = discord.Intents.default()
import asyncio
import datetime
import random
import traceback
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
from collections import  Counter
import json
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown
from random import choice, randint
from typing import Optional
from aiohttp import request
from aiohttp import ClientSession
import collections
from discord.ext.commands import clean_content
from random import choice as randchoice
import pymongo
from pymongo import MongoClient
import requests
from datetime import timedelta
import ago
from ago import human

guild = 757098499836739594
color = 0xa100f2

class vein2(commands.Cog, name= "fun"):
    def __init__(self, client):
        self.client = client





    @commands.command(description='Show\'s mentioned users profile picture or if the user isn\'t mentioned the author\'s.', aliases=['av'])
    async def avatar (self, ctx , member: discord.Member=None):
        member =member or ctx.author
        embed= discord.Embed(color=0x529dff)
        embed.set_image(url= member.avatar_url_as(size=128))
        await ctx.send(embed=embed)


    @commands.command(aliases=['whois', 'ui'])
    @commands.guild_only()
    async def userinfo(self,ctx, member: discord.Member=None):
        ch = 781535649843904562

        if ctx.channel.id != (ch):

            msg = ctx.message
            return await msg.add_reaction('<:xmark:773959363379462184>')
        member = member or ctx.author
        if ctx.guild.id != (guild):
            uroles = []
            for role in member.roles[1:]:
                if role.is_default():
                    continue
                uroles.append(role.mention)

                uroles.reverse()

            time = member.created_at
            time1= member.joined_at

            embed=discord.Embed(color=color, timestamp=ctx.message.created_at, type="rich")
            embed.set_thumbnail(url= f"{member.avatar_url}")
            embed.set_author(name=f"{ctx.author.name}'s information",icon_url=f'{ctx.me.avatar_url}')
            embed.add_field(name="ㅤ",value=f'**Nickname:** {member.display_name}\n\n'
                                                            f'**ID** {member.id}\n\n'
                                                            f'**Account created:** {human(time, 4)}\n\n'
                                                            f'**Server joined at:** {human(time1, 3)}\n\n'
                                                            f'**Role(s):** {", ".join(uroles)}\n\n'
                                                            f'**Highest role:** {member.top_role.mention}'
                                                             , inline=False)

            embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif ctx.guild.id == (guild):
            member_id= str(member.id)

            mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

            cluster= MongoClient(mongo_url)
            db = cluster['AbodeDB']

            collection= db['Levels']
            qurey = {"_id" : member_id}
            users = collection.find(qurey)
            for user in users:
                realm = user['Realm']
                pth = user['Path']
                specy = user['Species']


            uroles = []
            for role in member.roles[1:]:
                if role.is_default():
                    continue
                uroles.append(role.mention)

                uroles.reverse()
            timestamp = 'ㅤ'
            time = member.created_at
            time1= member.joined_at
            if member.status == discord.Status.online:
                status= '<:online:769826555073003521>'
            elif member.status == discord.Status.idle:
                status= '<:idle:769826555479588864>'
            elif member.status== discord.Status.dnd:
                status = '<:dnd:769826555865989153>'
            else:
                status = '<:offline:769826555643691041>'
            if member.activity == None:
                activity = 'None'
            else:
                activity = member.activities[-1].name
                try:
                    timestamp = member.activities[0].details
                except:
                    timestamp ='ㅤ'
            embed=discord.Embed(color=color, timestamp=ctx.message.created_at, type="rich")
            embed.set_thumbnail(url= f"{member.avatar_url}")
            embed.set_author(name=f"{ctx.author.name}'s information",icon_url=f'{ctx.me.avatar_url}')
            embed.add_field(name="__General information__",value=f'**Nickname :** {member.display_name}\n'
                                                            f'**ID :** {member.id}\n'
                                                            f'**Account created :** {human(time, 4)}\n'
                                                            f'**Server joined :** {human(time1, 3)}\n'
                                                            ,inline=False)
            embed.add_field(name="__Cultivation info__", value= f'**Realm :** {realm} realm\n'
                                            f'**Species :** {specy} \n'
                                            f'**Path : ** {pth} \n')
            embed.add_field(name="__Role info__", value= f'**Highest role :** {member.top_role.mention}\n'
                                                        f'**Color** : {member.color}\n'
                                                        f'**Role(s) :** {", ".join(uroles)}\n'
                                               , inline=False)
            embed.add_field(name="__Presence__", value =f'**Status : ** {status}\n'
                                                        f'**Activity : ** {activity}  \nㅤㅤㅤㅤ{timestamp}')
            embed.set_footer(text=f"Requested by {ctx.author.name}",  icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)








    @commands.command(aliases= ['8ball', 'question'])
    async def _8ball (self,ctx, *, question ):
        responses = [' It is certain.',
                    'It is decidedly so.',
                    ' Without a doubt.',
                    'Yes – definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Sings point to yes.',
                    'I know this is off topic but, master Vein is the best.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'concentrate and ask again.',
                    'Donot count on it.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
        await ctx.send (f'{ctx.message.author.mention} The decree of mandator fortells: ** {random.choice(responses)}**')







    @commands.command(aliases=['wel'])
    @commands.guild_only()
    async def welcome(self,ctx):
        await ctx.send(f'<:Cuppedfist:769143163414773760> Welcome to Abode of Scholars, enjoy your stay here.')

    @commands.command(aliases=['servercount','membercount'])
    @commands.guild_only()
    async def members(self,ctx):
        embed=discord.Embed(color=0x529dff)
        embed.add_field(name="Total members", value=f"{ctx.guild.member_count}", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(aliases=['si'])
    @commands.guild_only()
    async def serverinfo(self, ctx):
        ch = 781535649843904562

        if ctx.channel.id != (ch):

            msg = ctx.message
            return await msg.add_reaction('<:xmark:773959363379462184>')
        guild= ctx.guild
        emojis = str(len(guild.emojis))

        channels = str(len(guild.channels))
        roles= str(len(guild.roles))
        time= ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")
        voice= str(len(guild.voice_channels))
        text= str(len(guild.text_channels))
        statuses = collections.Counter([member.status for member in guild.members])

        online = statuses[discord.Status.online]
        idel = statuses[discord.Status.idle]
        dnd = statuses[discord.Status.dnd]
        offline= statuses[discord.Status.offline]

        embed= discord.Embed(
                                timestamp= ctx.message.created_at, color=color )

        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=f"Information for  {ctx.guild.name}")
        embed.add_field(name="__General information__\n", value= f'**Server name : ** {guild.name}\n'
                                                               f'**Server region : ** {guild.region}\n'
                                                               f'**Server ID : ** {guild.id}\n'
                                                               f'**Created at : ** {time}\n'
                                                               f'**Verification level : ** {guild.verification_level} \n'
                                                               f'**Server owner : ** Vein \n'
                                                               f'**Server bot : ** Abode (by Vein)', inline=False)


        embed.add_field(name="\n\n\n__Statistics__", value= f'**Member count : ** {ctx.guild.member_count}\n'
                                                 f'**Role count : ** {roles} \n'
                                                 f'**Channel count : ** {channels}\n'
                                                 f'**Text channels :** {text}\n'
                                                 f'**Voice channels :** {voice}\n'
                                                 f'**Emoji count : ** {emojis}\n'
                                                 f'**Server boosters : ** {guild.premium_subscription_count}\n')

        embed.add_field(name="__Activity__", value= f'<:online:769826555073003521>{online}\n'
                                                    f'<:idle:769826555479588864>{idel}\n'
                                                    f'<:dnd:769826555865989153>{dnd}\n'
                                                    f'<:offline:769826555643691041>{offline}')


        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @serverinfo.error
    async def command_name_here_error(self,ctx, e):
        tb = '\n'.join(traceback.format_exception(type(e), e, e.__traceback__))
        await ctx.send(tb[:2000])







    @commands.command(aliases=['serverinvite'])
    async def invite(self,ctx):
        await ctx.send(f'https://discord.gg/tA4PDtX')



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()

    async def echo(self, ctx,*, arg):
        await ctx.send(arg)
        await ctx.message.delete()



    @commands.command(aliases=['lennyface'])
    @commands.guild_only()


    async def lenny( self, ctx):
        lennys= ['( ͡° ͜ʖ ͡°)', 'ಠ_ಠ', '( ͡ʘ ͜ʖ ͡ʘ)', '(▀̿Ĺ̯▀̿ ̿)', '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)', '( ͡ᵔ ͜ʖ ͡ᵔ )',
                 '(╯ ͠° ͟ʖ ͡°)╯┻━┻', 'ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ', '(✿╹◡╹)', 'щ（ﾟДﾟщ） < "Dear god why‽ )', '(人◕ω◕)', '(*бωб)', 'ヽ(͡◕ ͜ʖ ͡◕)ﾉ',
                 '(⌐▀͡ ̯ʖ▀)︻̷┻̿═━一-', 'ᕕ(╯°□°)ᕗ' ]
        await ctx.send(random.choice(lennys))
        await ctx.message.delete()

    @commands.command(aliases=['coin'])
    @commands.guild_only()

    async def flip(self,ctx):
        value=['Heads', 'Tails']
        await ctx.send (random.choice(value))






    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def lovemeter(self, ctx, name1: clean_content, name2: clean_content ):
        percentage = random.randint(0, 100)

        if 0 <= percentage <= 10:
            result= ['Friendzone',
                     'You sure it was love-metre not friend-metre ',
                     'Dude that is insultingly low.]',
                     'Ahh the classic ``one sided love``',
                     'Just friends?',
                     'Is my metre off today? Can not pick any numbers']

        elif 10<= percentage <= 30:
            result=['Huh, just started dating?',
                     'I guess friendzone never ends',
                     'Best-friend zone?',
                     'My metre picked something up']

        elif 30 <= percentage <=50:
            result=['Still one sided, next time bud',
                     'There is still alot room for love',
                     'I mean it is a good start',
                     'There is potential']


        elif 50<= percentage <= 70:
            result= ['I sense love here',
                     'Oh... love birds?',
                     'Love is in the air',
                     'My metre picked something big',
                     'There is still a long road ahead, stay strong :D',
                     'I mean acceptable']

        elif 70<= percentage <=90:
            result= ['Just got wed?',
                     'Very good relationship',
                     'I do not talk much with love birds',
                     'My metre says it is looking good ',
                     'Just steps below the perfect match']

        elif 90<= percentage <=100:
            result= ['Yoo dude that iss real love',
                     'Romeo and Juliet?',
                     'My metre nearly exploded',
                     'Adam and Eve?',
                     'Match made in heavens']


        if percentage <= 33:
            shipColor = 0x000000
        elif 33 < percentage < 66:
            shipColor = 0xe3ff00
        else:
            shipColor = 0xee66ee


        if percentage <= 10:
            gif =  "https://media.tenor.com/images/8eb3ea6f8b8e05115a37df84ba03144a/tenor.gif"
        if 10 < percentage <=30:
            gif= "https://media.tenor.com/images/d9f4ebad1365272d2605a1a5151d501a/tenor.gif"
        if 30 < percentage <=50:
            gif = "https://media.tenor.com/images/12414d69b8a99bd6dc19275363e17554/tenor.gif"
        if 50 <percentage <= 70:
            gif = "https://64.media.tumblr.com/09efd576d1e31d6dbf2a66eaa07ef6af/tumblr_n52l5bmodz1tt23n5o1_500.gif"
        if 70 < percentage <= 100:
            gif = "https://media.tenor.com/images/d85ef0ba33daf46de0838eba3efe8d08/tenor.gif"


        final_result= random.choice(result)

        embed= discord.Embed(color=shipColor,
                             title= f"Love metre of {name1} and {name2}")
        embed.set_thumbnail(url=f'{gif}')
        embed.add_field(name="Results:", value=f'{percentage}% ', inline=True)

        embed.add_field(name="Personal opinion :", value=f'{final_result}', inline=False)

        embed.set_author(name="Abode")
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)



    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def happy(self, ctx):
        await ctx.send(f'https://media1.tenor.com/images/3419ea3da202cf42d6c7ab37a7fcd44e/tenor.gif')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def sad(self, ctx):
        await ctx.send(f'https://media1.tenor.com/images/09b085a6b0b33a9a9c8529a3d2ee1914/tenor.gif')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def angry(self, ctx):
        await ctx.send(f'https://tenor.com/view/anime-angry-evil-plan-gif-14086662')

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def f(self, ctx):
        await ctx.send(f'{ctx.author.display_name} paid their respects.')


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def embed(self, ctx, *, string):
        ch = 781535649843904562

        if ctx.channel.id != (ch):

            msg = ctx.message
            return await msg.add_reaction('<:xmark:773959363379462184>')
        embed=discord.Embed(description=f'{string}', color=ctx.author.color)
        await ctx.send(embed=embed)




    '''@commands.command()
    async def addnote(self, ctx, *, note):

        author_id= str(ctx.message.author.id)
        user= await self.client.pg_con.fetchrow("SELECT * FROM notes WHERE user_id= $1 ", author_id)
        if user is None:
            await self.client.pg_con.execute("INSERT INTO notes (user_id, usernote) VALUES ($1, $2)", author_id, note)
            return await ctx.send(f'Just added a note for {ctx.message.author.display_name}')

        await self.client.pg_con.execute("UPDATE notes SET usernote= $1 WHERE user_id= $2",note,author_id)
        return await ctx.send(f'Just updated note for {ctx.message.author.display_name}')

    @commands.command()
    async def note(self,ctx):
        author_id= str((ctx.message.author.id))
        user= await self.client.pg_con.fetchrow("SELECT * FROM notes WHERE user_id = $1", author_id)
        if user is None:
            return await ctx.send('{ctx.message.author.display_name} ``.addnote`` using the following command  add a note before trying this command out.')
        else:
            embed= discord.Embed(color=ctx.author.colour)
            embed.set_author(name=f'Note for {ctx.message.author.display_name}', icon_url=ctx.author.avatar_url)
            embed.add_field(name=f'Details', value= user['usernote'])
            await ctx.send(embed=embed)'''




def setup (client):
     client.add_cog (vein2(client))
     print("Fun cog is working.")
