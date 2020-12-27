import discord
from discord.ext import commands, tasks
import datetime
import random
from prettytable import PrettyTable


data = ['Water', 'Air', 'Earth', 'Fire', 'Destruction',
        'Illusion', 'Time', 'Space', 'Karma', 'Chaos']
paths = random.choice(data)
luck = random.randint(1, 100)
data1 = ['Demon', 'Human', 'Dragon', 'Beast',
         'Phoenix', 'Spirit', 'Giant', 'Fey']
race = random.choice(data1)
strength = random.randint(1, 10)
speed = random.randint(1, 10)
defense = random.randint(1, 10)
soul = random.randint(1, 10)
Hp = random.randint(50, 350)

color = 0xa100f2
guild = 757098499836739594


class vein8(commands.Cog, name='leveling'):
    def __init__(self, Bot):
        self.Bot = Bot
        # self.cultivate_over.start()
        self.Bot.scholar_chat = self.Bot.get_channel(757108786497585172)

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        # remove the unnecessay things
        if message.guild.id != 757098499836739594:
            return
        if message.author.id == 759784064361299989:
            return
        if message.author.bot:
            return
        if self.Bot.DEFAULT_PREFIX == '&':
            return
        bot1 = message.guild.get_channel(781535649843904562)
        bot2 = message.guild.get_channel(757136943149613076)
        music = message.guild.get_channel(768684108770574366)
        testing = message.guild.get_channel(757941959796195484)
        if message.channel.id == bot1.id:
            return
        if message.channel.id == (music.id) or message.channel.id == (testing.id):
            return
        author_id = str(message.author.id)

        db = self.Bot.cluster1['AbodeDB']
        collection = db['Levels']
        user_id = {"_id": author_id}
        # checks if user is in the db or not

        if (collection.find_one({"_id": author_id}) == None):

            leauge = "Novice scholar"
            Realm = "Mortal"
            Path = paths

            lol = "None"

            user_data = {"_id": author_id, "points": 1, "Leauge": leauge, "Qi": 0, "Daos": 0, "Path": Path, "Realm": Realm, "Luck": luck,
                         "Species": race, "Strength": strength, "Speed": speed, "Defense": defense, "Soul": soul, "Health": Hp, "Name": lol}
            collection.insert_one(user_data)

        else:
            query = {"_id": author_id}
            level = collection.find(query)

            for lvl in level:
                cur_p = lvl['points']
                new_p = cur_p + 1

                # this is a mess
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
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> Congragulations! {message.author.mention}, your Qi just reached **{new_q}**.')
                elif (new_q % 600) == 0:
                    await message.channel.send(f'{message.author}, you now have comprehendded ``{dao}`` heavenly dao(s).')
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Daos": +1}})

                if (new_q == 500):
                    ok = 'Star'
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Realm": ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``Star realm`` expert.\nAnd also, you earned the ``intermediate scholar`` medal.')
                    new_medal1 = 'Intermediate scholar'
                    collection.update_one({"_id": author_id}, {
                                          "$set": {"Leauge": new_medal1}})

                elif (new_q == 1500):
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {member.author.mention}, Congragulations you earned the ``Expert scholar`` medal.')
                    new_medal2 = 'Expert scholar'
                    collection.upate_one({"_id": author_id}, {
                                         "$set": {"Leauge": new_medal2}})
                elif (new_q % 10) == 0:
                    strength1 = random.randint(1, 15)
                    speed1 = random.randint(1, 10)
                    defense1 = random.randint(1, 25)
                    soul1 = random.randint(1, 5)
                    Hp1 = random.randint(1, 20)
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Strength": stre + strength1}})

                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Speed":  sped + speed1}})
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Defense": defen + defense1}})
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Soul": sol + soul1}})
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Health": health + Hp1}})

                if (new_q == 1100):
                    ok = 'Transcendent'
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Realm": ok}})
                    await message.channel.send(f'{message.author.mention},<:Cuppedfist:757112296094040104> Congragulations! you just brokethrough to become a ``Transcendent realm`` expert.')
                if (new_q == 2500):
                    ok = 'Saint'
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Realm": ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``Saint realm`` expert.')
                if (new_q == 5100):
                    ok = 'God'
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Realm": ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``God realm``expert.')
                if (new_q == 10001):
                    ok = 'Chaotic'
                    collection.update_one({"_id": author_id},  {
                                          "$set": {"Realm": ok}})
                    await message.channel.send(f'<:Cuppedfist:757112296094040104> {message.author.mention} Congragulations! you just brokethrough to become a ``Chaotic realm`` expert.')

                collection.update_one({"_id": author_id}, {
                                      "$set": {'points': new_p}})
                collection.update_one({"_id": author_id},  {
                                      "$set": {"Qi": new_q}})

    @commands.command(aliases=['apoints'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def addpoints(self, ctx, member: discord.Member, *, amount):
        channel = ctx.guild.get_channel(780785741101137926)
        if ctx.guild.id != (guild):
            return await ctx.send('<:WeirdChamp:757112297096216627> Come to the main server if you dare.')
        if int(amount) <= 2000:
            memeber_id = str(member.id)

            db = self.Bot.cluster1['AbodeDB']
            collection = db['Levels']
            user_id = {"_id": memeber_id}

            query = {"_id": memeber_id}
            points = collection.find(query)

            if collection.find_one({"_id": memeber_id} == None):
                await ctx.send(f"{ctx.author.name}, No such user by the name {member.name} exists. ")
            for point in points:
                old_p = point['points']

                amount_n = int(amount)

                new_p = (int(old_p) + int(amount_n))

                collection.update_one({"_id": memeber_id}, {
                                      "$set": {"points": new_p}})
                await ctx.send(f"Sucessfully added ``{amount}`` points to {member.name}. Now {member.name} has ``{new_p}`` in total.")
                embed = discord.Embed(title=f'Addpoints', color=color,
                                      description=f'{ctx.author.mention} added ``{amount}`` points to {member.mention}')
                await channel.send(embed=embed)
        elif int(amount) >= 2000:
            await ctx.send(f"<:WeirdChamp:757112297096216627> {ctx.author.name}, 2000 is the limit for now.")

    @commands.command(aliases=['rpoints'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def removepoints(self, ctx, member: discord.Member, *, amount):
        channel = ctx.guild.get_channel(780785741101137926)
        if ctx.guild.id != 757098499836739594:
            return await ctx.send('<:WeirdChamp:757112297096216627> Come to the main server if you dare.')
        if ctx.author.top_role < member.top_role:
            return await ctx.send("You can't remove points of someone higher than you.")

        if int(amount) <= 2000:
            memeber_id = str(member.id)

            db = self.Bot.cluster1['AbodeDB']
            collection = db['Levels']
            user_id = {"_id": memeber_id}

            query = {"_id": memeber_id}
            points = collection.find(query)

            if collection.find_one({"_id": memeber_id} == None):
                await ctx.send(f"{ctx.author.name}, No such user by the name {member.name} exists. ")
            for point in points:
                old_p = point['points']

                amount_n = int(amount)

                new_p = (int(old_p) - int(amount_n))

                collection.update_one({"_id": memeber_id}, {
                                      "$set": {"points": new_p}})
                await ctx.send(f"Sucessfully removed ``{amount}`` points from {member.name}. Now {member.name} has ``{new_p}`` in total.")
                embed = discord.Embed(title='**Removepoints**', color=color,
                                      description=f'{ctx.author.mention} removed  ``{amount}`` from {member.mention} and now {member.name} has ``{new_p}`` in total')
                await channel.send(embed=embed)
        if int(amount) > 2000:
            await ctx.send(f"{ctx.author.name}, you can't remove more than 2000 points. <:WeirdChamp:757112297096216627>")

    @commands.command(aliases=["points", "qi", "p", 'stats'], description=f'Show your stats and general info.')
    @commands.guild_only()
    async def point(self, ctx):

        if ctx.message.channel.id == 757108786497585172:
            return
        try:
            member = ctx.author

            member_id = str(member.id)

            db = self.Bot.cluster1['AbodeDB']
            collection = db['Levels']
            qurey = {"_id": member_id}
            users = collection.find(qurey)
            total = collection.count()
            hm = collection.find().sort("Qi", -1)
            a = 0
            for x in hm:

                idd = x["_id"]

                if idd == member_id:
                    break
                else:
                    a += 1

            for lvl in users:
                _id = lvl['_id']

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
                pth = lvl['Path']
                nme = lvl['Name']

                embed = discord.Embed(
                    color=color, timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=f'{ctx.guild.icon_url}')

                embed.set_author(name=f'{member.name} ',
                                 icon_url=f'{member.avatar_url}')
                embed.add_field(name=f'__#{int(a) +1}/{total}__', value=f'**Aliases** :{nme} \n'
                                f'**Realm** :  {str(realm)}\n'
                                f'**Species** : {str(speci)}')
                embed.add_field(name="__Legacy__", value=f'**Path** : {str(pth)}\n'
                                f'**Medals** :  {str(medal)}\n'
                                f'**Daos** : {str(dao)}')

                embed.add_field(name='__Accomplishments__', value=f'**Qi : ** {str(qi)}\n'
                                f'**Points : ** {str(points)}\n'
                                f' **Luck : ** {str(luk)}', inline=False)

                embed.add_field(name='__Stats__', value=f'**Strength :** {str(stre)}\n'
                                f'**Defense :** {str(defen)}\n'
                                f'**Speed** : {str(sped)}\n'
                                f'**Soul : **{str(sol)}\n'
                                f'**Health : ** {str(health)}')

                embed.set_footer(text=f"Abode of Scholars")
                await ctx.send(embed=embed)
        except:
            await ctx.send(f'Your data probably isn\'nt saved on the database.')

    @commands.command(aliases=["puser", "statsu"], description=f'Shows shats on another user, be sure to use the user id.')
    @commands.guild_only()
    async def pu(self, ctx, member_id: int):
        if ctx.guild.id != (guild):
            return

        member = ctx.guild.get_member(member_id)

        member_id = str(member_id)

        db = self.Bot.cluster1['AbodeDB']

        collection = db['Levels']
        qurey = {"_id": member_id}
        users = collection.find(qurey)
        total = collection.count()
        hm = collection.find().sort("Qi", -1)
        a = 0
        for x in hm:

            idd = x["_id"]

            if idd == member_id:
                break
            else:
                a += 1

        for lvl in users:
            _id = lvl['_id']

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
            pth = lvl['Path']

            embed = discord.Embed(
                color=color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=f'{ctx.guild.icon_url}')

            embed.set_author(name=f'{member.name} ',
                             icon_url=f'{member.avatar_url}')
            embed.add_field(name=f'__Main__', value=f'**Rank** : #{int(a) +1}/{total}\n'
                            f'**Realm** :  {str(realm)}\n'
                            f'**Species** : {str(speci)}')
            embed.add_field(name="__Legacy__", value=f'**Path** : {str(pth)}\n'
                            f'**Medals** :  {str(medal)}\n'
                            f'**Daos** : {str(dao)}')

            embed.add_field(name='__Accomplishments__', value=f'**Qi : ** {str(qi)}\n'
                            f'**Points : ** {str(points)}\n'
                            f' **Luck : ** {str(luk)}', inline=False)

            embed.add_field(name='__Stats__', value=f'**Strength :** {str(stre)}\n'
                            f'**Defense :** {str(defen)}\n'
                            f'**Speed** : {str(sped)}\n'
                            f'**Soul : **{str(sol)}\n'
                            f'**Health : ** {str(health)}')

            embed.set_footer(text=f"Abode of Scholars")
            await ctx.send(embed=embed)

    @commands.command(aliases=['aliases', 'cname'], description=f'Add your cultivator name.')
    @commands.guild_only()
    async def nickname(self, ctx, *, arg):
        if len(arg) > 10:
            return await ctx.send('Bruh you can\'t go over 10 characthers.')
        if ctx.guild.id != (guild):
            return

        db = self.Bot.cluster1['AbodeDB']
        collection = db['Levels']

        user_id = str(ctx.author.id)
        name = str(arg)

        name = str(arg)
        collection.update_one({"_id": user_id}, {"$set": {"Name": name}})
        await ctx.send(f'{ctx.author.mention} Your cultivator name was sucessfully set to  {arg}.')

    @commands.command(aliases=["lb"], description='Shows the top 10 cultivators on the server.')
    @commands.guild_only()
    async def leaderboard(self, ctx):
        if ctx.channel.id == self.Bot.scholar_chat:
            return

        member = discord.Member or ctx.author

        memeber_id = str(member.id)
        db = self.Bot.cluster1['AbodeDB']
        collection = db['Levels']
        collection2 = db['Levels1']

        users = collection.find().sort("Qi", -1).limit(10)
        names = collection2.find().sort("Name", 1)

        a2 = []
        nme1 = []
        name2 = []
        pts1 = []
        pth1 = []
        table = PrettyTable()
        table1 = PrettyTable()
        a = 0
        table.field_names = ["Rank", "Aliases", "Qi", "Points", "Path"]
        table1.field_names = ["Rank", "Aliases", "Qi", "Points"]
        table.align = "c"
        for u in users:

            user_id = u['_id']
            qi = u['Qi']
            pts = u['points']
            pth = u['Path']
            nme = u['Name']

            a += 1
            hm = str(pts)
            hm1 = str(qi)
            pts1.append(hm)
            nme1.append(nme)
            name2.append(hm1)
            pth1.append(pth)

            '''embed.add_field(name='Aliases', value=f"\n\n".join(nme1))
                embed.add_field(name='Qi', value="\n\n".join(name2))
                embed.add_field(name="Points", value=" \n\n ".join(pts1))

                #embed.add_field(name=f"{a}", value=f'**Aliases : {nme}** \n**Qi : ** {qi}\n**Points : **  {pts}  \n**Path : **{pth}')
                embed.set_footer(text=f'To remove the \'None\' from your name, add your Cultivator name through .aliases')
                await ctx.send(embed=embed)'''

            table.add_row([a, f'{nme}', qi, pts, f'{pth}'])
            table1.add_row([a, f'{nme}', qi, pts])
        if ctx.author.is_on_mobile():
            await ctx.send(f'```prolog\n{table}```')

        else:
            embed = discord.Embed(
                title="Leaderboard \n``You can add your aliases by [.aliases <yourname>]``", color=color, description=f'```prolog\n{table1}```')
            embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
            embed.set_footer(text=f'Requested by {ctx.author.name}')

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cultivate(self, ctx):
        time = 5
        await ctx.send(f'{ctx.author.mention} Your cultivation time has started for {time}m.')

    @tasks.loop(seconds=10)
    async def cultivate_over(self):
        channel = self.Bot.get_channel(764393920381190144)

        await channel.send(f'Cultivation time over ok Qi was gained.')


def setup(Bot):
    Bot.add_cog(vein8(Bot))
    print("Leveling cog is working.")
