import discord
import random
from discord.ext import commands
from random import randint

class vein5(commands.Cog, name= "games"):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def rps(self, ctx, msg: str):

        tie_data= ['Tie for this time but I am sure I will win the next time.', 'We have tied, a good battle.',
        'It was a good battle, learned alot from you but a tie is a tie', 'Good batlle, you didnnot disappoint me.']

        win_data= ['Sorry but I will be taking the crown for today.','Hehe, no victory for you today, friend. ',
         'A good match but you lost.', 'I have seen better from you.', 'Weakness disgusts me.', 'I see no god up here, other than me!' ]

        data = ['I have lost this time but it doesnot mean that this is over', 'I have lost, good battle.',
        'Never felt a defeat in so long.', 'Ah the smell of defeat, finally!', 'I have lost to a meer human',
        'Hey kid, you won but not for long.', 'I have lost this time but next time I will crush you!']

        t = ["rock", "paper", "scissors"]
        result = None
        tcolor = None
        computer = t[randint(0, 2)]
        player = msg.lower()

        if player == computer:
            result= tie_data

        elif player == "scissors":

            if computer == "rock":
                result=win_data
            else:
                result= data

        elif player == "rock":
            if computer == "paper":
               result= win_data
            else:
                result= data

        elif player == "paper":
            if computer == "scissors":
                result= win_data

            else:
                result= data
        else:
            await ctx.send("Do I have to teach you rock scissors and paper now?")

        if result==win_data:
            tcolor=0x2eff5d
        if result==data:
            tcolor=0xff0003
        if result ==tie_data:
            tcolor=0x529dff


        final_result= random.choice(result)
        embed= discord.Embed(color=tcolor,
                             title= f"Rock Paper Scissors")
        embed.set_thumbnail(url=f'https://media.tenor.com/images/5969d2658a51ef93de54a0049fffac9e/tenor.gif')
        embed.add_field(name="I choose:", value= f'**{computer}**' ,inline=True)

        embed.add_field(name=f"Abode's words:", value=f'"**{final_result}**"',inline=False)


        embed.set_footer(text=f'Played with {ctx.author}',icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(vein5(client))
    print("Games cogs is working.")
