import discord
from discord.ext import commands
from disputils import BotEmbedPaginator,BotMultipleChoice

color = 0xa100f2
nomasti = 'https://pbs.twimg.com/media/EUqVvbQUcAAtL1H.jpg'
ban = 'https://cdn.discordapp.com/attachments/759796216044978239/781453844269367306/ban.gif'
slowmode = 'https://cdn.discordapp.com/attachments/759796216044978239/781453902582513674/Slowmode.gif'
role = 'https://cdn.discordapp.com/attachments/759796216044978239/781453873469980672/Role.gif'
nickname = 'https://cdn.discordapp.com/attachments/759796216044978239/781453847854972928/Nickname.gif'
poll = 'https://cdn.discordapp.com/attachments/759796216044978239/781453866029154304/poll.gif'

class vein9(commands.Cog, name='Help'):
        def __init__(self, Bot):
            self.Bot = Bot

        @commands.command()
        @commands.guild_only()
        async def help(self, ctx):
                ch = 781535649843904562
                ch1= 757136943149613076

                if ctx.channel.id == ((ch)):
                    embed1= discord.Embed(title="Commands #1", description="Basic fun commands on the server", color=color)
                    embed1.set_thumbnail(url=f'{ctx.guild.icon_url}')
                    embed1.set_author(name="Abode",icon_url=f'{ctx.me.avatar_url}')
                    embed1.add_field(name="helppoints", value=f'To get a help page about points.',  inline=False)
                    embed1.add_field(name="ping", value="To check Abode's latency", inline=False)
                    embed1.add_field(name="8ball", value="To ask Abode an 8ball question", inline=False)
                    embed1.add_field(name="echo", value="To make Abode repeat something \n"
                                                                    "``.hi`` To get a random gretting from over 50 languages.", inline=False)
                    embed1.add_field(name="points/p ", value="To see your contribution points for the server. ``p @Vein#8177`` to see points of a specific user.", inline=False)

                    embed1.add_field(name="userinfo", value="To make Abode get the general info on the user", inline=False)
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
                    embed3.add_field(name="lenny", value="To make Abode send a lenny face", inline=False)
                    embed3.add_field(name="welcome", value="To make Abode welcome a new user", inline=False)
                    embed3.set_footer(text=f"Requested by {ctx.message.author.name}")


                    embed3.set_thumbnail(url=f'{ctx.guild.icon_url}')



                    embeds= [embed1, embed2, embed3]
                    paginator = BotEmbedPaginator(ctx, embeds)
                    await paginator.run()
                else:
                    msg = ctx.message
                    await msg.add_reaction('<:xmark:773959363379462184>')





        @commands.command(alaises=['moderationcommands'])
        @commands.guild_only()
        @commands.has_permissions(kick_members=True)
        async def helpmod(self,ctx):

                embed1= discord.Embed(color=color)
                embed1.set_author(name="Mod Commands", icon_url=f'{ctx.me.avatar_url}')
                embed1.add_field(name="Clear", value= "**Aliases** : Purge\n"
                                                        "**Limit** : 200 \n"
                                                        "**Default value** : 3 \n"
                                                        "**Permission** : Manage messages \n"
                                                        "**Roles** : Elder or higher\n"
                                                        "**Usage**\n ```.clear 10```\n\n"
                                                        )
                embed1.add_field(name="Clearuser", value= "**Aliases** : Purgeuser, Clearuser\n"

                                                        "**Permission** : Manage messages\n"
                                                        "**Roles** : Elder or higher\n"
                                                        "**Usage**\n ```.clearuser @Vein#8177 10```\n\n")
                embed1.add_field(name="‎‎‎‏‏‎ ", value='‎‎‎‏‏‎ ')
                embed1.add_field(name="DM", value = f"**Aliases** : PM\n"

                                                        "**Permission** : Manage messages\n"
                                                        "**Roles** : Elder or higher\n"
                                                        "**Usage**\n ```.dm Idek why this is a command.```\n\n")
                embed1.add_field(name="Dmuser", value = f"**Aliases** : Pmuser\n"

                                                        "**Permission** : Manage messages\n"
                                                        "**Roles** : Elder or higher\n"
                                                        "**Usage**\n ```.dmuser @Vein#8177 why this is a command.```\n\n")
                embed1.set_footer(text=f"Tip : All the command names are case insensitive.")


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
                embed2.set_footer(text=f"Tip : If you are a new elder feel free to bug your seniors. ")
                embed3= discord.Embed(color=color)

                embed3.add_field(name="cnick", value=f"**Aliases** : None\n"

                                                        "**Permission** : Change nickname\n"
                                                        "**Roles** : Outer elder or higher\n"
                                                        "**Usage**\n ```.cnick @Vein#8177 Waifu ```\n"
                                                        "**Example :** \n\n", inline= False)
                embed3.set_image(url=f'{nickname}')

                embed3.set_footer(text=f"Tip : Altough the commands are insensitive the role names aren't be carefull.")
                embed4 = discord.Embed(color = color)
                embed4.add_field(name='role', value=f"**Aliases** : None\n"
                                                    f'**What for** : To add or remvoe roles to the mentioned user.\n'
                                                        "**Permission** : Manage roles\n"
                                                        "**Roles** : Inner elder or higher\n"
                                                        "**Usage**\n ```.role @Vein#8177 Head Insturctor ```\n"
                                                        "**Example :** \n\n", inline= False)
                embed4.set_image(url=f'{role}')
                embed4.set_footer(text='Tip : Is used on the user who already has the role the bot will remove the role.')
                embed5 = discord.Embed (color = color)
                embed5.add_field(name='Channelstats', value= f"**Aliases** : cstats\n"


                                                        "**Roles** : Outer elder or higher\n"
                                                        "**Usage**\n ```.Channelstats ```\n"
                                                        , inline= False)
                embed5.add_field(name='Slowmode', value= f"**Aliases** : smode\n"
                                                        "**Permission** : Manage channel"

                                                        "**Roles** : Inner or higher\n"
                                                        "**Usage**\n ```.Slowmode 10 ```\n\n"
                                                        "**Example **:")
                embed5.set_footer(text='Tip : Only read mods use Channelstats. \nTip2 : ".Slowmode remove" will remove the slowmode. ')
                embed5.set_image(url=f'{slowmode}')
                embed6= discord.Embed(color=color)
                embed6.add_field(name='Poll', value=f"**Aliases** : None\n"
                                                        "**Limit** : 7\n"
                                                        "**Atleast** : 2\n"
                                                        "**Roles** : Outer elder or higher\n"
                                                        '**Usage**\n ```.poll "Poll title here" "Option1" "Option2" ```\n'
                                                        "**Example :** \n\n", inline= False)
                embed6.set_footer(text=f'Tip : If your options are "yes" and "no", Abode will react with a tick and a cross.')
                embed6.set_image(url=f'{poll}')
                embed7 = discord.Embed(color=color)
                embed7.add_field(name='Lock / Unlock', value=f'**Aliases : **None\n**For :** Verified role\n**Roles :** Supreme elder or higher. \n**Usuage :** ```.lock / .unlock```', inline=False)
                embed7.add_field(name='Roleinfo', value=f"**Aliases : **  rinfo\n"

                                                        "**Roles :**  Inner elder or higher\n"
                                                        '**Usage**\n ```.roleinfo Verified ```\n'
                                                        ,)
                embed7.set_footer(text=f'You earn a custom role for being an elder, don\'t forget to ask one for yourself.')

                embeds = [embed1, embed2,embed3, embed4, embed5, embed6, embed7]
                paginator = BotEmbedPaginator(ctx, embeds)
                await paginator.run()


        @commands.command(aliases=['helpstats', 'helpp'])
        @commands.guild_only()
        async def helppoints(self, ctx):
            ch = 781535649843904562

            if ctx.channel.id != (ch):

                msg = ctx.message
                return await msg.add_reaction('<:xmark:773959363379462184>')
            embed1= discord.Embed(color =color)
            embed1.add_field(name="Stats / Statsu", value='To see your points, stats info.\n'
                                                            'To check someone\'s stats, ``.stats <userid>``', inline=False)
            embed1.add_field(name="addcommand", value='To add your own custom command.You need ``500`` points to buy a command and you can\'t overrite an existing command.', inline=False)
            embed1.add_field(name="aliases", value='To add an aliases to your name')
            embeds = [embed1]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()












def setup(Bot):
    Bot.add_cog (vein9(Bot))
    print("Help cog is working.")
