import discord
from discord.ext import commands
import hentai 
from hentai import Format, Hentai, Tag, Utils
import random
from cogs.utils import Pag
import asyncio
from disputils import BotEmbedPaginator
class hentaii(commands.Cog, name="hentaii"):
	def __init__(self, Bot):
		self.Bot = Bot
		self.page = 1

	@commands.command(aliases=['hid'])
	@commands.guild_only()
	@commands.cooldown(1, 15, commands.BucketType.guild)

	async def hsearch(self, ctx, id: int):
		if ctx.channel.is_nsfw():
			send = await ctx.send(f"<:nh3ntai:802131455215796224> Searching for ``{id}`` ")
			await ctx.message.delete()
			if not Hentai.exists(id):
				await ctx.send("404 not found")
			else:
			
				doujin = Hentai(id)
				language = Tag.get(doujin.language, property_="name")
				emoji = "🌐"
				if language == "english, translated":
					emoji = "<:English_language:802096460170395658>"
				if language == "japanese, translated":
					emoji = "<:Japanese:802096455962984468>"
				if language == "chinese, translated":
					emoji = "<:FlagChina:802097002364010527>"
				type_= Tag.get(doujin.category, property_="name")
				close = []
				for related in doujin.related:
					hmm = str(related.id)
					close.append(related.title(Format.Pretty))
				
				embed = discord.Embed(title=doujin.title(Format.Pretty),
				 url=doujin.url, color=random.choice(self.Bot.color_list))
				embed.add_field(name="Language", value=f"{emoji} ")

				embed.add_field(name="Author", value=Tag.get(doujin.artist, property_='name'))
				embed.add_field(name="Type", value = type_)
				if doujin.num_favorites == 0:
					embed.add_field(name="Favorites", value=f"For some reason this is broken :(")
				else:
					embed.add_field(name="Favorites", value=f"❤ {(doujin.num_favorites)}")
				embed.add_field(name="Pages", value=f"📕 {doujin.num_pages}")
				embed.set_thumbnail(url=doujin.thumbnail)
				thing= doujin.tag
				tags = []
				for tag in thing:
					x = Tag.get(thing, property_="name")
					

				embed.add_field(name="Tags",value=f"{x}", inline=False)
				if close != None:
					embed.add_field(name="Related",value=f" \n".join(close))
				embed.description=f"React with <:nh3ntai:802131455215796224> if you want to read this."
				await send.delete()
				x = await ctx.send(embed=embed)
				await x.add_reaction("<:nh3ntai:802131455215796224>")
				def check(reaction,user):
					
					return user == ctx.author and user.id != ctx.me.id
				try:
					reaction, user= await self.Bot.wait_for("reaction_add",timeout=30, check=check)
					await x.remove_reaction( emoji = f"<:nh3ntai:802131455215796224>" , member = ctx.author)
					if str(reaction.emoji) == f'<:nh3ntai:802131455215796224>':
						a =0 
						if a == 0:
							no = 0
							pages = []
							for images in doujin.image_urls:
								no =+ 1
								title = f"{doujin.title(Format.Pretty)}"
								link = images
								pages.append(link)
								
							
							
							list_ = pages
							embeds= []
							for i in list_:
							    e = discord.Embed(color = random.choice(self.Bot.color_list))

							    e.set_image(url=i)
							    embeds.append(e)

							paginator = BotEmbedPaginator(ctx, embeds)
							await paginator.run()
					
				except asyncio.TimeoutError:
					return
		else:

			await ctx.send("Please enable the NSFW option on the channels settings.")			  


def setup (Bot):
	Bot.add_cog(hentaii(Bot))
	print("Hentai cog is working.")