import discord 
from discord.ext import commands,tasks
import pymongo
from pymongo import MongoClient
import random


class cultivation(commands.Cog, name="cultivation"):
	def __init__(self, Bot):
		self.Bot = Bot
		self.cultivation_over.start()

	async def DataBase(self, ctx, user_id, return_=None, search=None):
		db = self.Bot.cluster1['AbodeDB']
		if search == None:
			collection= db['Levels1']
		elif search != None:
			collection = db['Levels']
		if return_ !=None:
			if (collection.find_one({"_id":user_id}) == None):
				if return_ == "true":
					
					return await ctx.send(f"{ctx.author.name}, There is no result about you on the DB.")
				elif return_ =="false":
					user_id = str(ctx.author.id)
					insertData = {"_id" : user_id, "cultivation": 1, "channelName" : ctx.channel.name}
					collection.insert_one(insertData)
		if return_ == None:
			if search != None:
				search = collection.find({"_id": user_id})
				return search


	@commands.command(aliases=["train"], description="One can use this command twice per day and will gain Qi after the cultivation session is over.")
	@commands.guild_only()
	@commands.cooldown(1, 43200, commands.BucketType.user)
	async def cultivate(self, ctx):
		await self.DataBase(ctx=ctx, user_id=ctx.author.id, return_="false")
		await ctx.send("Your cultivation time has started for the next few minutes.")


	@tasks.loop(seconds=600)
	async def cultivation_over(self):
		
		await self.Bot.wait_until_ready()
		guild =  self.Bot.get_guild(self.Bot.guild_id)
		db =  self.Bot.cluster1['AbodeDB']
		collection= db['Levels1']
		collection2 = db['Levels']
		searchUser = collection.find()
		channelName= None
		userID = 'blah'
		for user in searchUser:
			userID = user["_id"]
			channelName = user["channelName"]

		if channelName == None:
			return
		author_id= str(userID)
		
		query = {"_id": author_id}
		dbAnswer = collection2.find(query)
		
		randomQi = random.randint(10, 15)
		new_q = 0
		

		for user2 in dbAnswer:
			
			userID = user2["_id"]
			
			qi = user2['Qi']
			new_q = qi + randomQi
			collection2.update_one({"_id":userID}, {"$set": {"Qi":new_q}})
		
			
			
			cultivator =  guild.get_member(int(userID))
			channel =  discord.utils.get(guild.channels, name = f"{channelName}")
			
			await channel.send(f"{cultivator.mention} {self.Bot.cupped_fist} Your cultivation time is over. Through this session you have gained ``{randomQi}``,totalling your Qi to ``{new_q}``. ")
			collection.delete_one({"_id" :userID})












def setup (Bot):
	Bot.add_cog(cultivation(Bot))
	print("Cultivation cog is working.")