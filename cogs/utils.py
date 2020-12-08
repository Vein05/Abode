import discord
from discord.ext import commands
from discord.ext.buttons import Paginator
color = 0xa100f2
class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass







