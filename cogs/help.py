import discord
from discord.ext import commands
from disputils import BotEmbedPaginator
from cogs.utils import Pag

color = 0xa100f2
nomasti = 'https://pbs.twimg.com/media/EUqVvbQUcAAtL1H.jpg'
ban = 'https://cdn.discordapp.com/attachments/759796216044978239/781453844269367306/ban.gif'
slowmode = "https://cdn.discordapp.com/attachments/782161513825042462/793127261653565450/slowmode.gif"
role = 'https://cdn.discordapp.com/attachments/782161513825042462/793127248495771658/role.gif'
nickname = 'https://cdn.discordapp.com/attachments/782161513825042462/793127274249060362/nick.gif'
poll = 'https://cdn.discordapp.com/attachments/782161513825042462/793127274181427220/ban_and_unban.gif'


class vein9(commands.Cog, name='Help'):
    def __init__(self, Bot):
        self.Bot = Bot
        self.cmds_per_page = 10

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx, *, entity=None):
        if ctx.channel.id == 757108786497585172:
            return

        if not entity:
            embed1 = discord.Embed(color=color,
                                   title=f'[``{self.Bot.DEFAULT_PREFIX}help <command name>``] for more info on commands.')
            embed1.set_thumbnail(url=f'{ctx.me.avatar_url}')

            embed1.add_field(
                name="Main commands", value=f'``helppoints`` ``stats`` ``complaint`` ``suggestions`` ``faq`` ``abode`` ``welcome``',  inline=False)
            embed1.add_field(
                name="Handy commands", value=f'``ping`` ``invite`` ``lenny`` ``f`` ``hi`` ``flip`` ``calc``',  inline=False)
            embed1.add_field(
                name="Fun commands", value=f'``8ball`` ``lovemeter`` ``rps`` ``sad/happy/angry`` ``aquote``',  inline=False)
            embed1.add_field(
                name="Image commands", value=f'``cat`` ``dog`` ``panda`` ``koala`` ``pikachu`` ``dankmemes`` ``pmemes`` ``clyde`` ``facepalm`` ``wink`` ``headpat`` ``hug``', inline=False)
            embed1.add_field(
                name="Nerd commands", value=f'``userinfo`` ``serverinfo`` ``statsu``',  inline=False)
            embed1.add_field(
                name="Fact commands", value=f'``dogfact`` ``catfact`` ``pandafact`` ``numberfact`` ``yearfact`` ',   inline=False)
            embed1.add_field(
                name="Note commands", value=f'``addnote`` ``note`` ``removenote``',  inline=False)

            embeds = [embed1]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
        else:
            command = self.Bot.get_command(entity)
            if command:
                await self.setup_help_pag(ctx, command, command.name)

            else:
                await ctx.send(f"{entity} not found.")

    async def return_filtered_commands(self, walkable, ctx):
        filtered = []
        for c in walkable.walk_commands():
            try:
                if c.hidden:
                    continue
                elif c.parent:
                    continue
                await c.can_run(ctx)
                filtered.append(c)
            except commands.CommandError:
                continue
        return self.return_sorted_commands(filtered)

    def return_sorted_commands(self, commandList):
        return sorted(commandList, key=lambda x: x.name)

    def get_command_signature(self, command: commands.Command, ctx: commands.Context):
        aliases = "| ".join(command.aliases)
        cmd_invoke = f'[{command.name} | {command.aliases}]' if command.aliases else command.name
        full_invoke = command.qualified_name.replace(command.name, "")
        signature = f'{self.Bot.DEFAULT_PREFIX}{full_invoke}{cmd_invoke} {command.signature}'
        return signature

    async def setup_help_pag(self, ctx, entity=None, title=None):
        entity = entity or self.Bot
        title = title or self.Bot.description

        pages = []

        if isinstance(entity, commands.Command):
            filtered_commands = (
                list(set(entity.all_commands.values()))
                if hasattr(entity, "all_commands")
                else []
            )
            filtered_commands.insert(0, entity)
        else:
            filtered_commands = await self.return_filtered_commands(entity, ctx)

        for i in range(0, len(filtered_commands), self.cmds_per_page):
            next_commands = filtered_commands[i: i + self.cmds_per_page]
            commands_entry = ""

            for cmd in next_commands:
                desc = cmd.short_doc or cmd.description
                signature = self.get_command_signature(cmd, ctx)
                subcommands = "Has subcommands " if hasattr(
                    cmd, "all_commands") else ""
                commands_entry += (
                    f" ```{signature}\n```\n**Description:** {desc}\n"
                    if isinstance(entity, commands.Command)
                    else f"**{cmd.name}**\n{desc}\n    {subcommands}\n"
                )
            pages.append(commands_entry)
        await Pag(title=title, color=color, entries=pages, length=1).start(ctx)

    @commands.command()
    async def help_default(self, ctx, *, entity=None):
        if not entity:
            await self.setup_help_pag(ctx)
        else:
            cog = self.Bot.get_cog(entity)
            if cog:
                await self.setup_help_pag(ctx, cog, f"{cog.qualified_name}'s commands")

            else:
                command = self.Bot.get_command(entity)
                if command:
                    await self.setup_help_pag(ctx, command, command.name)

                else:
                    await ctx.send(f"{entity} not found.")

    @commands.command(alaises=['moderationcommands'])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def helpmod(self, ctx):

        embed1 = discord.Embed(color=color)
        embed1.set_author(name="Mod Commands", icon_url=f'{ctx.me.avatar_url}')
        embed1.add_field(name="Clear", value="**Aliases** : Purge\n"
                         "**Limit** : 200 \n"
                         "**Default value** : 3 \n"
                         "**Permission** : Manage messages \n"
                         "**Roles** : Elder or higher\n"
                         "**Usage**\n ```.clear 10```\n\n"
                         )
        embed1.add_field(name="Clearuser", value="**Aliases** : Purgeuser, Clearuser\n"

                         "**Permission** : Manage messages\n"
                         "**Roles** : Elder or higher\n"
                         "**Usage**\n ```.clearuser @Vein#8177 10```\n\n")
        embed1.add_field(name="‎‎‎‏‏‎ ", value='‎‎‎‏‏‎ ')
        embed1.add_field(name="DM", value=f"**Aliases** : PM\n"

                         "**Permission** : Manage messages\n"
                         "**Roles** : Elder or higher\n"
                         "**Usage**\n ```.dm Idek why this is a command.```\n\n")
        embed1.add_field(name="Dmuser", value=f"**Aliases** : Pmuser\n"

                         "**Permission** : Manage messages\n"
                         "**Roles** : Elder or higher\n"
                         "**Usage**\n ```.dmuser @Vein#8177 why is this a command?```\n\n")
        embed1.set_footer(
            text=f"Tip : All the command names are case insensitive.")

        embed2 = discord.Embed(color=color)
        embed2.add_field(name="Kick", value=f"**Aliases** : None\n"

                         "**Permission** : Kick users\n"
                         "**Roles** : Outer elder or higher\n"
                         "**Usage**\n ```.kick <user> <Reason>```\n")
        embed2.add_field(name="Ban", value=f"**Aliases** : None\n"

                         "**Permission** : Ban users\n"
                         "**Roles** : Inner elder or higher\n"
                         "**Usage**\n ```.ban <user> <Reason>```\n")
        embed2.add_field(name="Unban", value=f"**Aliases** : None\n"

                         "**Permission** : Administrator\n"
                         "**Roles** : Admin\n"
                         "**Usage**\n ```.unban Vein#6003```\n"
                         "**Example :** \n\n", inline=False)
        embed2.set_image(url=f'{ban}')
        embed2.set_footer(
            text=f"Tip : If you are a new elder feel free to bug your seniors. ")
        embed3 = discord.Embed(color=color)

        embed3.add_field(name="cnick", value=f"**Aliases** : None\n"

                         "**Permission** : Change nickname\n"
                         "**Roles** : Outer elder or higher\n"
                         "**Usage**\n ```.cnick @Vein#8177 Waifu ```\n"
                         "**Example :** \n\n", inline=False)
        embed3.set_image(url=f'{nickname}')

        embed3.set_footer(
            text=f"Tip : Altough the commands are insensitive the role names aren't be carefull.")
        embed4 = discord.Embed(color=color)
        embed4.add_field(name='role', value=f"**Aliases** : None\n"
                                            f'**What for** : To add or remvoe roles to the mentioned user.\n'
                         "**Permission** : Manage roles\n"
                         "**Roles** : Inner elder or higher\n"
                         "**Usage**\n ```.role @Vein#8177 Head Insturctor ```\n"
                         "**Example :** \n\n", inline=False)
        embed4.set_image(url=f'{role}')
        embed4.set_footer(
            text='Tip : Is used on the user who already has the role the bot will remove the role.')
        embed5 = discord.Embed(color=color)
        embed5.add_field(name='Channelstats', value=f"**Aliases** : cstats\n"


                         "**Roles** : Outer elder or higher\n"
                         "**Usage**\n ```.Channelstats ```\n", inline=False)
        embed5.add_field(name='Slowmode', value=f"**Aliases** : smode\n"
                         "**Permission** : Manage channel"

                                                "**Roles** : Inner or higher\n"
                                                "**Usage**\n ```.Slowmode 10 ```\n\n"
                                                "**Example **:")
        embed5.set_footer(
            text='Tip : Only read mods use Channelstats. \nTip2 : ".Slowmode remove" will remove the slowmode. ')
        embed5.set_image(url=f'{slowmode}')
        embed6 = discord.Embed(color=color)
        embed6.add_field(name='Poll', value=f"**Aliases** : None\n"
                         "**Limit** : 7\n"
                         "**Atleast** : 2\n"
                         "**Roles** : Outer elder or higher\n"
                         '**Usage**\n ```.poll "Poll title here" "Option1" "Option2" ```\n'
                         "**Example :** \n\n", inline=False)
        embed6.set_footer(
            text=f'Tip : If your options are "yes" and "no", Abode will react with a tick and a cross.')
        embed6.set_image(url=f'{poll}')
        embed7 = discord.Embed(color=color)
        embed7.add_field(
            name='Lock / Unlock', value=f'**Aliases : **None\n**For :** Verified role\n**Roles :** Supreme elder or higher. \n**Usuage :** ```.lock / .unlock```', inline=False)
        embed7.add_field(name='Roleinfo', value=f"**Aliases : **  rinfo\n"

                                                "**Roles :**  Inner elder or higher\n"
                                                '**Usage**\n ```.roleinfo Verified ```\n',)
        embed7.set_footer(
            text=f'You earn a custom role for being an elder, don\'t forget to ask one for yourself.')

        embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]
        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

    @commands.command(aliases=['helpstats', 'helpp'])
    @commands.guild_only()
    async def helppoints(self, ctx):
        ch = 781535649843904562

        if ctx.channel.id != (ch):

            msg = ctx.message
            return await msg.add_reaction('<:xmark:773959363379462184>')
        embed1 = discord.Embed(color=color)
        embed1.add_field(name="Stats / Statsu", value='To see your points, stats info.\n'
                         'To check someone\'s stats, ``.stats <userid>``', inline=False)
        embed1.add_field(
            name="addcommand", value='To add your own custom command.You need ``500`` points to buy a command and you can\'t overrite an existing command.', inline=False)
        embed1.add_field(
            name="aliases", value='To add an aliases to your name')
        embeds = [embed1]
        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


def setup(Bot):
    Bot.add_cog(vein9(Bot))
    print("Help cog is working.")
