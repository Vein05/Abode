import discord
from discord.ext import commands
import requests
import asyncio
import time
from datetime import datetime, timedelta
import aiohttp
import random
from misc.fetch import fetch 
from ago import human
import re
from cogs.utils import Pag
import aiomangadexapi
from fundoshi import parse_chapter
import os
from disputils import BotEmbedPaginator


class anime(commands.Cog, name='anime'):
    def __init__(self, Bot):
        self.Bot = Bot






    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def anime(self,ctx, *, title):
        
        
        aqres = await fetch.fetch_anilist(title, 'anime')
        if isinstance(aqres, str):
            return await ctx.send(aqres)

        max_page = aqres['data_total']
        resdata = aqres['result']
        

        first_run = True
        time_table = False
        num = 1
        while True:
            if first_run:
                
                data = resdata[num - 1]
                embed = discord.Embed(color=random.choice(self.Bot.color_list))

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=data['footer'])

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it ", value=f"[Here]({data['link']})")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                first_run = False
                msg = await ctx.send(embed=embed)

            reactmoji = []
            if time_table:
                reactmoji.append('👍')
            elif max_page == 1 and num == 1:
                pass
            elif num == 1:
                reactmoji.append('⏩')
            elif num == max_page:
                reactmoji.append('⏪')
            elif num > 1 and num < max_page:
                reactmoji.extend(['⏪', '⏩'])
            if 'next_episode' in data and not time_table:
                reactmoji.append('⏳')
            reactmoji.append('✅')

            for react in reactmoji:
                await msg.add_reaction(react)

            def check_react(reaction, user):
                if reaction.message.id != msg.id:
                    return False
                if user != ctx.message.author:
                    return False
                if str(reaction.emoji) not in reactmoji:
                    return False
                return True

            try:
                res, user = await self.Bot.wait_for('reaction_add', timeout=30.0, check=check_react)
            except asyncio.TimeoutError:
                return await msg.clear_reactions()
            if user != ctx.message.author:
                pass
            elif '⏪' in str(res.emoji):
               
                num = num - 1
                data = resdata[num - 1]

                embed = discord.Embed(color=random.choice(self.Bot.color_list))

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'],  icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=data['footer'])

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it", value=f"[Here]({data['link']})")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '⏩' in str(res.emoji):
              
                num = num + 1
                data = resdata[num - 1]

                embed = discord.Embed(color=0x19212d)

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=data['footer'])

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it", value=f"[Here]({data['link']})")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '👍' in str(res.emoji):
               
                embed = discord.Embed(color=0x19212d)

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=data['footer'])

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it", value=f"[Here]({data['link']})")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                time_table = False
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '⏳' in str(res.emoji):
               
                ep_txt = 'Episode ' + str(data['next_episode'])
                embed = discord.Embed(color=0x19212d)
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text='Airing at {}'.format(data['airing_date']))

                embed.add_field(name=ep_txt, value=data['time_remain'], inline=False)

                time_table = True
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '✅' in str(res.emoji):
                await ctx.message.delete()
                return await msg.delete()


    @commands.command(aliases=['msearch'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.guild_only()
    async def manga(self, ctx, *, mangaName):
        self.username = os.environ.get("ID")
        self.password = os.environ.get("PW")
        session = await aiomangadexapi.login(username=f'{self.username}'
            ,password=f'{self.password}')  
        manga = await aiomangadexapi.search(session=session, name=f"{mangaName}")
        alternative1 = []
        chapter_read= []
        for result in manga:
            id_= result['id']
            title = result['title']
            stars = result['stars']
            alternative = result['alternative']
            mangaLink = result['link']
            cover= result['image'] 
            genre = result['genre']   
            author = result['author'] 
            views = result['views']  
            chapters = result['chapters']
            status = result['status']
            if status == 1:
                status = "On-going"
            elif status ==2:
                status = "Completed" 
            latest = result['latest']
            description =result['description']
            chapters_read = result['chapters_read']

        await session.close()
        
        
       
        embed = discord.Embed(color=random.choice(self.Bot.color_list),
            )
        embed.set_thumbnail(url=cover)
        embed.set_author(name=title, url=mangaLink, icon_url=f'{ctx.me.avatar_url}')
        embed.add_field(name="ID", value=f"Manga ID: {id_}")
        embed.add_field(name="Authors", value=f"{author}")
        embed.add_field(name="Rating", value=f"{stars}")
        embed.add_field(name="Status", value=f"{status}")
        if status == "On-going":
            embed.add_field(name="Latest chapter", value = f"[Here]({latest})")
        if views!= None:
            embed.add_field(name="View", value=f"{views:,}")
        embed.add_field(name="Chapters", value=f"{chapters}")

        embed.add_field(name="Genres", value= f"{genre}", inline=False)
        if not alternative:
            embed.add_field(name="Other names", value =f"None")
        if alternative:
            embed.add_field(name="Other names", value =f", ".join(alternative))
        if len(description) > 1024:
            embed.add_field(name="Synopsis", value=f'{description[25:1021]}...', inline=False)
        else:
            embed.add_field(name="Synopsis", value=f'{description[25:]}', inline=False)
        
        send = await ctx.send(embed=embed)

        self.readit = "<:Cuppedfist:757112296094040104>"
        await send.add_reaction(f"{self.readit}")
        await send.add_reaction("✅")
        

        def check(reaction,user):
            return user == ctx.author and user.id != ctx.me.id
        try:
            reaction, user= await self.Bot.wait_for("reaction_add",timeout=30, check=check)
            if str(reaction.emoji) == f'✅':
                try:
                    await send.delete()    
                except:
                    return await ctx.send("Something wrong happened.")
            # if str(reaction.emoji) == f'🔢':
            #     try:
            #         await send.edit(content = f"``{chapters_read}``", embed=None)
                    
            #     except:
            #         return await ctx.send(f"Too long to send it here. Get the chapters from <{mangaLink}>.")

            if str(reaction.emoji) ==f'{self.readit}':
                try:
                    await ctx.send(f"Coming soon....")
                except:
                    return

        except asyncio.TimeoutError:
                    return        



def setup (Bot):
    Bot.add_cog(anime(Bot))
    print("Anime cog is working.")