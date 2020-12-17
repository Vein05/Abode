import discord
from discord.ext import commands
from datetime import datetime
import pymongo
from pymongo import MongoClient
import random
from discord.utils import get
mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"
cluster= MongoClient(mongo_url)



class fist(commands.Cog, name ='Fist'):
    def __init__(self, Bot):
        self.Bot = Bot
        self.fistboard = self.Bot.get_channel(789009245436903474)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payLoad):
        emoji_id = 757112296094040104
        if payLoad.emoji.id != emoji_id:
            return
        db = cluster['AbodeDB']
        collection= db['starboard']
        message = await self.Bot.get_channel(payLoad.channel_id).fetch_message(payLoad.message_id)
        guild = message.guild
        message_id = int(message.id)
        query = {"_id":message_id}
        x = collection.find(query)
        for fi in x:

            hmm = fi['_id']
            stars = fi['stars']
            stmsg = fi['starmsg']
            new_star = stars-1
            if new_star <= 0:
                channel = message.guild.get_channel(789009245436903474)

                fetch = await channel.fetch_message(stmsg)
                await fetch.delete()
                collection.delete_one({"_id" : message_id})
            if new_star >= 1:
                    embed = discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
                    embed.set_author(name=f"{message.author.name}", icon_url=f'{message.author.avatar_url}')
                    embed.set_thumbnail(url =f'{message.guild.icon_url}')
                    #embed.add_field(name= f'Fist', value=f'{new_star}<:Cuppedfist:787245768968241162>')
                    embed.add_field(name='Channel', value=f'{message.channel.mention}')


                    try:
                        embed.set_image(url=message.attachments[0].url)

                    except:


                        if (len(str(message.clean_content)) > 1024):
                            x = message.clean_content
                            embed.add_field(name='Content', value=x[:1023],  inline=False)


                        if (len(message.clean_content)) > 1:
                            embed.add_field(name="Content", value=f'{message.clean_content} ',inline=False)

                        else :
                            embed.add_field(name="Content", value=f'Error loading content.',inline=False)
                    embed.add_field(name='Message', value=f'[Jump to the exact message]({message.jump_url})', inline=False)
                    fetch = await self.fistboard.fetch_message(stmsg)
                    await fetch.edit(f'{count} <:Cuppedfist:787245768968241162>ㅤㅤ``({message.id})``\n',embed=embed)
                    collection.update_one({"_id":message_id}, {"$set":{"stars": new_star}})



    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payLoad):

            emoji_id = 757112296094040104
            if payLoad.emoji.id != emoji_id:
                return

            db = cluster['AbodeDB']
            collection= db['starboard']
            count = 1
            message = await self.Bot.get_channel(payLoad.channel_id).fetch_message(payLoad.message_id)
            guild = message.guild
            if payLoad.emoji.id == emoji_id:
                channel = self.fistboard

                reaction = get(message.reactions, emoji=payLoad.emoji)
                if not reaction.count >= count:
                    return

            if payLoad.member.id != message.author.id:



                message_id = int(message.id)
                name = int(message.author.id)

                if (collection.find_one({"_id": message_id}) == None):

                    embed = discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
                    embed.set_author(name=f"{message.author.name}", icon_url=f'{message.author.avatar_url}')
                    embed.set_thumbnail(url =f'{message.guild.icon_url}')
                    #embed.add_field(name= f'Fist', value=f'{count}<:Cuppedfist:787245768968241162>')
                    embed.add_field(name='Channel', value=f'{message.channel.mention}')


                    try:
                        embed.set_image(url=message.attachments[0].url)

                    except:


                        if (len(str(message.clean_content)) > 1024):
                            x = message.clean_content
                            embed.add_field(name='Content', value=x[:1023],  inline=False)


                        if (len(message.clean_content)) > 1:
                            embed.add_field(name="Content", value=f'{message.clean_content} ', inline=False)

                        else :
                            embed.add_field(name="Content", value=f'Error loading content.',inline=False)
                    embed.add_field(name="** **", value=f'**    **➤ [Jump to the exact message]({message.jump_url})', inline=False)
                    channel = message.guild.get_channel(789009245436903474)
                    x1 = await channel.send(f'**{count}** <:Cuppedfist:787245768968241162>ㅤ ``({message.id})``\n',embed=embed)

                    thing = {"_id": message_id, "stars" : 1, "starmsg" : x1.id }
                    collection.insert_one(thing)

                else:

                    query = {"_id": message_id}
                    fist = collection.find(query)
                    for fi in fist:

                        msg_id = fi['_id']
                        nxt_id = fi['starmsg']

                        star = fi['stars']
                        new_star= star + 1

                        collection.update_one({"_id":message_id},  {"$set":{"stars": new_star}})

                        embed = discord.Embed(color = random.choice(self.Bot.color_list), timestamp=datetime.utcnow())
                        embed.set_author(name=f"{message.author.name}", icon_url=f'{message.author.avatar_url}')
                        embed.set_thumbnail(url =f'{message.guild.icon_url}')
                        #embed.add_field(name= f'Fists', value=f'{new_star} <:Cuppedfist:787245768968241162>')
                        embed.add_field(name='Channel', value=f'{message.channel.mention}')
                        embed.add_field(name='Message', value=f'[Jump to the exact message]({message.jump_url})', inline=False)

                        try:
                            embed.set_image(url=message.attachments[0].url)

                        except:
                            embed.add_field(name="Content", value=f'{message.clean_content} ',inline=False)

                    channel = message.guild.get_channel(789009245436903474)
                    msg = channel.fetch_message(nxt_id)
                    await msg.edit(f'{count} <:Cuppedfist:787245768968241162> ㅤ``({message.id})``\n',embed=embed)

            else:

                await message.remove_reaction(payLoad.emoji, payLoad.member)









def setup (Bot):
    Bot.add_cog (fist(Bot))
    print("Fistboard cog is working.")
