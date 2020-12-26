import discord
import datetime
from datetime import datetime
from discord.ext import commands
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import PIL.ImageFilter
from io import BytesIO
from discord.utils import get
import random

starttime = datetime.utcnow()
class owner(commands.Cog, name='owner'):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(hidden=True)
    @commands.is_owner()

    async def runtime(self,ctx):
        now = datetime.utcnow()
        elapsed = now - starttime
        seconds = elapsed.seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        embed = discord.Embed(color = self.Bot.color,timestamp=starttime ,description=f'**Abode has been running for ``{elapsed.days}`` days ``{hours}`` hours ``{minutes}`` mminutes and ``{seconds}`` seconds**')
        embed.set_author(name='Runtime', icon_url=ctx.me.avatar_url)
        embed.set_footer(text=f'Last restart')

        await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.guild_only()
    @commands.command(hidden=True)
    async def sayin(self, ctx, channel: discord.TextChannel, *, text: str):
        x = await channel.send(text)
        await ctx.message.add_reaction('<:phoCheck:786720919845994526>')


    '''@commands.command(aliases=['mc'])
    @commands.is_owner()
    async def messagecount(self, ctx):
        channel = ctx.channel
        a = 0
        msg = ctx.message
        await msg.add_reaction(':arrow_forward:')
        async for msg in channel.history(limit = None):
            a+= 1

        await msg.add_reaction(":white_check_mark: ")
        await ctx.send(f'{a} messages.')'''

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def emojilist(self, ctx):
        emojis = sorted([e for e in ctx.guild.emojis if len(e.roles) == 0 and e.available], key=lambda e: e.name.lower())
        paginator = commands.Paginator(suffix='', prefix='')
        channel = ctx.channel

        for emoji in emojis:
            paginator.add_line(f'{emoji} -- `{emoji}`')

        for page in paginator.pages:
            await channel.send(page)

        await ctx.send(ctx.tick(True))


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def image_info(self,ctx, user: discord.Member= None):
        if user is None:
            user = ctx.message.author
        img = PIL.Image.open("assets/imges/247.jpg")
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = PIL.Image.open(data)
        pfp = pfp.resize((835,911))

        img.paste(pfp,(2407,53))

        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype("assets/fonts/Modern_Sans_Light.otf", 100)
        fontbig = PIL.ImageFont.truetype("assets/fonts/litfont.ttf", 400)

        draw.text((200, 0), "Information:", (255, 255, 255), font=fontbig)
        draw.text((50, 500), "Username:  {}".format(user), (255, 255, 255), font=font)
        draw.text((50, 700), "ID:  {}".format(user.id), (255, 255, 255), font=font)
        draw.text((50, 900), "Status Type:  {}".format(user.status), (255, 255, 255), font=font)
        #draw.text((50,1100), "User Status: {}".format(user.activity.name), (255, 255, 255), font=font)
        draw.text((50, 1100), "Nickname:  {}".format(user.display_name), (255, 255, 255), font=font)
        draw.text((50, 1300), "Account created:  {}".format(user.created_at.strftime("%A %d, %B %Y.")), (255, 255, 255), font=font)
        draw.text((50, 1500), "User's Top Role: {}".format(user.top_role), (255, 255, 255), font=font)
        draw.text((50, 1700), "User Joined:  {}".format(user.joined_at.strftime("%A %d, %B %Y.")), (255, 255, 255), font=font)
        img.save('img_info.png')
        await ctx.send(file=discord.File("img_info.png"))

    @commands.Cog.listener()
    async def on_message_edit(self,before, after):
        if before.guild.id != self.Bot.guild_id:
            return
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        if before.content != after.content:
            log_channel= self.Bot.get_channel(759583119396700180)
            embed = discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
            embed.description=f"{before.author.mention} edited his/her message on {before.channel.mention}"
            embed.add_field(name="Before", value=f"``{before.clean_content}``", inline=False)
            embed.add_field(name="After", value=f"``{after.clean_content}``")
            embed.set_footer(text=f'User ID: {before.id} ')
            embed.set_author(name="Message edit!", icon_url=before.author.avatar_url)
            await log_channel.send(embed=embed)


    @commands.command()
    @commands.is_owner()
    async def playlist(self, ctx, *, playList):

        if playList == "nepali":
            await ctx.send("<https://www.youtube.com/playlist?list=PLssMJHK9DpegjOJBQGe8wjovLUb9ojlRT>")
        if playList == "spotify":
            await ctx.send("<https://open.spotify.com/playlist/3o7vSOC06Rff7NFEnheQJ4?si=4eZpAfcOT8C4s03T7svOdA>")
        if playList == "anime":
            await ctx.send("<https://www.youtube.com/playlist?list=PLssMJHK9DpeiYCHbMQucJzjQUCKRzNuSr>")

def setup (Bot):
    Bot.add_cog(owner(Bot))
    print("Owner command is working.")



