import discord
from discord.ext import commands
import random
import requests
import re
from bs4 import BeautifulSoup
import cloudscraper
import lxml.html
import os 
import json 

try:
	path = "../things.json"

	with open(path, "r") as handler:
	    info = json.load(handler)

	ID = info["ID"]
	PW = info["PW"]
except:
	ID = os.environ.get("ID")
	PW = os.environ.get("PW")

class wuxia(commands.Cog, name="wuxia"):
    def __init__(self, Bot):
        self.Bot = Bot
        self.username = ID 
        self.password = PW 


    # @commands.command()
    # @commands.guild_only()
    # async def wuxia(self, ctx, *, name: str):
    #     query = (re.sub("[ ,.]", "-", name))

    #     # cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    #         }
    #     s = requests.session()
    #     response = s.get('https://www.novelupdates.com/login/', headers=headers)
        
        
    #     if response.status_code == 200:
    #         login_html = lxml.html.fromstring(response.text)
    #         hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    #         form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    #         form['log'] = self.username
    #         form['pwd'] = self.password
    #         argh = s.post('https://www.novelupdates.com/login/', data=form)
    #         a = 1
    #         if a ==1:
	   #          cookies = response.cookies
	   #          print(cookies)
	   #          url = f"https://www.novelupdates.com/series/{query}"
	   #          print(url)
	   #          soup = BeautifulSoup(requests.get(url, headers=headers, cookies=cookies).content, 'lxml')
	   #          print(soup)
	   #          chapters = soup.find('div', id="editstatus").text
	   #          year = soup.find('div', id="edityear").text
	   #          authors = soup.find('div', id="showauthors").text
	   #          ratings = soup.find('span', class_="uvotes").text
	   #          name = soup.find('div', class_="seriestitlenu").text
	   #          description = soup.find('div', id="editdescription").p.text
	   #          all_img = soup.find_all('img')
	   #          aliases = soup.find('div', id="editassociated").text
	   #          type_ = soup.find('div', id="showtype").text
	   #          is_translated = soup.find('div', id="showtranslated").text
	   #          is_lis = soup.find('div', id="showlicensed").text
	   #          og_pu = soup.find('div', id="showopublisher").text
	   #          eg_pu = soup.find('div', id="showepublisher").text
	   #          lang = soup.find('div', id="showlang").text
	   #          bruh = ''
	   #          for link in all_img:
	   #              url = link['src']
	   #              if f"{name[:3]}" in url:
	   #                  bruh = url
	   #                  break
	   #              if f"{name}" not in url:
	   #                  continue

	   #          embed = discord.Embed(color=random.choice(self.Bot.color_list))
	   #          embed.set_thumbnail(url=f"{bruh}")
	   #          embed.set_author(name=f"{name}", url=f"{url}", icon_url=f'{ctx.me.avatar_url}')
	   #          embed.add_field(name="Author", value=f"{authors}")
	   #          embed.add_field(name="Status in COO", value=f"{chapters}")
	   #          embed.add_field(name="Release date", value=f"{year}")
	   #          embed.add_field(name="Is completely translated?", value=f"{is_translated}")
	   #          embed.add_field(name="Is licensed?", value=f"{is_lis}")

	   #          # embed.add_field(name="Aliases", value=f"``{aliases}``")
	   #          embed.add_field(name="Type", value=f"{type_}")
	   #          embed.add_field(name="English publishers", value=f"{eg_pu}")
	   #          embed.add_field(name="Original publishers", value=f"{og_pu}")
	   #          embed.add_field(name="Laguage", value=f"{lang}")
	   #          embed.add_field(name="Description", value=f"{description}", inline=False)
	   #          embed.set_footer(text=f"Requested by {ctx.author} || Ratings {ratings}")
	        
	   #          await ctx.send(embed=embed)
	               
    #     # else:
	   #     #  await ctx.send("Error loading data")

def setup(Bot):
    Bot.add_cog(wuxia(Bot))
    print("Wuxia cog is working.")
