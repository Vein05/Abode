import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

import disputils
from disputils import BotEmbedPaginator
color = 0xa100f2

class vein9(commands.Cog, name='Help'):
        def __init__(self, client):
            self.client = client

        @commands.command()
        @commands.guild_only()
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
                embed1.add_field(name="points/p ", value="To see your contribution points for the server. ``p @Vein#8177`` to see points of a specific user.", inline=False)

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
                embed3.add_field(name="lenny", value="To make Abode send a lenny face", inline=False)
                embed3.add_field(name="welcome", value="To make Abode welcome a new user", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.message.author.name}")


                embed3.set_thumbnail(url=f'{ctx.guild.icon_url}')



                embeds= [embed1, embed2, embed3]
                paginator = BotEmbedPaginator(ctx, embeds)
                await paginator.run()
            else:
                await ctx.send(f"{ctx.message.author.display_name}, This command only works on Bots category.")




        @commands.command(alaises=['moderationcommands'])
        @commands.guild_only()
        @commands.has_permissions(kick_members=True)
        async def helpmod(self,ctx):
            try:
                embed= discord.Embed( color=color)
                embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
                embed.set_author(name="Main commands of Abode.", icon_url=f'{ctx.me.avatar_url}')
                embed.add_field(name="‎‎‎‏‏‎‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ‎‎‎‏‏‎ ㅤModeration", value=f"**DM** \nTo make Abode DM you something, ``.dm Abode``\n"
                                                            f'**DMuser** \nTo make Abode DM a specific Use, ``.dm @Vein#8177 Abode``\n\n'
                                                            f"**clear ** \nTo clear messages sent ``.purge 3``, default no of message that bot clears is ``3``.\n"
                                                            f'**clearuser** \nTo clear messages of a specific user, be carefull while using this ``.clearuser @Vein#8177 10``'
                                                            , inline=False)

                embed.add_field(name="‎‎‎‏‏‎ ‎ ", value= "**Kick** \nTo kick a user, make sure to have a reason in the command ``Kick @Vein#8177 being too cool``\n\n"
                                                            "**ban** \nTo ban a user, make sure to have a reason in the command ``ban @Vein#8177 being too annoying, as always``\n\n"
                                                            "**cnick** \nTo change the server nickname of the meantioned user ``.cnick @Vein#8177 Waifu``\n\n"
                                                            "**role** \nTo add a role to an user ``.role @Vein#8177 Civilian`` note : the spellings or the letter case should not be wrong. \n\n"
                                                                , inline=False)


                embed.add_field(name="‎‎‎‏‏ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤUtility", value= '**channelstats** \nTo show the stats/info of the channel the command is used on ``.channelstats``\n\n'\
                                                        '**poll** \nTo make a poll about things. ``.poll "Poll title here" "option 1" "option2" "option3" "option4"`` if you don\'t get it just see the pinned message on <#757128532789821490>\n\n'
                                                        '**(add / remove)points** \nTo add or remove points on users ``.addpoints @Vein#8177 2000`` also the limit is 2000.\n\n'
                                                        '**slowmode** To add slowmode on a channel, ``.slowmode 10`` to remove the slowmode ``.slowmode remove``.', inline=False)

                embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=(ctx.author.avatar_url))
                embed.timestamp= datetime.datetime.utcnow()
                await ctx.message.author.send(embed=embed)
                await ctx.send(f'{ctx.message.author.display_name}, Sent you a DM.', delete_after=10)
                await ctx.message.delete()
            except:
                await ctx.send(f'{ctx.message.author.display_name}, You have your dms closed.', delete_after=10)
                await ctx.message.delete()






def setup(client):
    client.add_cog (vein9(client))
    print("Help cog is working.")
