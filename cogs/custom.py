import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient



class vein6(commands.Cog, name= "custom"):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def a(self, ctx, *, arg: str):
            #get into the db
            mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
            cluster= MongoClient(mongo_url)
            db = cluster['AbodeDB']
            collection= db['Gifs']



            vein = (arg)

            user_id= {"_id": vein}
            dbnote = collection.find((user_id))
            #acces name from the db and also the link
            for nte in dbnote:




                giflink = nte['link']

                await ctx.send(f'{giflink}')
                await ctx.message.delete()







    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def addcommand(self, ctx, name ,*, giflink):
        author_id = str(ctx.message.author.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Gifs']
        user_id= {"_id": name}
        cmd_name = {"user_id": author_id}
        link = giflink
        #adds a command to the db it's just a link ngl lmao
        #idek why i used try here but it works
        try:
            gif_data= {"_id": name, "Mod": ctx.author.name, "user_id": author_id, "link": link}
            collection.insert_one(gif_data)
            await ctx.send(f'Just added a new command ``{name}``.')
        except:
            await ctx.send(f'{ctx.author.name}, there already exists an custom command by that name please try another name.', delete_after=10)



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
        user_id = {"_id": commandname}
        if (collection.find_one({"_id": commandname})== None):
            await ctx.send(f'{ctx.message.author.display_name}, No command found by that name please try agian with the correct name.', delete_after=10)

        collection.delete_one(user_id)

        await ctx.send(f'{ctx.message.author.display_name}, Just removed a command, add another command through ``.addcommand <name> <link>``.', delete_after=10)


def setup (client):
    client.add_cog (vein6(client))
    print("Custom cog is working.")
