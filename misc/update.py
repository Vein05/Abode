import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient





class update(commands.Cog, name="update"):
	def __init__(self, Bot):
		self.Bot = Bot




	@commands.command()
	@commands.guild_only()
	async def update(self, ctx):
		author_id= (ctx.author.id)
		db = self.Bot.cluster1['AbodeDB']
		collection= db['Levels']

		query = {"_id": author_id}
		find = collection.find(query)
		

		for lvl in find:
			idd = lvl['_id']
			points = lvl['points']
			medal = lvl['Leauge']
			dao = lvl['Daos']
			stre = lvl['Strength']
			sped = lvl['Speed']
			defen = lvl['Defense']
			sol = lvl['Soul']
			health = lvl['Health']
			luk = lvl['Luck']
			qi = lvl['Qi']
			realm = lvl['Realm']
			speci = lvl['Species']
			pth = lvl['Path']
			nme = lvl['Name']	


		#when adding new things to the levelng add em trough here.
		await ctx.send("i don't have anything to do here tbh.")







def setup (Bot):
	Bot.add_cog(update(Bot))
	print("Update cog is working.")