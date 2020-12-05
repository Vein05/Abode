import discord
import praw
from discord.ext import commands, tasks
import datetime
import random
import asyncio
import traceback
import aiohttp
from aiohttp import ClientSession
from aiohttp import ClientSession
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import requests
import urllib
from discord.ext.commands import command, cooldown



class vein3(commands.Cog, name= "APIs"):
    def __init__(self, client):
        self.client = client

    account=  praw.Reddit(client_id = "0H3JtzbIXbtZNw",
                         client_secret = "XKE_G2TxnXZY3nZQb8pOI17b10o",
                         username= "LordVein05",
                         passowrd= "vein6969",
                         user_agent= "Abode")



    @commands.command()
    @commands.guild_only()
    async def helpimages(self, ctx):
        embed= discord.Embed(title='Image commands or API commands ||commands have cooldowns||', colour=0x529dff)
        embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
        embed.add_field(name="dankmemes", value=f' Make Abode send a meme from Dankmemes subreddit', inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="pmemes", value= f'Make Abode send a meme from ProgrammerHumor subreddit', inline=False)
        embed.add_field(name="cat and catfact", value=  f' Make Abode send a woof picture ', inline=False)
        embed.add_field(name="dog and dogfact", value=   f' Make Abode send a meow picture ', inline=False)
        embed.add_field(name="panda and pandafact", value= f' Make Abode send cutuest pands', inline=False)
        embed.add_field(name="pikachu", value= f' Make Abode send a pikachu gif or an image', inline=False)
        embed.add_field(name="yearfact", value= f' Make Abode send a random fact on the mentioned year', inline=False)
        embed.add_field(name="clyde", value= f' Make clyde say something', inline=False)


        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dankmemes(self,ctx):

        account=  praw.Reddit(client_id = "_AhvH0lWxXDJhg",
                         client_secret = "n73tfGobbpfrhSrAXb4RmDoPH6U",
                         username= "LordVein05",
                         passowrd= "vein6969",
                         user_agent= "Abode")

        subreddit = account.subreddit("dankmemes")
        all_subs = []

        top= subreddit.top (limit=70)
        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name= random_sub.title
        url= random_sub.url

        embed= discord.Embed(title= name, colour=0x529dff)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}, Source: DankMemes")
        await ctx.send(embed=embed)


    @commands.command(aliases=['pmeme'])
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def Pmemes(self,ctx):

        account=  praw.Reddit(client_id = "_AhvH0lWxXDJhg",
                         client_secret = "n73tfGobbpfrhSrAXb4RmDoPH6U",
                         username= "LordVein05",
                         passowrd= "vein6969",
                         user_agent= "Abode")

        subreddit = account.subreddit("ProgrammerHumor")
        all_subs = []

        top= subreddit.top (limit=50)
        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name= random_sub.title
        url= random_sub.url

        embed= discord.Embed(title= name, colour=0x529dff)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}, Source : ProgrammerHumor", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dog(self, ctx):
        try:
            async with ctx.channel.typing():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                        data = await r.json()

                        embed = discord.Embed(title="Woof", colour=0x529dff)
                        embed.set_image(url=data['message'])
                        embed.set_footer(text=f"Requested by {ctx.author}, Source: Thedogapi", icon_url=ctx.author.avatar_url)

                        await ctx.send(embed=embed)
        except:
                await ctx.send(f'Command on cooldown for some seconds.', delete_after=5)




    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def clyde(self, ctx, *, text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=0x529dff

                )
                embed.set_image(url=res['message'])
                embed.set_footer(text=f'Requested by {ctx.author.name}, Source : Nekobot.xyz',icon_url=ctx.author.avatar_url)

                await ctx.send(embed=embed)
                await ctx.message.delete()


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def yearfact (self, ctx):

        async with aiohttp.ClientSession() as cs:

            async with cs.get(f"http://numbersapi.com/random/year?json") as r:
                data = await r.json()

                embed = discord.Embed(title= data['number'], description=data['text'], colour=0x529dff)

                embed.set_footer(text=f"Requested by {ctx.author}, Fact from numbersapi.com", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def pandafact(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/facts/panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Panda fact", colour=0x529dff)
                    embed.set_author(name=data['fact'])
                    embed.set_footer(text=f"Requested by {ctx.author}, Source: Some-random-api", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def catfact(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/facts/cat") as r:
                 data= await r.json()

                 embed = discord.Embed(title="Cat fact :D", colour=0x529dff)
                 embed.set_author (name=data['fact'])
                 embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)
                 await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dogfact(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/facts/dog") as r:
                 data= await r.json()

                 embed = discord.Embed(title="Dog fact :D", colour=0x529dff)
                 embed.set_author (name=data['fact'])
                 embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)

                 await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def cat(self, ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow", colour=0x529dff)
                    embed.set_image(url=data['file'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source : Aws.randam.cat/meow", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def panda(self, ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Pandasound :P", colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def koala(self, ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/koala") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Koala sound :P", colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)



    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def pikachu(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/pikachu") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Pika pika" ,colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source some random api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)



    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def numberfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://numbersapi.com/random?json") as r:
                data = await r.json()

                embed = discord.Embed(title=data['number'], description=data ['text'],colour=0x529dff)
                embed.set_footer(text=f"Requested by {ctx.author}, Fact from numbersapi.com", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def advice(self, ctx):
        r = requests.get("https://api.adviceslip.com/advice").json()
        advice= r["slip"]["advice"]
        embed = discord.Embed(title=advice ,colour=0x529dff)
        embed.set_footer(text=f"Requested by {ctx.author}, adviceslip.com", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)




    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def aquote(self, ctx):
       async with aiohttp.ClientSession() as cs:
           async with cs.get(f'https://some-random-api.ml/animu/quote') as r:

                data = await r.json()
                by = data['characther']
                anime= data['anime']
                quote= data['sentence']

                embed = discord.Embed(title=f'"{quote}"', colour=0x529dff)
                embed.set_author(name=f'By {by} from {anime}')
                embed.set_footer(text=f'Requested by {ctx.author}, Quote from some-random-api')
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def headpat(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/pat") as r:
                    data = await r.json()

                    embed = discord.Embed(title="There there everything will be better" ,colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source some random api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def wink(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/wink") as r:
                    data = await r.json()

                    embed = discord.Embed(title=";)" ,colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source some random api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def hug(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/hug") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Hug!!!!!" ,colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source some random api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def facepalm(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/face-palm") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Palm to the face" ,colour=0x529dff)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source some random api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
def setup (client):
    client.add_cog (vein3(client))
    print("APIs cog is working.")
