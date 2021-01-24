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
        query = (re.sub("[ ,.]", "-", title))
        
        aqres = await fetch.fetch_anilist(query, 'anime')
        # print(aqres)
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
                # embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] !='No Data':
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                views = data['popularity']
                embed.add_field(name="Views", value=f"{views:,}")
               
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Genres", value=data['genres'], inline=False)

                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it ", value=f"[Here]({data['link']}) ")
                embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")
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
                embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                views = data['popularity']
                embed.add_field(name="Views", value=f"{views:,}")
                               
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it", value=f"[Here]({data['link']})")
                
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '⏩' in str(res.emoji):
              
                num = num + 1
                data = resdata[num - 1]

                embed = discord.Embed(color=0x19212d)

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
               

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Episode", value=data['episodes'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                views = data['popularity']
                embed.add_field(name="Views", value=f"{views:,}")
                
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="More about it", value=f"[Here]({data['link']})")
                embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '👍' in str(res.emoji):
               
                embed = discord.Embed(color=0x19212d)

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                

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
                eembed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")
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

    @commands.command()
    @commands.guild_only()
    #@commands.cooldown(1, 15, commands.BucketType.user)
    async def manga(self,ctx, *, title):
        
        
        aqres = await fetch.fetch_anilist(title, 'manga')
        if isinstance(aqres, str):
            return await ctx.send(aqres)

        max_page = aqres['data_total']
        resdata = aqres['result']
        

        first_run = True
        num = 1
        while True:
            if first_run:
                
                data = resdata[num - 1]
                embed = discord.Embed(color=random.choice(self.Bot.color_list))

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")
                
                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Chapter/Volume", value=data['ch_vol'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                views = data['popularity']
                embed.add_field(name="Views", value=f"{views:,}")
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Genres", value=data['genres'], inline=False)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="Read it ", value=f"[Here]({data['link']})")
                
                first_run = False
                msg = await ctx.send(embed=embed)

            reactmoji = []
            if max_page == 1 and num == 1:
                pass
            elif num == 1:
                reactmoji.append('⏩')
            elif num == max_page:
                reactmoji.append('⏪')
            elif num > 1 and num < max_page:
                reactmoji.extend(['⏪', '⏩'])
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
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Chapter/Volume", value=data['ch_vol'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                views = data['popularity']
                embed.add_field(name="Views", value=f"{views:,}")
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Genres", value=data['genres'], inline=False)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="Read it ", value=f"[Here]({data['link']})")
                
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '⏩' in str(res.emoji):
                
                num = num + 1
                data = resdata[num - 1]

                embed = discord.Embed(color=random.choice(self.Bot.color_list))

                embed.set_thumbnail(url=data['poster_img'])
                embed.set_author(name=data['title'], url=data['link'], icon_url=f'{ctx.me.avatar_url}')
                embed.set_footer(text=f"Requested by {ctx.author.name} | AniID: {data['ani_id']} MALID: {data['MALID']}")

                embed.add_field(name="Other Names", value=data['title_other'], inline=True)
                embed.add_field(name="Chapter/Volume", value=data['ch_vol'], inline=True)
                embed.add_field(name="Status", value=data['status'], inline=True)
                if data['score'] ==None:
                    embed.add_field(name="Scores", value=data['score'], inline=True)
                embed.add_field(name="Released", value=data['start_date'], inline=True)
                embed.add_field(name="Ended", value=data['end_date'], inline=True)
                embed.add_field(name="Format", value=data['format'], inline=True)
                embed.add_field(name="Source Material", value=data['source_fmt'], inline=True)
                embed.add_field(name="Genres", value=data['genres'], inline=False)
                embed.add_field(name="Synopsis", value=data['synopsis'], inline=False)
                embed.add_field(name="Read it ", value=f"[Here]({data['link']})")
                
                await msg.clear_reactions()
                await msg.edit(embed=embed)
            elif '✅' in str(res.emoji):
                await ctx.message.delete()
                return await msg.delete()

    



def setup (Bot):
    Bot.add_cog(anime(Bot))
    print("Anime cog is working.")