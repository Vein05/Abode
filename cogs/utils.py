import discord
from discord.ext import commands
from discord.ext.buttons import Paginator

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass






def setup(bot):
    bot.add_cog(Help(bot))
    print('Utils working')
