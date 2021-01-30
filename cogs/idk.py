from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands
import random
from disputils import BotEmbedPaginator

class movie(commands.Cog, name="movie"):
	
	def __init__(self,Bot):
		self.Bot = Bot

	@commands.command()
	@commands.guild_only()
	async def movie(self, ctx, *, title):
		send = await ctx.send(f"Searching for {title}")
		embeds = []
		for page in range(1, 2):
			name = title
			url = "https://yts.mx/browse-movies/" + str(
				   name) + "/all/all/0/seeds/0/all"
			r = requests.get(url).text
			soup = BeautifulSoup(r, "lxml")
			for name in soup.findAll(
				   "div",
				   class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"):
				mov_name = name.find("div", class_="browse-movie-bottom")
				movie_name = mov_name.a.text
				movie_year = mov_name.div.text
				movie_name = movie_name + " " + movie_year
				rating = name.find("h4", class_="rating", text=True)
				if rating is not None:
					rating = rating.text
					rating = rating[:3]
				else:
					rating = "0.0"
				if rating[2] == "/":
					rating = rating[0:2]
				try:
					
					if movie_name[0] == "[" and movie_name[3] == "]":
						movie_name = movie_name[5:]
					movie_name = movie_name.replace(" ", "-")
					index = 0
					for char in movie_name:  #Handles Special Character In Url
						if char.isalnum() == False and char != "-":
							movie_name = movie_name.replace(char, "")
					for char in movie_name:
						if char == "-" and movie_name[index + 1] == "-":
							movie_name = movie_name[:index] + movie_name[index + 1:]
						if index < len(movie_name) - 1:
							index = index + 1
					if "--" in movie_name:  #Handles Movie Url Containing "--"
						movie_name = movie_name.replace("--", "-")
					movie_url = "https://yts.mx/movie/" + movie_name
					movie_url = movie_url.lower()
					request = requests.get(movie_url).text
					n_soup = BeautifulSoup(request, "lxml")
					info = n_soup.find("div", class_="bottom-info")
					torrent_info = n_soup.find("p", class_="hidden-xs hidden-sm")
					genre = n_soup.findAll("h2")[1].text
					likes = info.find("span", id="movie-likes").text
					imdb_link = info.find("a", title="IMDb Rating")["href"]
					for torrent in torrent_info.findAll("a"):
						if (torrent.text[:3] == "720"):
							torrent_720 = torrent["href"]
						if torrent.text[:4] == "1080":
							torrent_1080 = torrent["href"]
				except Exception as e:
					likes = None
					genre = None
					num_downloads = None
					imdb_link = None
					torrent_720 = None
					torrent_1080 = None
					pass
				movie_name = mov_name.a.text

				embed = discord.Embed(color =random.choice(self.Bot.color_list) )
				embed.description=f"{movie_name}"
				embed.add_field(name="Year", value=f"{movie_year}")
				embed.add_field(name="IMDb link", value=f"[Here]({imdb_link})")
				embed.add_field(name="Ratings", value=f"{rating}")
				embed.add_field(name=f"Genres", value=f"{genre}", inline=False)
				embed.add_field(name=f"Download", value=f"[720p]({torrent_720}) ||"
														f"[1080p]({torrent_1080})")
				embeds.append(embed)

		paginator = BotEmbedPaginator(ctx, embeds)
		await send.delete()
		await paginator.run()
		
def setup (Bot):
	Bot.add_cog(movie(Bot))
	print("Movie cog is working.")