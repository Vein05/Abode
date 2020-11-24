import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import datetime
import random
from random import randint

data= ['Water', 'Air' , 'Earth', 'Fire', 'Destruction', 'Illusion' , 'Time', 'Space', 'Karma', 'Chaos']
paths = random.choice(data)
luck = random.randint(1, 100)
data1= ['Demon', 'Human', 'Dragon', 'Beast', 'Phoenix', 'Spirit', 'Giant', 'Fey']
race = random.choice(data1)
strength= random.randint(1,10)
speed = random.randint(1, 10)
defense = random.randint(1, 10)
soul = random.randint(1, 10)
Hp = random.randint(50, 350)

color = 0xa100f2
guild = 757098499836739594

class vein8(commands.Cog, name='leveling'):
    def __init__(self, client):
        self.client= client

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        #remove the unnecessay things
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
        #checks if user is in the db or not

        if (collection.find_one({"_id": author_id})== None):

            leauge = "Novice scholar"
            Realm = "Mortal"
            Path = paths



            user_data= {"_id" : author_id, "points": 1, "Leauge": leauge,"Qi": 0, "Daos": 0, "Path": Path, "Realm" : Realm , "Luck": luck, "Species" : race, "Strength": strength, "Speed": speed, "Defense" : defense, "Soul" :soul, "Health": Hp }
            collection.insert_one(user_data)


        else:
            query= {"_id": author_id}
            level = collection.find(query)


            for lvl in level:
                cur_p= lvl['points']
                new_p= cur_p + 1

                #this is a mess
                cur_q = lvl['Qi']
                new_q = cur_q + 0.25
                Leauge = lvl['Leauge']
                dao = lvl['Daos']
                stre = lvl['Strength']
                sped = lvl['Speed']
                defen = lvl['Defense']
                sol = lvl['Soul']
                health = lvl['Health']


                if (new_q % 200) == 0:
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> Congragulations! {message.author.mention}, your Qi just reached. ``{new_q}``.')
                elif (new_q % 600) == 0:
                    await message.channel.send(f'{message.author}, you now have comprehendded ``{dao}`` heavenly dao(s).')
                    collection.update_one({"_id":author_id},  {"$set":{"Daos" : +1 }})

                if (new_q == 500):
                    ok = 'Star'
                    collection.update_one({"_id":author_id},  {"$set":{"Realm" : ok }})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``Star realm`` expert.\nAnd also, you earned the ``intermediate scholar`` medal.')
                    new_medal1 = 'Intermediate scholar'
                    collection.update_one({"_id" : author_id}, {"$set":{"Leauge" : new_medal1}})

                elif (new_q == 1500):
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {member.author.mention}, Congragulations you earned the ``Expert scholar`` medal.')
                    new_medal2= 'Expert scholar'
                    collection.upate_one({"_id" : author_id}, {"$set": {"Leauge" : new_medal2}})
                elif (new_q % 10) == 0:
                    collection.update_one({"_id":author_id},  {"$set":{"Strength" : +10}})
                    collection.update_one({"_id":author_id},  {"$set":{"Attack" : +2}})
                    collection.update_one({"_id":author_id},  {"$set":{"Defense" : +1}})
                    collection.update_one({"_id":author_id},  {"$set":{"Soul": +0.25}})
                    collection.update_one({"_id":author_id},  {"$set":{"Health" : +3}})

                if (new_q == 1100):
                    ok = 'Transcendent'
                    collection.update_one({"_id":author_id},  {"$set":{"Realm" : ok}})
                    await message.channel.send(f'{message.author.mention},<:Cuppedfist:757112296094040104> Congragulations! you just brokethrough to become a ``Transcendent realm`` expert.')
                if (new_q == 2500):
                    ok = 'Saint'
                    collection.update_one({"_id":author_id},  {"$set":{"Realm" : ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``Saint realm`` expert.')
                if (new_q == 5100):
                    ok = 'God'
                    collection.update_one({"_id":author_id},  {"$set":{"Realm" : ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``God realm``expert.')
                if (new_q == 10001):
                    ok ='Chaotic'
                    collection.update_one({"_id":author_id},  {"$set":{"Realm" : ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``Chaotic realm`` expert.')




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

        for lvl in users:
            _id= lvl['_id']

            points = lvl['points']
            medal = lvl['Leauge']
            dao = lvl['Daos']
            stre = lvl['Strength']
            sped = lvl['Speed']
            defen = lvl['Defense']
            sol = lvl['Soul']
            health = lvl['Health']
            luk = lvl['Luck']
            qi = lvl['Qi']
            realm = lvl['Realm']
            speci = lvl['Species']
            pth= lvl['Path']

            embed= discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url = f'{ctx.guild.icon_url}')

            embed.set_author(name=f'{member.name} ', icon_url=f'{member.avatar_url}')
            embed.add_field(name=f'Rank', value=f'``#{int(a) +1}``', inline=False)
            embed.add_field(name=f'Realm', value=f'``{str(realm)}``')
            embed.add_field(name='Path', value=f'``{str(pth)}``')
            embed.add_field(name='Qi', value=f'``{str(qi)}``',inline=False)
            embed.add_field(name='Points', value=f'``{str(points)}``')
            embed.add_field(name='Medal', value=f'``{str(medal)}``', inline=False)
            embed.add_field(name='Strength', value=f'``{str(stre)}``')
            embed.add_field(name='Defense', value= f'``{str(defen)}``')
            embed.add_field(name='Speed', value= f'``{str(sped)}``')

            embed.add_field(name='‎‎‎‏‏‎Soul', value=f'``{str(sol)}``')
            embed.add_field(name='Health', value=f'``{str(health)}``')
            embed.add_field(name='Luck', value=f' ``{str(luk)}``')

            embed.set_footer(text=f"Abode of Scholars")
            await ctx.send(embed=embed)




    @commands.command(aliases=["p", "puser"])
    @commands.guild_only()
    async def pointinfo (self, ctx, member:discord.Member):
        if ctx.guild.id != (guild):
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

        for lvl in users:
            _id= lvl['_id']

            points = lvl['points']
            medal = lvl['Leauge']
            dao = lvl['Daos']
            stre = lvl['Strength']
            sped = lvl['Speed']
            defen = lvl['Defense']
            sol = lvl['Soul']
            health = lvl['Health']
            luk = lvl['Luck']
            qi = lvl['Qi']
            realm = lvl['Realm']
            speci = lvl['Species']
            pth= lvl['Path']

            embed= discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url = f'{ctx.guild.icon_url}')

            embed.set_author(name=f'{member.name} ', icon_url=f'{member.avatar_url}')
            embed.add_field(name=f'Rank', value=f'``#{int(a) +1}``', inline=False)
            embed.add_field(name=f'Realm', value=f'``{str(realm)}``')
            embed.add_field(name='Path', value=f'``{str(pth)}``')
            embed.add_field(name='Qi', value=f'``{str(qi)}``',inline=False)
            embed.add_field(name='Points', value=f'``{str(points)}``')
            embed.add_field(name='Medal', value=f'``{str(medal)}``', inline=False)
            embed.add_field(name='Strength', value=f'``{str(stre)}``')
            embed.add_field(name='Defense', value= f'``{str(defen)}``')
            embed.add_field(name='Speed', value= f'``{str(sped)}``')

            embed.add_field(name='‎‎‎‏‏‎Soul', value=f'``{str(sol)}``')
            embed.add_field(name='Health', value=f'``{str(health)}``')
            embed.add_field(name='Luck', value=f' ``{str(luk)}``')

            embed.set_footer(text=f"Abode of Scholars")
            await ctx.send(embed=embed)




def setup (client):
    client.add_cog(vein8(client))
    print("Leveling cog is working.")


