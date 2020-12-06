import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import random
from random import randint

color = 0xa100f2
guild = 757098499836739594
battle = ("put battle chnl id here")

mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
cluster= MongoClient(mongo_url)
class vein11(commands.Cog, name='battle'):
    def __init__(self, client):
        self.client= client

    @commands.command(aliases=['battle'])
    @commands.guild_only()
    async def challenge(self, ctx, member: discord.Member):
        if ctx.guild.id != (guild):
            return await ctx.send('Main server only ;)')
        if ctx.channel.id != (757941959796195484):
            return
        if member.id == ctx.author.id:
            msg = ctx.message
            await msg.add_reaction('<:WeirdChamp:757112297096216627>')
            return
        if member.bot:
            return
        author_id = str(ctx.message.author.id)
        member_id = str(member.id)

        db = cluster['AbodeDB']
        collection= db['Levels']
        hm1 = {"_id" : author_id}
        hm2 = {"_id" : member_id}
        author_db = collection.find(hm1)
        member_db = collection.find(hm2)
        if (collection.find_one({"_id": member_id})== None):
            await ctx.send(f'{member.name} is not on the database.')
        def check(reaction,user):
                return user.id == member.id and user.id != 759784064361299989


        msg = await ctx.send(f"{member.name} {ctx.author.mention} wants to challenge you to a duel. React with <:check:773959361953267742> to accept the battle or react with <:xmark:773959363379462184> to deny the challenge.")
        await msg.add_reaction('<:check:773959361953267742>')
        await msg.add_reaction('<:xmark:773959363379462184>')


        reaction, user= await self.client.wait_for("reaction_add",timeout=30, check=check)



        if str(reaction.emoji) == '<:xmark:773959363379462184>':
            return await ctx.send(f'{member.name} rejected the battle.')
        elif str(reaction.emoji) == '<:check:773959361953267742>':
            await msg.delete()
            await ctx.send(f'Duel accepted.')

        for lvl1 in author_db:
                stre = lvl1['Strength']
                sped = lvl1['Speed']
                defen = lvl1['Defense']
                sol = lvl1['Soul']
                health = lvl1['Health']
                luk = lvl1['Luck']
                qi = lvl1['Qi']
                pth= lvl1['Path']
                nme = lvl1['Name']
        for lvl in member_db:
                stre1 = lvl['Strength']
                sped2 = lvl['Speed']
                defen3 = lvl['Defense']
                sol4 = lvl['Soul']
                health5 = lvl['Health']
                luk6 = lvl['Luck']
                qi7 = lvl['Qi']
                pth8= lvl['Path']
                nme9= lvl['Name']
        smthin = random.randint(1,5)
        new_total_user = (stre + sped + defen + sol + health + (qi*2) + (luk *smthin))
        new_total_member = (stre1 + sped2 + defen3 + sol4 + health5 + (qi7*2) + (luk6 *smthin))

        print (new_total_user)
        print(new_total_member)


        await ctx.send(new_total_member)








def setup (client):
    client.add_cog(vein11(client))
    print("Battle cog is working.")
