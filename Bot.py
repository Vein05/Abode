import discord
from discord.ext import commands
import sys
import os
import traceback
import discord.utils
from pymongo import MongoClient
import os

prefix = '.'
vein_id  = 427436602403323905
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    prefix), case_insensitive=True, intents=intents, owner_id=vein_id)
bot.DEFAULT_PREFIX = prefix
bot.remove_command("help")
bot.color = 0xa100f2
bot.guild_id = 757098499836739594
bot.github = "https://github.com/Vein05/Abode"
bot.cupped_fist = "<:Cuppedfist:757112296094040104>"


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('.help if you are lost '))
    print("Bot is running.")
    vein= bot.get_guild(bot.guild_id).get_member(vein_id)

    await vein.send("https://cdn.discordapp.com/attachments/774905992743747584/795535756759531530/sob.jpg")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} <:xmark:773959363379462184> You don't meet all the requirements to use this command.")
    if isinstance(error, commands.CommandOnCooldown):
        msg = " The command is on **Cooldown!** Try again after **{:.2f}s!**".format(
            error.retry_after)
        await ctx.send(f'{ctx.message.author.mention}, {msg}')

    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
        helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(
            ctx.command)
        await ctx.send(f'{ctx.author.name} The correct way of using that commands is: ')
        await ctx.send_help(helper)


bot.colors = {
    "WHITE": 0x26fcff,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "who_even_likes_red_bruh!": 0xa5ddff,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "Light_blue": 0x30ffcc,
    "ok": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "cool_color": 0x6891ff,
    "something": 0xfc7bb2,
    "DARK_NAVY": 0xe8c02a,
    "Hm": 0xebf54c,
    "nice_color": 0xfc00f1,
    "nice_color2": 0x21f5fc,
    "very_nice_color": 0x25c059,
    "my_fav": 0xb863f2
}
bot.color_list = [c for c in bot.colors.values()]


extensions = [
    'cogs.mod_commands',
    'cogs.fun_commands',
    'cogs.api_commands',
    'cogs.admin',
    'cogs.games',
    'cogs.custom',
    'cogs.db',
    'cogs.leveling',
    'cogs.help',
    'cogs.shop',
    'cogs.battle',
    'wuxia.cultivation',
    'cogs.owner',
    'misc.fist',
    'cogs.events',
    'misc.update',
    'cogs.anime',
    'wuxia.wuxia',
    'nsfw.hentaii'



]
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Error loading the {extension}", file=sys.stderr)
            traceback.print_exc()


bot.load_extension("jishaku")


TOKEN = os.environ.get("TOKEN")

bot.cluster1 = MongoClient(os.environ.get("DB1"))
bot.cluster2 = MongoClient(os.environ.get("DB2"))
bot.run(f"{TOKEN}")
