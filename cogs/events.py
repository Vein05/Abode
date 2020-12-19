import discord
from discord.ext import commands
import random
from datetime import datetime
from discord.utils import get


class events(commands.Cog, name='Events'):
    def __init__(self, Bot):
        self.Bot = Bot




    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id != self.Bot.guild_id:
            return
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        welcome = [f'As the prevailing wind blows east to west, **{member.name}** joins the scholars.',
                   f'**{member.name}** joined the Scholars.'


        ]
        embed= discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
        embed.description= random.choice(welcome)
        embed.set_author(name=f"{member.name}",   icon_url=member.avatar_url)
        embed.set_footer(text=f'#{member.guild.member_count} member')
        await self.Bot.scholar_chat.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id != self.Bot.guild_id:
            return

        if self.Bot.DEFAULT_PREFIX == '&':
            return

        embed= discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())

        embed.description=(f"** {member.mention} has left the Scholars** <:FeelsSadMan:757112294856589312>")
        embed.set_author(name=f"Member left",   icon_url=member.avatar_url)
        embed.set_footer(text=f'#{member.guild.member_count} member | ID :  {member.id}')
        await self.Bot.leave.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        if channel.guild.id != self.Bot.guild_id:
            return

        if self.Bot.DEFAULT_PREFIX == '&':
            return
        embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow(), description=f'**Channel {channel.mention}**')
        embed.set_author(name=f"Channel create!", icon_url=channel.guild.icon_url)
        #embed.add_field(name="Created by", value=f"{member.mention}")
        embed.set_footer(text=f'ID: {channel.id}')
        await self.Bot.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if channel.guild.id != self.Bot.guild_id:
            return

        if self.Bot.DEFAULT_PREFIX == '&':
            return
        embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow(), description=f"**Channel name: ** {channel.name}")
        embed.set_author(name=f"Channel delete!", icon_url=channel.guild.icon_url)
        embed.set_footer(text=f'ID: {channel.id}')
        await self.Bot.log_channel.send(embed=embed)


    '''@commands.Cog.listener()
    async def on_member_update(self, before, after):'''

    @commands.Cog.listener()
    async def on_message_edit(self,something, message):

        if message.guild.id != self.Bot.guild_id:
            return
        if self.Bot.DEFAULT_PREFIX == '&':
            return

        if not message.author.bot and not message.channel.is_nsfw():

            embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
            embed.description=f"Message sent by {something.author.mention} and edited in {something.channel.mention}"
            if len(something.clean_content) < 1023:

                embed.add_field(name="Before", value=f" ``{something.clean_content}``", inline=False)
                embed.add_field(name="After", value=f"``{message.clean_content}``")

            if len(something.clean_content) > 1023:
                hm = something.clean_content[:1023]
                hm1=message.clean_content[:1023]
                embed.add_field(name="Before", value=f"``{hm}``", inline=False)
                embed.add_field(name="After", value=f"``{hm1}``", inline=False)
            embed.set_author(name="Message edit",icon_url=message.author.avatar_url)
            await self.Bot.log_channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_delete(self,m):
        if m.guild.id != self.Bot.guild_id:
            return
        if m.channel.id == 783714539832868874:
            return
        if not m.author.bot and not m.channel.is_nsfw():

            embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
            embed.description=f"Message sent by {m.author.mention} and deleted in {m.channel.mention}"
            if len(m.clean_content) < 1023:

                embed.add_field(name="Message Content", value=f"``{m.clean_content}``")
            if len(m.clean_content) > 1023:
                hm = m.clean_content[:1023]
                embed.add_field(name="Message Content", value=f"``{hm}``", inline=False)
            embed.set_author(name="Message delete",icon_url=m.author.avatar_url)
            embed.set_footer(text=f'ID: {m.id}')
            await self.Bot.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, user):
        if user.guild.id != self.Bot.guild_id:
            return
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        embed = discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
        embed.description=f"{user.mention} was unbanned by an elder."
        embed.set_author(name=f"Unban!", icon_url=user.avatar_url)
        embed.set_footer(text=f"{user.id}")
        await self.Bot.log_channel.send(embed=embed)


def setup (Bot):
    Bot.add_cog (events(Bot))
    print("Event cog is working.")
