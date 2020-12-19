import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import random
from datetime import datetime

mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
cluster= MongoClient(mongo_url)

class vein6(commands.Cog, name= "custom"):
    def __init__(self, Bot):
        self.Bot = Bot


    '''@commands.Cog.listener()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def on_message(self, message):
        try:
            if message.guild.id != 757098499836739594:
                return
            mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
            cluster= MongoClient(mongo_url)
            db = cluster['AbodeDB']
            collection= db['Gifs']
            vein = str(message.clean_content)
            user_id= {"_id": vein}
            dbnote = collection.find()
            for nte in dbnote:
                gifname = nte['_id']
                giflink= nte['link']
                if f'{seld.Bot.DEFAULT_PREFIX}{gifname}' in message.content:

                    await message.channel.send(f'{giflink}')
        except:
            return'''

    '''@commands.Cog.listener()
    async def on_message(self, message):
        if '<@!759784064361299989>'in message.content:

            await message.channel.send(f'{message.author.mention}My prefix is {self.Bot.DEFAULT_PREFIX}.')'''


    @commands.command(aliases=['cc list'], description=f'List all the available custom commands.')
    @commands.guild_only()
    async def cc_list(self, ctx):

        db = cluster['AbodeDB']
        collection= db['Gifs']
        total = collection.count()
        hm = collection.find().sort("_id" , 1)
        total = collection.count()
        gifname =[]
        embed = discord.Embed(color=random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
        for gifs in hm:
            name = gifs['_id']
            gifname.append(name)
        if len(gifname) >=1024:
            embed.add_field(name=f"Custom Commands ({total})", value= f' ,'.join(gifname[:1023]), inline=False)
        if len(gifname)< 1024:
            embed.add_field(name=f"Custom Commands ({total})", value= f' ,'.join(gifname[:1023]), inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def a(self, ctx, *, arg: str):
            #get into the db

            db = cluster['AbodeDB']
            collection= db['Gifs']



            vein = (arg)

            user_id= {"_id": vein}
            dbnote = collection.find((user_id))
            #acces name from the db and also the link
            for nte in dbnote:
                giflink = nte['link']

                await ctx.send(f'{giflink}')








    @commands.command(aliases=['acommand'])
    @commands.guild_only()

    async def addcommand(self, ctx, name ,*, giflink):
        author_id = str(ctx.message.author.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Gifs']
        collection2 = db ['Levels']
        user_id= {"_id": name}
        cmd_name = {"user_id": author_id}
        link = giflink
        print('check')
        query = {"_id": author_id}
        gifh = collection2.find(query)
        neededpoints = 500
        print('check0')

        for pts in gifh:
            print('check o')
            cur_p = pts['points']
            new_p = (int(cur_p)) - (int(neededpoints))
            if cur_p >=  neededpoints:


                #adds a command to the db it's just a link ngl lmao
                #idek why i used try here but it works
                nme = str(name)
                if (collection.find_one({"_id": nme})== None):
                    gif_data= {"_id": name, "user_id": author_id, "link": link}
                    collection.insert_one(gif_data)
                    collection2.update_one({"_id":author_id},  {"$set": {"points" : new_p}})

                    await ctx.send(f'Just added a new command ``{name}``. {ctx.message.author.name} you now have ``{new_p}`` points.')

                else:
                    await ctx.send(f'{ctx.author.name}, there already exists an custom command by that name please try another name.', delete_after=10)
            elif cur_p < neededpoints:
                x = int(neededpoints) - int(cur_p)

                await ctx.send(f'{ctx.author.name}, you don\'t have required points to buy a command, you still need ``{x}`` points.' )




    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    #duh remove command
    async def removecommand(self, ctx, *, commandname):
        author_id= str(ctx.message.author.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Gifs']
        cmd_name = str(commandname)
        user_id = {"_id": cmd_name}
        if (collection.find_one({"_id": commandname})== None):
            await ctx.send(f'{ctx.message.author.display_name}, No command found by that name please try agian with the correct name.', delete_after=10)

        else:
            collection.delete_one(user_id)

            await ctx.send(f'{ctx.message.author.display_name}, Just removed a command ``{cmd_name}``, add another command through ``.addcommand <name> <link>``.', delete_after=10)


def setup (Bot):
    Bot.add_cog (vein6(Bot))
    print("Custom cog is working.")
