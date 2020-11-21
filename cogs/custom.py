import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient



class vein6(commands.Cog, name= "custom"):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def a(self, ctx, *, arg: str):

            mongo_url= "mongodb://Abode:sap6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
            cluster= MongoClient(mongo_url)
            db = cluster['AbodeDB']
            collection= db['Gifs']



            vein = (arg)

            user_id= {"_id": vein}
            dbnote = collection.find((user_id))

            for nte in dbnote:




                giflink = nte['link']
                print(gifname)
                await ctx.send(f'{giflink}')







    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def addcommand(self, ctx, name ,*, arg):
        author_id = str(ctx.message.author.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Gifs']
        user_id= {"_id": name}
        cmd_name = {"user_id": author_id}
        link = arg

        if (collection.find_one({"name": cmd_name})== True):
            await ctx.send(f'``{ctx.message.author.name}``, this command already exists please try another name.')

        else:
            gif_data= {"_id": name, "Mod": ctx.author.name, "user_id": author_id, "link": link}
            collection.insert_one(gif_data)
            await ctx.send(f'Just added a new command ``{name}``.')


















    @commands.command()
    async def token(self, ctx):
        await ctx.send(f'https://pbs.twimg.com/media/EUqVvbQUcAAtL1H.jpg:large')

    @commands.command()
    async def vein2(self, ctx):
        await ctx.send(f'Why call the lord?')

    @commands.command()
    async def sap(self, ctx):
        await ctx.send(f'https://tenor.com/view/lotta-sap-christmas-vacation-christmas-tree-pine-tree-gif-16521866')

    @commands.command()
    async def vein(self,ctx):
        await ctx.send(f'https://media.discordapp.net/attachments/705447271285784578/722838393075007558/vein_orig.gif?width=1152&height=648')
        await ctx.message.delete()

    @commands.command()
    async def mortal(self,ctx):
        await ctx.send(f'https://media1.tenor.com/images/31411b30062cb1ca41e38c33e7d04840/tenor.gif?itemid=4331350')

    @commands.command()
    async def fate(self,ctx):
        await ctx.send(f'Fate knows no bound')

    @commands.command()
    async def leery(self,ctx):
        await ctx.send(f'https://tenor.com/view/party-pooper-everything-sucks-scott-pilgrim-vs-the-world-gif-6015471')


def setup (client):
    client.add_cog (vein6(client))
    print("Custom cog is working.")
