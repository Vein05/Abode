import discord
from discord.ext import commands
import traceback
import pymongo
from pymongo import MongoClient
import datetime

class vein7(commands.Cog, name='db'):
    def __init__(self,client):
        self.cleint = client



    @commands.command()
    async def addnote (self, ctx, *, data):
        print('test1')
        author_id= str(ctx.message.author.id)

        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Notes']

        print('test2')

        if (collection.find_one({"_id": author_id})== None):
            user_data= {"_id": author_id, "note": data}
            collection.insert_one(user_data)
            await ctx.send(f'Just added a note for ``{ctx.message.author.display_name}``.')
            print('test3')
        else:
            query= {"_id": author_id}
            user = collection.find(query)
            for note in user:

                new_data= data

            collection.update_one({"_id":author_id}, {"$set":{"note": new_data}})
            await ctx.send(f"Just updated notes for ``{ctx.message.author.display_name}``.")


    @commands.command()
    async def note (self, ctx):
        author_id= str(ctx.message.author.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Notes']
        user_id= {"_id": author_id}
        dbnote = collection.find(user_id)


        if (collection.find_one({"_id": author_id})== None):
            await ctx.send(f'Please add a note using ``.addnote``.')


        for nte in dbnote:
            cur_note = nte['note']
            embed= discord.Embed(color= ctx.author.color)
            embed.add_field(name=f'ㅤ', value= f'{ctx.author.display_name}\'s Note: \n\n **{cur_note}**')

            await ctx.send(embed=embed)


def setup (client):
    client.add_cog (vein7(client))
    print("DB cogs is working.")
