import discord
from discord.ext import commands

import pymongo
from pymongo import MongoClient
import datetime


mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
cluster= MongoClient(mongo_url)

class vein7(commands.Cog, name='db'):
    def __init__(self,Bot):
        self.Bot = Bot



    @commands.command()
    @commands.guild_only()
    async def addnote (self, ctx, *, data):
        await ctx.message.delete()
        author_id= str(ctx.message.author.id)
        time= datetime.datetime.utcnow()
        #time= str(ctx.message.created_at.strftime("%Y-%m-%d, %I:%M:%S UTC"))

        db = cluster['AbodeDB']
        collection= db['Notes']



        if (collection.find_one({"_id": author_id})== None):
            user_data= {"_id": author_id, "note": data, "time": time}
            collection.insert_one(user_data)
            await ctx.send(f'Just added a note for ``{ctx.message.author.display_name}``. To see your note just ``.note``.')

        else:

            query= {"_id": author_id}
            user = collection.find(query)


            for n in user:

                new_data= data
                new_time= time

            collection.update_one({"_id":author_id}, {"$set":{"note": new_data}})
            collection.update_one({"_id":author_id},  {"$set":{"time": new_time}})

            await ctx.send(f"Just updated notes for {ctx.message.author.display_name}. To see you note just ``.note``", delete_after=15)



    @commands.command()
    @commands.guild_only()
    async def note (self, ctx):
        author_id= str(ctx.message.author.id)

        db = cluster['AbodeDB']
        collection= db['Notes']
        user_id= {"_id": author_id}
        dbnote = collection.find(user_id)


        if (collection.find_one({"_id": author_id})== None):
            await ctx.send(f'{ctx.message.author.display_name}, Please add a note using ``.addnote``.' , delete_after=15)


        else:
            for nte in dbnote:

                cur_note = nte['note']
                time= nte['time']
                embed= discord.Embed(color= ctx.author.color, timestamp= time, description= f'{cur_note}' )
                embed.set_author(name=f"{ctx.author.name}'s note:", icon_url= ctx.author.avatar_url)
                embed.set_footer(text=f'Created at ')


            '''confirmation = BotConfirmation(ctx, 0xa100f2)
            msg = await confirmation.confirm(f"{ctx.author.name}, do you want me to DM you your note or show it here? \nReact with ✅ for the DM or react with ❌ if you want me to send it here.\n**Be quick!**")
            if confirmation.confirmed:
                try:
                    await ctx.author.send(embed=embed)
                    await msg.delete()


                except:
                    await ctx.send(f'{ctx.author.name}, Your dms are off.')
            else :
                await ctx.send(embed=embed)'''

            def check(reaction,user):
                    return user == ctx.author and user.id != 759784064361299989


            msg = await ctx.send(f"{ctx.author.name}, do you want me to DM me your note or show it here? React with ✅ for the DM or react with ❌ if you want me to send it here.")

            await msg.add_reaction('✅')
            await msg.add_reaction('❌')

            reaction, user= await self.Bot.wait_for("reaction_add",timeout=30, check=check)




            if str(reaction.emoji) == '✅':

                try:
                    await ctx.author.send(embed=embed)
                    await msg.delete()
                except:
                    await ctx.send(f'You have your DMs closed.')
                    await msg.delete()
            elif str(reaction.emoji) == '❌':
                await ctx.send(embed=embed)
                await msg.delete()






    @commands.command()
    @commands.guild_only()
    async def removenote (self, ctx):
        author_id= str(ctx.message.author.id)

        db = cluster['AbodeDB']
        collection= db['Notes']
        user_id = {"_id": author_id}
        if (collection.find_one({"_id": author_id})== None):
            await ctx.send(f'{ctx.message.author.display_name}, Please add a note using ``.addnote``.')

        collection.delete_one(user_id)

        await ctx.send(f'{ctx.message.author.display_name}, Just removed your note. To add a new note just ``.addnote <note>``.')











def setup (Bot):
    Bot.add_cog (vein7(Bot))
    print("DB cogs is working.")
