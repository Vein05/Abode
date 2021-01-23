import asyncio

import discord
from discord.ext.commands import Paginator as CommandPaginator
from discord.ext import commands
from utils import emote

class CannotPaginate(Exception):
    pass

class Pages:
    def __init__(self, ctx, *, entries, per_page=12, show_entry_count=True, embed_color = discord.Color.blurple(), title=None, thumbnail=None, footericon=None, footertext=None, author=None, delete_after=None):
        self.bot = ctx.bot
        self.entries = entries
        self.message = ctx.message
        self.channel = ctx.channel
        self.author = author if author else ctx.author
        self.thumbnail = thumbnail
        self.footericon = footericon
        self.footertext = footertext
        self.title = title
        self.delete_after = delete_after
        self.per_page = per_page
        pages, left_over = divmod(len(self.entries), self.per_page)
        if left_over:
            pages += 1
        self.maximum_pages = pages
        self.embed = discord.Embed(colour=embed_color)
        self.paginating = True
        self.show_entry_count = show_entry_count
        self.reaction_emojis = [

            ('\U000023ee\U0000fe0f', self.first_page),
            ('\N{BLACK LEFT-POINTING TRIANGLE}', self.previous_page),
            ('\U000023f9', self.stop_pages),
            ('\N{BLACK RIGHT-POINTING TRIANGLE}', self.next_page),
            ('\U000023ed\U0000fe0f', self.last_page)
            # (f'{emote.first}', self.first_page),
            # (f'{emote.previous}', self.previous_page),
            # (f'{emote.stop}', self.stop_pages),
            # (f'{emote.next}', self.next_page),
            # (f'{emote.last}', self.last_page)
            #('<:python:682881809649762358>', self.show_help)
        ]

        if ctx.guild is not None:
            self.permissions = self.channel.permissions_for(ctx.guild.me)
        else:
            self.permissions = self.channel.permissions_for(ctx.bot.user)

        if not self.permissions.embed_links:
            raise commands.BotMissingPermissions('I do not have permissions to embed links.')

        if not self.permissions.send_messages:
            raise commands.BotMissingPermissions('Bot cannot send messages.')

        if self.paginating:
            # verify we can actually use the pagination session
            if not self.permissions.add_reactions:
                raise commands.BotMissingPermissions('I do not have permissions to add reactions.')

            if not self.permissions.read_message_history:
                raise commands.BotMissingPermissions('I do not have permissions to Read Message History.')

    def get_page(self, page):
        base = (page - 1) * self.per_page
        return self.entries[base:base + self.per_page]

    def get_content(self, entries, page, *, first=False):
        return None

    def get_embed(self, entries, page, *, first=False):
        self.prepare_embed(entries, page, first=first)
        return self.embed

    def prepare_embed(self, entries, page, *, first=False):
        p = []
        for index, entry in enumerate(entries, 1 + ((page - 1) * self.per_page)):
            p.append(f'{entry}')

        if self.maximum_pages > 1:
            if self.show_entry_count:
                text = f'Showing page {page}/{self.maximum_pages} ({len(self.entries)} entries)'
            else:
                text = f'Showing page {page}/{self.maximum_pages}'

            self.embed.set_footer(text=text)

        if self.paginating and first:
            p.append('')

        self.embed.description = ''.join(p)
        self.embed.title = self.title or discord.Embed.Empty
        if self.thumbnail:
            self.embed.set_thumbnail(url=self.thumbnail)
        # if self.author:
        #     self.embed.set_author(icon_url=self.author.avatar_url, name=str(self.author))

    async def show_page(self, page, *, first=False):
        self.current_page = page
        entries = self.get_page(page)
        content = self.get_content(entries, page, first=first)
        embed = self.get_embed(entries, page, first=first)

        if not first:
            await self.message.edit(content=content, embed=embed)
            return

        self.message = await self.channel.send(content=content, embed=embed)
        for (reaction, _) in self.reaction_emojis:
            if self.maximum_pages == 2 and reaction in ('\U000023ee\U0000fe0f', '\U000023ed\U0000fe0f'):
                # no |<< or >>| buttons if we only have two pages
                # we can't forbid it if someone ends up using it but remove
                # it from the default set
                continue
            if self.maximum_pages == 1 and reaction in ('\U000023ee\U0000fe0f', '\U000023ed\U0000fe0f', '\N{BLACK RIGHT-POINTING TRIANGLE}', '\N{BLACK LEFT-POINTING TRIANGLE}'):
                continue

            await self.message.add_reaction(reaction)

    async def checked_show_page(self, page):
        if page != 0 and page <= self.maximum_pages:
            await self.show_page(page)

    async def first_page(self):
        """goes to the first page"""
        await self.show_page(1)

    async def last_page(self):
        """goes to the last page"""
        await self.show_page(self.maximum_pages)

    async def next_page(self):
        """goes to the next page"""
        await self.checked_show_page(self.current_page + 1)

    async def previous_page(self):
        """goes to the previous page"""
        await self.checked_show_page(self.current_page - 1)

    async def show_current_page(self):
        if self.paginating:
            await self.show_page(self.current_page)

    async def numbered_page(self):
        """lets you type a page number to go to"""
        to_delete = []
        to_delete.append(await self.channel.send('What page do you want to go to?'))

        def message_check(m):
            return m.author == self.author and \
                   self.channel == m.channel and \
                   m.content.isdigit()

        try:
            msg = await self.bot.wait_for('message', check=message_check, timeout=30.0)
        except asyncio.TimeoutError:
            to_delete.append(await self.channel.send('Took too long.'))
            await asyncio.sleep(5)
        else:
            page = int(msg.content)
            to_delete.append(msg)
            if page != 0 and page <= self.maximum_pages:
                await self.show_page(page)
            else:
                to_delete.append(await self.channel.send(f'Invalid page given. ({page}/{self.maximum_pages})'))
                await asyncio.sleep(5)

        try:
            await self.channel.delete_messages(to_delete)
        except Exception:
            pass

    async def show_help(self):
        """shows this message"""
        messages = ['Welcome to the interactive paginator!\n']
        messages.append('This interactively allows you to see pages of text by navigating with ' \
                        'reactions. They are as follows:\n')


        embed = self.embed.copy()
        embed.clear_fields()
        embed.description = '\n'.join(messages)
        embed.set_footer(text=f'We were on page before this message.')
        await self.message.edit(content=None, embed=embed)

        async def go_back_to_current_page():
            await asyncio.sleep(60.0)
            await self.show_current_page()

        self.bot.loop.create_task(go_back_to_current_page())

    async def stop_pages(self):
        """stops the interactive pagination session"""
        await self.message.delete()
        self.paginating = False

    def react_check(self, reaction, user):
        if user is None or user.id != self.author.id:
            return False

        if reaction.message.id != self.message.id:
            return False

        for (emoji, func) in self.reaction_emojis:
            if reaction.emoji == emoji:
                self.match = func
                return True
        return False

    async def paginate(self):
        """Actually paginate the entries and run the interactive loop if necessary."""
        first_page = self.show_page(1, first=True)
        # allow us to react to reactions right away if we're paginating
        self.bot.loop.create_task(first_page)

        while self.paginating:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=self.react_check, timeout=self.delete_after)
            except asyncio.TimeoutError:
                self.paginating = False
                try:
                    await self.message.delete()
                except:
                    pass
                finally:
                    break
            try:
                await self.message.remove_reaction(reaction, user)
            except:
                pass # can't remove it so don't bother doing so

            await self.match()

class FieldPages(Pages):
    """Similar to Pages except entries should be a list of
    tuples having (key, value) to show as embed fields instead.
    """
    def __init__(self, ctx, *, entries, per_page=12, show_entry_count=True, title, thumbnail, footericon, footertext, embed_color = discord.Color.blurple()):
        super().__init__(ctx, entries=entries, per_page=per_page, show_entry_count=show_entry_count, title=title, thumbnail=thumbnail, footericon=footericon, footertext=footertext, embed_color=embed_color)

    def prepare_embed(self, entries, page, *, first=False):
        self.embed.clear_fields()

        for key, value in entries:
            self.embed.add_field(name=key, value=value, inline=False)
        
        self.embed.title = self.title

        if self.maximum_pages > 1:
            if self.show_entry_count:
                text = f' ({page}/{self.maximum_pages})'
            else:
                text = f' ({page}/{self.maximum_pages})'
            self.embed.title = self.title + text

        self.embed.set_footer(icon_url = self.footericon, text=self.footertext)
        self.embed.set_thumbnail(url=self.thumbnail)

class TextPages(Pages):
    """Uses a commands.Paginator internally to paginate some text."""

    def __init__(self, ctx, text, *, prefix='```ml', suffix='```', max_size=2000):
        paginator = CommandPaginator(prefix=prefix, suffix=suffix, max_size=max_size - 200)
        for line in text.split('\n'):
            paginator.add_line(line)

        super().__init__(ctx, entries=paginator.pages, per_page=1, show_entry_count=False)

    def get_page(self, page):
        return self.entries[page - 1]

    def get_embed(self, entries, page, *, first=False):
        return None

    def get_content(self, entry, page, *, first=False):
        if self.maximum_pages > 1:
            return f'{entry}\nPage {page}/{self.maximum_pages}'
        return entry