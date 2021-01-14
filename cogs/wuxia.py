import discord
from discord.ext import commands
import random
import requests
import re

class wuxia(commands.Cog, name="wuxia"):
	def __init__(self, Bot):
		self.Bot = Bot

	@commands.command()
	@commands.guild_only()
	async def wuxia(self, ctx, *, name: str):
		query = (re.sub("[ ,.]", "-", name))
		url = f"https://kooma-api.herokuapp.com/boxnovel/novels?title={query}"
		





def setup (Bot):
	Bot.add_cog(wuxia(Bot))
	print("Wuxia cog is working.")
