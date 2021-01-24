import discord
from discord.ext import commands
import random
from wuxia.fetch1 import fetchNovel
import re





class wuxia(commands.Cog, name="wuxia"):
	def __init__(self, Bot):
		self.Bot = Bot


	@commands.command()
	@commands.guild_only()
	async def wuxia(self, ctx, *, name: str):
		query = (re.sub("[ ,.]", "-", name))
		x = fetchNovel(query)
		lang = str(x['language'])
		emjy= "🌐"
		if "Japanese" in lang:
			emjy = "<:Japanese:802096455962984468>"
		if "Chinese" in lang:
			emjy = "<:FlagChina:802097002364010527>"
		else:
			emjy = "<:English_language:802096460170395658>"
		activity= x['activityStats']
		activityWeek = activity['week']
		activitymonth = activity['month']
		activityalltime = activity['allTime']
		author = ", ".join(x['authors'])
		genre = ", ".join(x['genres'])
		description = x['description']

		embed = discord.Embed(color = random.choice(self.Bot.color_list)
			, title = f"{name.capitalize()}", url=f"https://www.novelupdates.com/series/{query}/"
			)
		embed.set_thumbnail(url=f"{x['image']}")	
		
		embed.add_field(name = "Year",value=f"{x['year']}")
		embed.add_field(name = "Language", value=f"{emjy} {x['language']}")
		embed.add_field(name = "Licensed", value=f"{x['licensed']}")
		embed.add_field(name = "Publisher", value=f"{emjy} Publishers: {x['publisher']}\n"
													f"<:English_language:802096460170395658> Publishers: {x['englishPublisher']}")
		embed.add_field(name="Chapters", value=f"{x['status']}", inline=False)
		embed.add_field(name = "Authors", value=f"{author}", inline=False)
		embed.add_field(name="Genres",  value=f"{genre}", inline=False)
		if len(description)>= 1023:
			embed.add_field(name = "Synopsis",  value = f"{description[:1020]}...", inline=False)
		else:
			embed.add_field(name = "Synopsis", value=f"{description}", inline=False)
		embed.add_field(name = "Tags", value=f", ".join(x['tags'][:25]), inline=False)
		embed.add_field(name = "Activity/Rank", value=f"Release Frequency: Every {x['releaseFrequency']} days\n"
												f"🇼🇼:regional_indicator_w: Weekly: {activityWeek}\n"
												f":regional_indicator_m: Montly: {activitymonth}\n"
												f":arrows_counterclockwise: All time: {activityalltime}")
		embed.add_field(name = "Ratings", value=f"⭐ {x['votes'][1]}\n"
												f"⭐⭐ {x['votes'][2]}\n"
												f"⭐⭐⭐ {x['votes'][3]}\n"
												f"⭐⭐⭐⭐ {x['votes'][4]}\n"
												f"⭐⭐⭐⭐⭐ {x['votes'][5]}\n"
												)
		embed.set_footer(text=f"Requested by {ctx.author.name}")
		await ctx.send(embed=embed)


        

def setup(Bot):
	Bot.add_cog(wuxia(Bot))
	print("Wuxia cog is working.")
