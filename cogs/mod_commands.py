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
from disputils import BotMultipleChoice

color = 0xa100f2
guild = 757098499836739594


class vein(commands.Cog, name= "moderation"):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.guild.id != (guild):
            return

        user = ctx.guild.get_member(ctx.author.id)

        me = ctx.guild.get_member(427436602403323905)
        role = ctx.guild.get_role(782624701779673129)
        if ctx.author.id == 427436602403323905:
            return
        if role in user.roles:

            channel = ctx.guild.get_channel(780785741101137926)
            embed= discord.Embed(color = color,timestamp= datetime.datetime.utcnow())
            embed.set_author(name=f"{ctx.author.name}",  icon_url=ctx.author.avatar_url)
            embed.add_field(name="Action", value=f'{ctx.message.clean_content}')
            embed.set_footer(text=f'ID : {ctx.message.id}')

            await channel.send(embed=embed)
        else:
            return






    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 757110183800471572:
            return
        msg = message
        await msg.add_reaction("<:check:773959361953267742>")
        await msg.add_reaction("<:xmark:773959363379462184>")

    @commands.command(aliases = ['Bot'],hidden=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def abode(self,ctx):

        embed= discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.me.avatar_url}')
        embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
        embed.add_field(name="‎‎‎‏‏‎Intro", value=f'**Abode mandator** or abode in short is a discord bot written python (discord.py).\n Abode is created by Vein, as a way to learn python but later on further continued as a fun-command based bot. Vein doesn\'t own any of the api used, so read the footers for the api source.', inline=False )
        embed.add_field(name="Tips", value= f"``.help``  is always there for you :D \n\n"
                                                  f'Want to earn a custom gif or role? You might earn them by reporting issues on more or the server on our suggestions channel. \n\n'
                                                  f'``.welcome`` whenever a new user joins. It is a easy way to make them feel welcomed :D \n\n'
                                                  f'If you can contribute to the server you may bypass some rules and get a higher role. \n\n'

                                                  f'``.faq`` FAQ are available there, do not leave your mind wander.\n\n'
                                                  f'Always check the pinned messages or the channel description to learn more about that channel.\n\n'
                                                  f'By default you don\'t have a cultivator name add it using ``.aliases <your name>.``', inline=False)


        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)




    @commands.command(aliases=['frequent_questions'],
        hidden=True)
    @commands.guild_only()
    async def faq(self, ctx):
        embed= discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="QnA", value=f'**Why is there a logo on every command?** \nBecause why not? <:Scholar2:779239176511946772>\n\n'
                                           f'**Can you remove the cooldown on images?** \nNo not anytime soon, maybe in future <:blobspearpeek:775344866246393876>\n\n'
                                           f'**Why aren not the image commands not working sometimes?**\nIt\'s due to bad response from the API.' )



        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=['purge'],hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=3):
        channel = ctx.guild.get_channel(780785741101137926)
        if amount <= 200:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'**The higher-ups have purged some messages.**', delete_after=10)
            embed = discord.Embed(title= f'Purge' , color =color, description=f'{ctx.author.mention} cleared {amount} messages from {ctx.channel.mention}')
            await channel.send(embed=embed)
        else:
            await ctx.send("Please add a number smaller than 200")



    @commands.command(aliases=['clearuser'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self, ctx, user: User,
        num_messages: typing.Optional[int] = 100,
    ):

        channel = ctx.message.channel

        def check(msg):
            return msg.author.id == user.id

        await ctx.message.delete()
        await channel.purge(limit=num_messages, check=check, before=None)
        await ctx.send (f'**The higher-ups have purged someones messsages.**', delete_after=10)

    @commands.command(hidden=True)
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def role(self , ctx, member: discord.Member, *,arg):
        role = discord.utils.get(ctx.guild.roles, name=f"{arg}")
        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"{member} was given role ``{arg}``.")
        else:
            await member.remove_roles(role)
            await ctx.send(f"{member} was removed from the role ``{arg}``.")

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def cnick(self , ctx, member: discord.Member, *,arg):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send("Admin :(")
        if ctx.message.author.top_role < member.top_role:
            return await ctx.send("You  have lower roles.")
        else:
            await member.edit(nick=arg)
            await ctx.send(f'{member} nickname was changed to {arg} by {ctx.message.author}')












    @commands.command(hidden=True, aliases =['PM'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def DM (self, ctx, *, arg ):
            await ctx.message.author.send(arg)












    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member is None:
            await ctx.send(f'{ctx.message.author.display_name}, Please tag an user whom you want to be kicked from the server.')
        else:
            await member.kick(reason=reason)
            await ctx.send (f'User {member.mention} was kicked from the server for {reason}.')





    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "You were banned from the server for not following the rules."):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
            await ctx.send(f'{member.mention} was banned from the server.')
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





    @commands.command(hidden=True, aliases=['cstats'])
    @commands.guild_only()
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
    @commands.guild_only()
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



    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('Weird you want to make a poll with less than 1 option?')
            return
        if len(options) > 7:
            await ctx.send('Bruh! you can\'t make a poll with more than 7 options.')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['<:check:773959361953267742>', ' <:xmark:773959363379462184>']
        else:
            reactions = ['1️⃣' , '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣']

        description = []
        for x, option in enumerate(options):
            description += f'\n\n {reactions[x]} {option}'
        embed = discord.Embed(title=question, description=''.join(description), color=color, timestamp= datetime.datetime.utcnow())
        embed.set_footer(text=f'Elder responsible for the poll : {ctx.message.author.name}')
        msg = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await msg.add_reaction(reaction)

        await ctx.edit_message(react_message, embed=embed)



    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def slowmode(self, ctx , time):
        channel = ctx.guild.get_channel(780785741101137926)
        if time == 'remove':
            await ctx.channel.edit(slowmode_delay = 0)
            await ctx.send(f'Slowmode removed.')
            embed = discord.Embed(title = f'Slowmode', color=color , description =f'{ctx.author.mention} removed slowmode from {ctx.channel.mention}')
            await channel.send(embed=embed)

        else:
            try:
                await ctx.channel.edit(slowmode_delay= time)
                await ctx.send(f'{time}s of slowmode was set on the current channel.')
                embed = discord.Embed(title = f'Slowmode', color=color , description =f'{ctx.author.mention} added slowmode of {time}s to {ctx.channel.mention}')
                await channel.send(embed=embed)
            except:
                await ctx.send(f'{ctx.author.mention}The slowmode time should be a number(s).')






def setup (client):
    client.add_cog(vein(client))
    print("Mod cog is working.")


