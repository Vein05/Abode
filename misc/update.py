import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import random
from random import randint





class update(commands.Cog, name="update"):
	def __init__(self, Bot):
		self.Bot = Bot




	@commands.command()
	@commands.guild_only()
	# @commands.cooldown(1, 3600, commands.BucketType.user)
	async def update(self, ctx):
		author_id= str(ctx.author.id)
		db = self.Bot.cluster1['AbodeDB']
		collection= db['Levels']
		query = {"_id": author_id}
		find = collection.find(query)
		
        # checks if user is in the db or not
		for lvl in find:
			idd = lvl['_id']
			pathDB= lvl['Path']
			realm = lvl['Realm']

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
			name = lvl['Name']
			try:
				wisdomDB = lvl['wisdom']
			except:
				wisdomDB = random.randint(50, 100)  
			



			leauge = medal
			Qi = qi
			Realm = realm
			pointsO = points
			daos = dao
			path = pathDB
			race = speci
			strength = stre 
			speed = sped
			defense = defen
			soul = sol
			luck = luk
			Hp = health 
			print("chek1")
			
				

			query = {"_id": str(author_id)}
			collection.delete_one(query)
			print("check2")

			if (collection.find_one({"_id": author_id}) == None):
				print("chc3")

				user_data = {"_id": author_id, "points": pointsO, "Leauge": leauge, "Qi": Qi, "Daos": daos, "Path": path, "Realm": Realm, "Luck": luck,
								"Species": race, "Strength": strength, "Speed": speed, "Defense": defense, "Soul": soul, "Health": Hp, "Name": name
								, "Wisdom": wisdomDB
								}
				print(user_data)
				collection.insert_one(user_data)
				await ctx.send("Your stats have been updated, ``.stats`` to check.")



		
		






def setup (Bot):
	Bot.add_cog(update(Bot))
	print("Update cog is working.")