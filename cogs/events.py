import discord
from discord.ext import commands
import random
from datetime import datetime
from discord.utils import get
import re
import asyncio


class events(commands.Cog, name='Events'):
    def __init__(self, Bot):
        self.Bot = Bot


    @commands.Cog.listener()
    async def on_raw_message_delete(self,payLoad):
        m = payLoad.cached_message
        if m.guild.id != self.Bot.guild_id:
            return
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
        if m.channel.id == 783714539832868874:
            return
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        if not m.author.bot and not m.channel.is_nsfw():

            color = random.choice(self.Bot.color_list)
            embed= discord.Embed(color=color, timestamp=datetime.utcnow())
            embed.description=f"Message sent by {m.author.mention} and deleted in {m.channel.mention}"
            if not m.attachments:
                if len(m.clean_content) < 1023:

                    embed.add_field(name="Message Content", value=f"``{m.clean_content}``")
                if len(m.clean_content) > 1023:
                    hm = m.clean_content[:1023]
                    embed.add_field(name="Message Content", value=f"``{hm}``", inline=False)
            embed.set_author(name="Message delete",icon_url=m.author.avatar_url)
            embed.set_footer(text=f'ID: {m.id}')
            x = await self.Bot.log_channel.send(embed=embed)
            if m.clean_content.startswith("https://cdn.discordapp.com/attachments"):
                em = discord.Embed(color=color)
                em.description=f"[Image]({m.clean_content})"
                em.set_image(url=f"{m.clean_content}")
                await self.Bot.log_channel.send(embed=em)







    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        if member.guild.id != self.Bot.guild_id:
            return

        welcome = [f'As the prevailing wind blows east to west, **{member.name}** joins the scholars.',
                   f'**{member.name}** joined the Scholars.'


        ]
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
        embed= discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
        embed.description= random.choice(welcome)
        embed.set_author(name=f"{member.name}",   icon_url=member.avatar_url)
        embed.set_footer(text=f'#{member.guild.member_count} member')
        self.Bot.scholar_chat= self.Bot.get_channel(757108786497585172)
        await self.Bot.scholar_chat.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id != self.Bot.guild_id:
            return

        if self.Bot.DEFAULT_PREFIX == '&':
            return
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
        embed= discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())

        embed.description=(f"** {member.mention} has left the Scholars** <:FeelsSadMan:757112294856589312>")
        embed.set_author(name=f"Member left",   icon_url=member.avatar_url)
        embed.set_footer(text=f'#{member.guild.member_count} member | ID :  {member.id}')
        self.Bot.leave = self.Bot.get_channel(760312430382809128)
        await self.Bot.leave.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        if channel.guild.id != self.Bot.guild_id:
            return

        if self.Bot.DEFAULT_PREFIX == '&':
            return
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
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
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
        embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow(), description=f"**Channel name: ** {channel.name}")
        embed.set_author(name=f"Channel delete!", icon_url=channel.guild.icon_url)
        embed.set_footer(text=f'ID: {channel.id}')
        await self.Bot.log_channel.send(embed=embed)











    @commands.Cog.listener()
    async def on_member_unban(self, user):
        if user.guild.id != self.Bot.guild_id:
            return
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        embed = discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
        embed.description=f"{user.mention} was unbanned by an elder."
        embed.set_author(name=f"Unban!", icon_url=user.avatar_url)
        embed.set_footer(text=f"{user.id}")
        await self.Bot.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self,before,after):
        if before.guild.id != self.Bot.guild_id:
            return
        self.Bot.log_channel= self.Bot.get_channel(759583119396700180)
        #if self.Bot.DEFAULT_PREFIX == '&':
            #return
        if before.nick != after.nick:

            embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
            embed.description=f"**Previous nickname**  \n{before.nick} \n\n**Current nickname** \n {after.nick}"
            embed.set_author(name=f"Nickname change of {before}", icon_url=before.avatar_url)
            embed.set_footer(text=f"ID: {before.id}")
            await self.Bot.log_channel.send(embed=embed)

        if len(before.roles) < len(after.roles):
            new_role = next(role for role in after.roles if role not in before.roles)
            embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
            embed.set_author(name=f"Role given!", icon_url=before.avatar_url)
            embed.description=f"**{before.mention} was given the {new_role.mention} role.**"
            embed.set_footer(text=f"Role ID {new_role.id} || User ID {before.id}")
            await self.Bot.log_channel.send(embed=embed)

        if len(before.roles) > len(after.roles):
            new_role = next(role for role in before.roles if role not in after.roles)
            embed= discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
            embed.set_author(name=f"Role removed!", icon_url=before.avatar_url)
            embed.description=f"**{before.mention} was removed from the role {new_role.mention} **"
            embed.set_footer(text=f"Role ID {new_role.id} || User ID {before.id}")
            await self.Bot.log_channel.send(embed=embed)




def setup (Bot):
    Bot.add_cog (events(Bot))
    print("Event cog is working.")
