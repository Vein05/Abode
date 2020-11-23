import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import datetime


color = 0xa100f2
guild = 757098499836739594

class vein8(commands.Cog, name='leveling'):
    def __init__(self, client):
        self.client= client

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if message.guild.id != 757098499836739594:
            return
        if message.author.id == 759784064361299989:
            return
        if message.author.bot:
            return
        bot1= message.guild.get_channel(757136905329442859)
        bot2= message.guild.get_channel(757136943149613076)
        music= message.guild.get_channel(768684108770574366)
        testing=message.guild.get_channel(757941959796195484)
        if message.channel.id == (bot1.id) or message.channel.id == (bot2.id) :
            return
        if message.channel.id == (music.id) or message.channel.id == (testing.id):
            return
        author_id= str(message.author.id)

        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Levels']
        user_id = {"_id": author_id}

        if (collection.find_one({"_id": author_id})== None):

            leauge = "Novice scholar"
            user_data= {"_id" : author_id, "points": 1, "Leauge": leauge,"Qi": 0}
            collection.insert_one(user_data)


        else:
            query= {"_id": author_id}
            level = collection.find(query)


            for lvl in level:
                cur_p= lvl['points']
                new_p= cur_p + 1


                cur_q = lvl['Qi']
                new_q = cur_q + 0.25
                Leauge = lvl['Leauge']

                if (new_q % 200) == 0:
                    await ctx.send(f'<:Cuppedfist:757112296094040104> {message.author.mention}, you Qi just got to {new_q}. ')
                if (new_q == 500):
                    await ctx.send(f'<:Cuppedfist:757112296094040104> {message.author.mention}, Congragulations you earned the ``intermediate scholar`` medal.')
                    new_medal1 = 'Intermediate scholar'
                    collection.upate_one({"_id" : author_id}, {"$set":{"Leauge" : new_medal1}})

                elif (new_q == 1500):
                    await ctx.send(f'<:Cuppedfist:757112296094040104> {member.author.mention}, Congragulations you earned the ``Expert scholar`` medal.')
                    new_medal2= 'Expert scholar'
                    collection.upate_one({"_id" : author_id}, {"$set": {"Leauge" : new_medal2}})
                collection.update_one({"_id":author_id}, {"$set":{'points':new_p}})
                collection.update_one({"_id":author_id},  {"$set":{"Qi": new_q}})




    @commands.command(aliases=['apoints'])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def addpoints(self, ctx, member:discord.Member, *,amount):
        if ctx.guild.id != (guild):
            return await ctx.send('<:WeirdChamp:757112297096216627> Come to the main server if you dare.')
        if int(amount) <= 2000:
            memeber_id= str(member.id)

            mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

            cluster= MongoClient(mongo_url)
            db = cluster['AbodeDB']
            collection= db['Levels']
            user_id = {"_id": memeber_id}

            query = {"_id": memeber_id}
            points = collection.find(query)

            if collection.find_one({"_id" : memeber_id} == None):
                await ctx.send(f"{ctx.author.name}, No such user by the name {member.name} exists. ")
            for point in points:
                old_p = point['points']

                amount_n = int(amount)

                new_p = (int(old_p) + int(amount_n))

                collection.update_one({"_id" : memeber_id}, {"$set" : {"points" : new_p}} )
                await ctx.send(f"Sucessfully added ``{amount}`` points to {member.name}. Now {member.name} has ``{new_p}`` in total.")
        elif int(amount) >= 2000:
            await ctx.send(f"<:WeirdChamp:757112297096216627> {ctx.author.name}, 2000 is the limit for now.")


    @commands.command(aliases=['rpoints'])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def removepoints(self, ctx, member:discord.Member, *,amount):
        if ctx.guild.id != 757098499836739594:
            return await ctx.send('<:WeirdChamp:757112297096216627> Come to the main server if you dare.')
        if ctx.author.top_role < member.top_role:
            return await ctx.send("You can't remove points of someone higher than you.")

        if int(amount) <= 2000:
            memeber_id= str(member.id)

            mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

            cluster= MongoClient(mongo_url)
            db = cluster['AbodeDB']
            collection= db['Levels']
            user_id = {"_id": memeber_id}

            query = {"_id": memeber_id}
            points = collection.find(query)

            if collection.find_one({"_id" : memeber_id} == None):
                await ctx.send(f"{ctx.author.name}, No such user by the name {member.name} exists. ")
            for point in points:
                old_p = point['points']

                amount_n = int(amount)

                new_p = (int(old_p) - int(amount_n))

                collection.update_one({"_id" : memeber_id}, {"$set" : {"points" : new_p}} )
                await ctx.send(f"Sucessfully removed ``{amount}`` points from {member.name}. Now {member.name} has ``{new_p}`` in total.")
        if int(amount) > 2000:
            await ctx.send(f"{ctx.author.name}, you can't remove more than 2000 points. <:WeirdChamp:757112297096216627>")




    '''@commands.command(aliases=["lb"])
    @commands.guild_only()
    async def leaderboard (self, ctx):
        member = discord.Member or ctx.author

        memeber_id= str(member.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']

        collection= db['Levels']

        users = collection.find()
        embed =discord.Embed(title="Leaderboard",color = color)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        for i in users:

            _id= i['_id']

            points = i['points']
            medal = i['Leauge']
            qi = i['Qi']






            embed.add_field(name=f'<@{_id}>', value='**Points**\n'
                                f'{str(points)}\n\n'
                                f'**Qi** \n'
                                f'{str(qi)}\n\n'
                                f'**Leauge** \n'
                                f'{str(medal)} \n', inline=False)


        await ctx.send(embed=embed)'''





    @commands.command(aliases=["points", "qi"])
    @commands.guild_only()
    async def point (self, ctx):
        if ctx.guild.id != (guild):
            return
        member= ctx.author


        member_id= str(member.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']

        collection= db['Levels']
        qurey = {"_id" : member_id}
        users = collection.find(qurey)

        hm = collection.find().sort("points" , -1)
        a = 0
        for x in hm:


            idd = x["_id"]


            if idd == member_id:
                break
            else:
                a += 1
                print(a)
        for i in users:
            _id= i['_id']

            points = i['points']
            medal = i['Leauge']
            qi = i['Qi']

            embed= discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url = f'{ctx.guild.icon_url}')

            embed.set_author(name=f'{member.name} ', icon_url=f'{member.avatar_url}')
            embed.add_field(name=f'Rank', value=f'#{int(a) +1}', inline=False)
            embed.add_field(name='Points', value=f'{str(points)}')
            embed.add_field(name='Qi', value=f'{str(qi)}')
            embed.add_field(name='Medal', value=f'{str(medal)}', inline=False)
            embed.set_footer(text=f"Contribution Points")
            await ctx.send(embed=embed)




    @commands.command(aliases=["p", "puser"])
    @commands.guild_only()
    async def pointinfo (self, ctx, member:discord.Member):
        if ctx.guild.id != (guil):
            return



        member_id= str(member.id)
        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']

        collection= db['Levels']
        qurey = {"_id" : member_id}
        users = collection.find(qurey)

        hm = collection.find().sort("points" , -1)
        a = 0
        for x in hm:


            idd = x["_id"]


            if idd == member_id:
                break
            else:
                a += 1
                print(a)
        for i in users:
            _id= i['_id']

            points = i['points']
            medal = i['Leauge']
            qi = i['Qi']

            embed= discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url = f'{ctx.guild.icon_url}')

            embed.set_author(name=f'{member.name} ', icon_url=f'{member.avatar_url}')
            embed.add_field(name=f'Rank', value=f'#{int(a) +1}', inline=False)
            embed.add_field(name='Points', value=f'{str(points)}')
            embed.add_field(name='Qi', value=f'{str(qi)}')
            embed.add_field(name='Medal', value=f'{str(medal)}', inline=False)
            embed.set_footer(text=f"Contribution Points")
            await ctx.send(embed=embed)




def setup (client):
    client.add_cog(vein8(client))
    print("Leveling cog is working.")



