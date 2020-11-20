import discord
import traceback
from discord.ext import commands
intents = discord.Intents.default()
import asyncio
import datetime
import random
from discord import User, errors
import typing
import ast
from PIL import Image
from io import BytesIO
import re
from disputils import BotEmbedPaginator
from discord import Embed

color = 0xa100f2


class vein(commands.Cog, name= "moderation"):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 757110183800471572:
            return
        msg = message
        await msg.add_reaction("<:check:773959361953267742>")
        await msg.add_reaction("<:xmark:773959363379462184>")

    @commands.command(alaises = ['Bot'],hidden=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def abode(self,ctx):

        embed= discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.me.avatar_url}')
        embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
        embed.add_field(name="‎‎‎‏‏‎ ‎", value=f'**Abode mandator** or abode in short is a discord bot written python (discord.py).\n Abode is created by Vein, as a way to learn python but later on further continued as a fun-command based bot. Vein doesn\'t own any of the api used, so read the footers for the api source.', inline=False )
        embed.add_field(name="Tips", value= f"``.help``  is always there for you :D \n\n"
                                                  f'Want to earn a custom gif or role? You might earn them by reporting issues on more or the server on our suggestions channel. \n\n'
                                                  f'``.welcome`` whenever a new user joins. It is a easy way to make them feel welcomed :D \n\n'
                                                  f'If you can contribute to the server you may bypass some rules and get a higher role. \n\n'

                                                  f'``.faq`` FAQ are available there, do not leave your mind wander.\n\n'
                                                  f'Always check the pinned messages or the channel description to learn more about that channel.\n\n' , inline=False)


        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)




    @commands.command(aliases=['frequent_questions'],
        hidden=True)
    async def faq(self, ctx):
        embed= discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="QnA", value=f'**Why is there a logo on every command?** \n\n = Because why not? <:GWcmeisterPeepoShrug:771605304520998942> \n'
                                           f'**Can you remove the cooldown on images?** \n\n = No not anytime soon, maybe in future :)\n'
                                           f'**Why aren not the image commands not working sometimes?**\n\n = Well, sometimes the requests are not received on time, so they donot work')



        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=['purge'],hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=3):
        if amount <= 200:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'**The higher-ups have purged some messages.**', delete_after=10)
        else:
            await ctx.send("Please add a number smaller than 200")





    @commands.command(hidden=True)
    @commands.has_permissions(manage_roles=True)
    async def role(self , ctx, member: discord.Member, *,arg):
        role = discord.utils.get(ctx.guild.roles, name=f"{arg}")
        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"{member} was given role ``{arg}``.")
        else:
            await member.remove_roles(role)
            await ctx.send(f"{member} was removed from the role ``{arg}``.")

    @commands.command(hidden=True)
    @commands.has_permissions(manage_nicknames=True)
    async def cnick(self , ctx, member: discord.Member, *,arg):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send("Admin :(")
        if ctx.message.author.top_role < member.top_role:
            return await ctx.send("You  have lower roles.")
        else:
            await member.edit(nick=arg)
            await ctx.send(f'{member} nickname was changed to {arg} by {ctx.message.author}')






    @commands.command(
        name='purge_user',

        aliases=['clearuser', 'purgeuser'],
        hidden=True
    )
    async def purge_user(
        self, ctx,
        user: User,
        num_messages: typing.Optional[int] = 100,
    ):

        channel = ctx.message.channel

        def check(msg):
            return msg.author.id == user.id

        await ctx.message.delete()
        await channel.purge(limit=num_messages, check=check, before=None)
        await ctx.send (f'**The higher-ups have purged someones messsages.**', delete_after=10)





    @commands.command(hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def DM (self, ctx, *, arg ):
            await ctx.message.author.send(arg)












    @commands.command(hidden=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member is None:
            await ctx.send(f'{ctx.message.author.display_name}, Please tag an user whom you want to be kicked from the server.')
        else:
            await member.kick(reason=reason)
            await ctx.send (f'User {member.mention} was kicked from the server for {reason}.')





    @commands.command(hidden=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "You were banned from the server for not following the rules."):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
        else:
            await ctx.send("Please specify an user to ban with a reason.")


    '''
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self ,ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)
            await ctx.send(f"{member} was muted.")
        else:
            await member.add_roles(role)
            await ctx.send(f"{member} was muted.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name= "Muted")


        await member.remove_roles(role)
        await ctx.send(f"{member} was unmuted.") '''



    @commands.command()
    async def help(self, ctx):
        ch = 757136905329442859
        ch1= 757136943149613076

        if ctx.channel.id == ((ch) or (ch1) ):
            embed1= discord.Embed(title="Commands #1", description="Basic fun commands on the server", color=color)
            embed1.set_thumbnail(url=f'{ctx.guild.icon_url}')
            embed1.set_author(name="Abode",icon_url=f'{ctx.me.avatar_url}')
            embed1.add_field(name="ping", value="To check Abode's latency", inline=False)
            embed1.add_field(name="8ball", value="To ask Abode an 8ball question", inline=False)
            embed1.add_field(name="echo", value="To make Abode repeat something \n"
                                                            "``.hi`` To get a random gretting from over 50 languages.", inline=False)
            embed1.add_field(name="lenny", value="To make Abode send a lenny face", inline=False)
            embed1.add_field(name="welcome", value="To make Abode welcome a new user", inline=False)
            embed1.add_field(name="whois", value="To make Abode get the general info on the user", inline=False)
            embed1.add_field(name="serverinfo", value="To get the general info of the server", inline=False)
            embed1.add_field(name="invite", value="Get invite link of Abode of Scholars.", inline=False)
            embed1.add_field(name="complaint", value="Add an server complaint which will go into <#757110183800471572>.", inline=False)
            embed1.set_footer(text=f"Requested by {ctx.message.author.name}" )


            embed2=discord.Embed(title='Commands #2', colour=color)
            embed2.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
            embed2.add_field(name="dankmemes", value=f' Make Abode send a meme from Dankmemes subreddit', inline=False)
            embed2.set_thumbnail(url=ctx.guild.icon_url)
            embed2.add_field(name="pmemes", value= f'Make Abode send a meme from ProgrammerHumor subreddit', inline=False)
            embed2.add_field(name="cat", value=  f' Make Abode send a woof picture ', inline=False)
            embed2.add_field(name="catfact", value=  f' A random woof fact ')
            embed2.add_field(name="dog", value=   f' Make Abode send a meow picture ', inline=False)
            embed2.add_field(name="dogfact", value=  f' A random meow fact ')
            embed2.add_field(name="panda ", value= f' Make Abode send cutest pandas', inline=False)
            embed2.add_field(name="pandafact", value=  f' A random panda fact ')
            embed2.add_field(name="pikachu", value= f' Make Abode send a pikachu gif or an image', inline=False)
            embed2.add_field(name="numberfact", value= f'Make abode send a random fact on numbers')
            embed2.add_field(name="yearfact", value= f' Make Abode send a random fact on a year', inline=False)
            embed2.add_field(name="clyde", value= f' Make clyde say something', inline=False)
            embed2.add_field(name="flip", value= f'Make Abode Flip a coin for you')
            embed2.add_field(name="lovemeter", value=f'You know it :eyes:')
            embed2.add_field(name="rps", value=f'Play Rock Scissors Paper with Abode', inline=False)
            embed2.set_footer(text=f"Requested by {ctx.message.author.name} ")

            embed3= discord.Embed(title='Commands #3', color=color)
            embed3.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
            embed3.add_field(name="aquote", value="Fetch some good anime quotes.", inline=False)
            embed3.add_field(name="sad, happy, angry", value=":D", inline=False )
            embed3.add_field(name='facepalm, wink, hug, pat', value="Anime gifs on the mentioned situations.", inline=False)
            embed3.add_field(name="koala", value= "koala pictures :D")
            embed3.add_field(name="f", value="Pay your repects, I paid mine")
            embed3.add_field(name='addnote',value= f'Add a note about something',inline=False)
            embed3.add_field(name='note', value= f'To view the added note.')
            embed3.add_field(name='removenote', value=f'To remove the note that you added.', inline=False)

            embed3.set_footer(text=f"Requested by {ctx.message.author.name}")


            embed3.set_thumbnail(url=f'{ctx.guild.icon_url}')



            embeds= [embed1, embed2, embed3]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
        else:
            await ctx.send(f"{ctx.message.author.display_name}, This command only works on Bots category.")



    @commands.command(alaises=['moderationcommands'])
    @commands.has_permissions(kick_members=True)
    async def helpmod(self,ctx):
        try:
            embed= discord.Embed(title="Commands for moderators", description="The main commands of the bot", color=color)
            embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
            embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
            embed.add_field(name="DM", value="To make Abode DM you something, ``.dm Abode``", inline=False)
            embed.add_field(name="DMuser", value="To make Abode DM a specific Use, ``.dm @Vein#8177 Abode`` ", inline=False)
            embed.add_field(name="clear/purge", value="To clear messages sent ``.purge 3``, default no of message that bot clears is 3", inline=False)
            embed.add_field(name="kick ", value= "To kick a user, make sure to have a reason in the command ``Kick @Vein#8177 being too cool``", inline=False)
            embed.add_field(name="ban", value= "To ban a user, make sure to have a reason in the command ``ban @Vein#8177 being too annoying, as always``", inline=False)
            embed.add_field(name='clearuser', value= 'To clear messages of a specific user, be carefull while using this ``.clearuser @Vein38177 10``', inline=False)
            embed.add_field(name="channelstats", value= 'To show the stats/info of the channel the command is used on ``.channelstats``', inline=False)
            embed.add_field(name='cnick', value= f'To change the server nickname of the meantioned user ``.cnick @Vein#8177 Waifu``', inline=False)
            embed.add_field(name='role', value= f'To add a role to an user ``.role @Vein#8177 Civilian`` note : the spellings should not be wrong.', inline=False)
            embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=(ctx.author.avatar_url))
            embed.timestamp= datetime.datetime.utcnow()
            await ctx.message.author.send(embed=embed)
            await ctx.send(f'{ctx.message.author.display_name}, Sent you a DM.')
        except:
            await ctx.send(f'{ctx.message.author.display_name}, You have your dms closed.')
            await message.delete()

    @commands.command(hidden=True)
    @commands.has_permissions(kick_members=True)
    async def channelstats(self, ctx):
        channel = ctx.channel
        tmembers= str(len(channel.members))
        nsfw=(ctx.channel.is_nsfw())
        news=(ctx.channel.is_news())
        embed= discord.Embed( color=color)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="__Information__", value=f'**Server name: ** {ctx.guild.name} \n'
                                                               f'**Channel name :** {channel.name}\n'
                                                               f'**Channel ID : ** {channel.id} \n'
                                                               f'**Channel type : **{channel.type}\n'
                                                               f'**Channel category : ** {channel.category}\n'
                                                               f'**Topic : ** {channel.topic}\n'
                                                               f'**Channel position :** {channel.position}\n'
                                                               f'**Created at :** {channel.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")}\n'
                                                               f'**Slowmode :** {channel.slowmode_delay}\n'
                                                               f'**Channel Permissions :** {channel.permissions_synced}\n'
                                                               f'**Channel members :** {tmembers}\n'
                                                               f'**Is nsfw : ** {nsfw}\n'
                                                               f'**Is news : ** {news}', inline=False)

        embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
        embed.set_footer(text= f" Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        embed.timestamp= datetime.datetime.utcnow()
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def complaint(self, ctx, *,arg):
        if ctx.channel.id != (757136905329442859 or 757136943149613076):
            await ctx.send(f'{ctx.author.name}, It\'s good that you have complaints but please use this command on the Bots category.' )
            return
        channel = ctx.guild.get_channel(757110183800471572)
        embed= discord.Embed(color=ctx.author.color, title= f'{arg}', timestamp= datetime.datetime.utcnow())
        embed.set_author(name=f"{ctx.author.name}'s complaint ", icon_url=f'{ctx.author.avatar_url}')
        embed.set_footer(text=f"Submitted on")
        await ctx.message.delete()
        await channel.send(embed=embed)
        await ctx.send(f'{ctx.author.name}, Sent your complaint in <#757110183800471572>.')








def setup (client):
     client.add_cog (vein(client))
     print("Mod cog is working.")


