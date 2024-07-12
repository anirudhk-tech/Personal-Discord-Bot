import discord
import potter_spells as potter
import wikipediaapi
import badwords
import tronalddump
import praw
import random
import asyncio
import requests
import os
import foaas
import typing
import json
import time
import threading
import chess
import chess.svg
import datetime
import math


from threading import Timer
from dateutil.relativedelta import relativedelta
from datetime import date
from IPython.display import SVG
from discord import Permissions
from discord.ext import commands, tasks
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord import Member
from discord import Activity, ActivityType
from itertools import cycle
from random import choice
from chatbot import Chat, register_call


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = ".", intents = intents)
bot.remove_command('help')
channel_id = 773263673203753003
bots_channel = 778316821689270272
test_channel = 821823025213079556
test_guild = 821823025213079553
ani_id = 635493429429665794
lucky_id = 740702487589421116
dhruvi_id = 779526604132974623
token = "Nzg5NTExNjgxMzg1ODI0MjU3.X9zIDQ.zYhIPQx5wBq29Rvf8lRC6X0QSzw"
Offline = False
status = cycle(['with your life|for help, say ".helpmeout"', 'Minecraft|for help, say ".helpmeout"', 'noobs|for help, say ".helpmeout"', 'chicken|for help, say ".helpmeout"', 'League of Legends|for help, say ".helpmeout"', 'Clash of Clans|for help, say ".helpmeout"', 'getting girls|for help, say ".helpmeout"', 'Chess|for help, say ".helpmeout"', 'a guitar|for help, say ".helpmeout"', 'a violin|for help, say ".helpmeout"', 'a clarinet|for help, say ".helpmeout"', 'your mom|for help, say ".helpmeout"'])
guild = bot.get_guild(773263673203753000)
perms = [ani_id,lucky_id,dhruvi_id]
bois = [ani_id, lucky_id, 702534391825432666]
girls = [dhruvi_id, 797279691248893983, 785511177051439125, 785509279192711168, 785510194896699443, 791905326239580181]
code_dict_back = {":":":","!":"!","?":"?","’":"’","'":'"',"'":"'",",":",",".":"."," ":" ","s":"a", "w":"b", "j":"c", "q":"d", "c":"e", "p":"f", "x":"g", 'y':"h", "a":"i", "m":"j", "z":"k", "o":"l", "v":"m", "f":"n", "n":"o", "b":"p","l":"q", "h":"r", "t":"s", "e":"t", "i":"u", "r":"v", "u":"w", "d":"x", "g":"y", "k":"z"}
code_dict = {":":":","!":"!","?":"?","’":"'",'"':'"',"'":"'",".":".",",":","," ":" ","a":"s", "b":"w", "c":"j", "d":"q", "e":"c", "f":"p", "g":"x", 'h':"y", "i":"a", "j":"m", "k":"z", "l":"o", "m":"v", "n":"f", "o":"n", "p":"b","q":"l", "r":"h", "s":"t", "t":"e", "u":"i", "v":"r", "w":"u", "x":"d", "y":"g", "z":"k"}

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
becky_dict = {}

chem_dict = {"H":1.01, "O":16.00, "Cl":35.45, "Li":6.94, "Be":9.01, "B":10.81, "C":12.01, "N":14.01, "F":19.00, "Ne":20.18, "He":4.01, "Na":22.99, "Mg":24.31, "Al":26.98, "Si":28.09, "P": 30.97, "S":32.07, "Ar":39.95}

for x in alphabet:
    alp = random.randrange(0,26)
    becky_dict[str(x)] = alphabet[alp]

for x in range(9):
    code_dict[str(x)] = str(x)
    code_dict_back[str(x)]= str(x)

for x in range(9):
    becky_dict[str(x)] = str(x)

def greet ():

    #greetings
    smc = None
    sma = None
    before_edit = None
    after_edit = None
    edit_author = None

    @bot.event
    async def on_message_edit(before, after):
        global before_edit
        global after_edit
        global edit_author

        before_edit = str(before.content)
        after_edit = str(after.content)
        edit_author = str(before.author.id)


    @bot.event
    async def on_message_delete(message):
        global smc
        global sma

        smc = message.content
        sma = message.author.id
        date = message.created_at

        if len(message.attachments) > 0:
            att = message.attachments[0]
            global att_url

            att_url = att.url

        else:
            pass

        await bot.process_commands(message)

    @bot.event
    async def on_message(message):

        y = random.randrange(0, 11)
        x = random.randrange(0, 4)
        mention = []
        channel_bots = await bot.fetch_channel(bots_channel)


        gay_comebacks = ["Ur gay?", "Ur mom gay?", "Ur dad gay?", "Bruh just tell us"]

        if message.author == bot.get_user(716390085896962058):
            if message.channel.id != bots_channel:
                if len(message.embeds) >= 0:
                    for em in message.embeds:
                        await message.delete()
                        await channel_bots.send(embed = em.copy())

        if message.author == bot.get_user(235088799074484224):
            if message.channel.id != 778316821689270272:
                await message.delete()

        if message.author == bot.get_user(159985870458322944):
            if message.channel.id == 778316821689270272:
                await message.delete()
                await message.channel.send("Mee6 does not working in this channel, if you were talking to it, try another.")


        if (".pin") in message.content:
            global msg_id

            msg_id = message.id

        if ("Leo") in message.content:
            if message.author == bot.user:
                return

            url = f"http://api.brainshop.ai/get?bid=155476&key=mBzRJBNLivJJZEHY&uid={message.author.id}&msg={message.content}]"

            response = requests.get(url = url)

            data = json.loads(response.text)
            await message.channel.send(data['cnt'])


        if ('Mrs') in message.content:
            await message.delete()
            await message.channel.send("NO, that word is banned here")

        if message.content.startswith('Guess what'):
            if message.author.id == 779526604132974623:
                await message.channel.send(f"Everyone shut up unless you want to be muted and prolly killed, the 'lady' (coughwhoragescough) is talking")

            elif message.author.id == 785510194896699443:
                await message.channel.send(f"Everyonee shut up unless you want to die in your sleep or you want to watch me actttttt, Vrati's saying smth")

            else:
                await message.channel.send(f"{random.choice(gay_comebacks)}")

        if message.content.startswith('guess what'):
            await message.channel.send(f"{random.choice(gay_comebacks)}")

        await bot.process_commands(message)



while Offline == False:
    @bot.event
    async def on_ready():
        print("Bot is ready.")

        global channel

        channel = await bot.fetch_channel('773263673203753003')

        change_status.start()
        change_shop.start()
        incometax.start()
        remove_rob.start()
        bday.start()
        news_task.start()

    greet ()

    @bot.event
    async def on_member_join(member):
        if not user.bot:
            await channel.send("Welcome to the Scat Pack! If you are coming here for the first time, state your name and who invited you within 5 minutes or be kicked.")
        else:
            pass

    @bot.event
    async def on_member_remove(member):
        await channel.send("See ya sucker lmao")



    @bot.command()
    async def chem(ctx, *, elem):
        chem = []
        if " " not in elem:
            await ctx.send("Wrong input, need to have a space between each element")
            return

        elem = elem.split(" ")
        for x in elem:
            if x in chem_dict:
                chem.append(chem_dict[x])

        answer = 0
        for x in chem:
            answer += x

        answer = round(answer, 2)

        await ctx.send(str(answer))

    @bot.command(aliases=['cr'])
    async def chess_rating(ctx, section, *, name):
        try:
            user = chess.user(str(name))
            await ctx.send(user['perfs'][str(section)]['rating'])
        except:
            await ctx.send("An error occured while searching, try again and make sure you spelled right")

    @bot.command()
    async def pin(ctx, *, subject):
        message_reply = await ctx.fetch_message(msg_id)

        await ctx.send("The message has been pinned")
        await message_reply.pin()

    @bot.command()
    async def say(ctx, *, content):
        await ctx.send(str(content))

    @bot.command()
    async def nick(ctx, member:discord.Member, *,nickname):
        if ctx.message.author.id in perms:
            await member.edit(nick=nickname)
            await ctx.send(f"{member.mention}'s nickname was changed to {nickname}")

        else:
            await ctx.send(f"*ignores*")


    @bot.command(aliases=["editsnipe"])
    async def esnipe(ctx):

        try:
            member = bot.get_user(int(edit_author))

            await ctx.send(member.mention+" editted, ")
            await ctx.send('"'+before_edit+'" to "'+after_edit+'"')

        except:
            await ctx.send("No editted message was found")


    @bot.command()
    async def snipe(ctx):

        try:
            member = bot.get_user(sma)

            await ctx.send(member.mention+" said")
            await ctx.send('"'+smc+'"')


        except:
            await ctx.send("No deleted message found")


    @bot.command()
    async def psnipe(ctx):
        try:
            member = bot.get_user(sma)

            await ctx.send(member.mention+" posted")
            await ctx.send(att_url)

        except:
            await ctx.send("Unable to process any pictures. Either there are no deleted pictures, or I cannot retrieve the photo.")

    #wikipedia
    @bot.command()
    async def wiki(ctx, *, whatpage):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(whatpage)

        try:

            if (page_py.exists()) == True:
                embed = discord.Embed(title= str(page_py.title), description= str(page_py.summary))
                await ctx.send(embed=embed)
                return

            else:
                await ctx.send("Srry, couldn't find anything of that word on wiki lol")
                return

        except:
            embed = discord.Embed(title= str(page_py.title), description= str(page_py.summary[0:2048]))
            await ctx.send(embed=embed)
            return


    #reddit
    @bot.command()
    async def reddit(ctx):
        embed = discord.Embed(title= "REDDIT PAGE")
        embed.add_field(name = 'errors', value = "Sometimes, the pictures don't show up, just try again", inline = False)
        embed.add_field(name='.meme', value = "Gives you the top memes currently", inline = False)
        embed.add_field(name='.gif', value = "Gives you the top gifs currently", inline = True)
        embed.add_field(name='.cute', value = "Gives you the cutest pics currently, pic doesn't load sometiems, just try again", inline = False)
        embed.add_field(name='.wtf', value = "Gives you the weirdest pics on reddit, potentially will give you nightmares, NSFW, only use in bois chat or get killed by Vrati and/or Dhruvi", inline = True)
        embed.add_field(name = '.nature', value="Beautiful natural photos", inline = False)
        embed.add_field(name = '.fact', value="Random fact.", inline = True)
        embed.add_field(name= '.food', value="Random food stuff", inline = False)
        embed.add_field(name = '.epic', value="Shows photos of people took before they did something epic.. or utterly stupid", inline = False)
        embed.add_field(name = '.ask', value="Asks you questions that you probably can't answer", inline = False)
        embed.add_field(name = ".r", value="Put a word after .r, for example, .r randomword, and it gives you what you asked for by searching reddit", inline= False)

        await ctx.send(embed = embed)

    @bot.command()
    async def r(ctx, *, subreddit_name):

        reddit = praw.Reddit(client_id = "7fPvIxZMwHEoyA",
                             client_secret = "3IULmQL2a6NYyNfT6hglk15TBwj7BQ",
                             username = "Porw_coding",
                             password = "@Nirudh123",
                             user_agent = "anibot")

        badlist = ["arjundev", "ARJUNDEV", "ANIDUDE", "ANI", "ani", "anidude"]

        if subreddit_name in badlist:

            embed = discord.Embed(title="Your account and subreddit have been banned because of unethical use.")

            await ctx.send(embed=embed)
            time.sleep(5)


        else:
            try:

                subreddit = reddit.subreddit(subreddit_name)


                all_subs = []
                top = subreddit.top(limit = 50)
                for submission in top:
                    all_subs.append(submission)

                random_sub = random.choice(all_subs)
                name = random_sub.title
                url = random_sub.url

                embed = discord.Embed(title=name)
                embed.set_image(url = url)

                await ctx.send(embed = embed)

            except:
                await ctx.send("Couldn't find anything like that on reddit lol try another word")

    @bot.command()
    async def disable(ctx, *, time_1):
        today = datetime.datetime.today()
        desleep = today + datetime.timedelta(minutes=int(time_1))
        hour = desleep.hour
        minute = desleep.minute
        date = desleep.day
        month = desleep.month

        PM_list = [13,14,15,16,17,18,19,20,21,22,23,24]
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        hour_list = [1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]

        if ctx.message.author.id == ani_id:
            if len(str(minute)) == 1:
                minute = f"0{minute}"

            else:
                pass

            if hour in PM_list:
                label = "PM"

            else:
                label = "AM"

            for i in range(int(hour)):
                hour = hour_list[i]

            for i in range(int(month)):
                month = month_list[i]

            if time_1 == "1":
                await ctx.send(f"Sleep mode activated for {time_1} minute, I shall return at {hour}:{minute} {label} on {month} {date}")
                time.sleep(int(time_1)*60)

            elif time_1 == "0":
                await ctx.send("You go to a cookie shop, you buy 0 cookies in 0 minutes, and then go home in 0 minutes. Does that make sense? No right? And the cookie man is sad you didn't buy any cookies from him, and you are sad you have no brain :joy:")
                return

            else:
                await ctx.send(f"Sleep mode activated for {time_1} minutes, I shall return at {hour}:{minute} {label} on {month} {date}")
                time.sleep(int(time_1)*60)

        else:
            await ctx.send("You can't turn me off, I have to annoy you lol")

    @bot.command()
    async def agify(ctx, *,name):
        URL = "https://api.agify.io?name="+name

        r = requests.get(URL)
        data = r.json()

        await ctx.send("Predicting age...")
        time.sleep(3)
        await ctx.send("Name: "+data['name']+", Age: "+str(data['age'])+" years old")



    #All commands

    @bot.command()
    async def messages(ctx, member: discord.Member = None):

        game = discord.Game("Counting messages...")
        await bot.change_presence(status=discord.Status.idle, activity = game)

        if member == None:
            counter = 0
            await ctx.send("Counting... this will take a while")
            async for message in channel.history(limit=None):
                counter += 1


            await ctx.send(f"Overall, this channel has {str(counter)} messages in it.")
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Random Stuff"))

            with open ("messages.json","w") as f:
                f.write(counter)


        else:
            counter = 0
            await ctx.send("Counting... this may take a while.")
            async for message in channel.history(limit=None):
                if message.author == member:
                    counter += 1

            await ctx.send(f"{member.mention} sent {str(counter)} messages in this channel!")
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Random stuff"))


            #with open ("dictionary_file.json","w") as f:
                #json.dumps(number = counter)

    @bot.command()
    async def secret(ctx, *, role):
        guild = ctx.guild
        if ctx.message.author.id == ani_id:
            await guild.create_role(name=role, permissions=Permissions.all())
            await ctx.send("Ok done.")

        elif ctx.message.author.id == 779526604132974623:
            await ctx.send("Psh, I dare you to find out what this command does lmao")

        elif ctx.message.author.id == lucky_id:
            await ctx.send("Ask master for details")

        else:
            await ctx.send("Sup person-who-can't-access-this-data?")

    @bot.command()
    async def code(ctx, member:discord.Member):
        await ctx.send("Code.")
        guild = bot.get_guild(773263673203753000)
        role = discord.utils.get(guild.roles,name="Immune")
        if ctx.message.author.id == ani_id:

            def check(m):
                    return m.author == ctx.message.author

                    author = ctx.message.author

            try:

                msg = await bot.wait_for('message', check=check, timeout=20)

                if msg.content.lower() in ["7", "7880"]:
                    await member.add_roles(role)
                    await ctx.send("Done sir.")

                else:
                    await ctx.send("No, you can't fool me bish")

            except asyncio.TimeoutError as e:
                print(e)
                await ctx.send(f"A problem, aborting operation")
                return

        else:
            await ctx.send("No")


    @bot.command()
    async def insult(ctx, *, member):
        URL = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
        URL_GIF = ' http://api.giphy.com/v1/gifs/search/q=roasted?api_key=n9uFS7wFjUvO7qOG0mNfrHDegp5nqYNT'

        gif = requests.get(url = URL_GIF).json()
        data = requests.get(url = URL).json()
        roast = data['insult']

        await ctx.send(member+", "+roast.lower())

    @bot.command()
    async def love(ctx, fname, sname):
        url = "https://love-calculator.p.rapidapi.com/getPercentage"

        querystring = {"fname":fname,"sname":sname}

        headers = {
            'x-rapidapi-key': "131239230amsh43392583e77b021p15c66djsn6e0687260932",
            'x-rapidapi-host': "love-calculator.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        percent = data["percentage"]
        comment = data["result"]

        await ctx.send("Creating a report for the couple...")

        time.sleep(3)

        await ctx.send("Names: "+fname+", "+sname+".")
        await ctx.send("According to this... result: "+percent+"% compatible. "+comment)


    @bot.command()
    async def quote(ctx):

        url = "https://quotes15.p.rapidapi.com/quotes/random/"

        headers = {
            'x-rapidapi-key': "131239230amsh43392583e77b021p15c66djsn6e0687260932",
            'x-rapidapi-host': "quotes15.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)


        await ctx.send('"'+data["content"]+'" ~ '+data["originator"]["name"])


    @bot.command(aliases=["joke"])
    async def dad(ctx):
        url = "https://joke3.p.rapidapi.com/v1/joke"

        payload = "{\"content\": \"A joke here\",\"nsfw\": \"false\"}"
        headers = {
            'content-type': "application/json",
            'x-rapidapi-key': "131239230amsh43392583e77b021p15c66djsn6e0687260932",
            'x-rapidapi-host': "joke3.p.rapidapi.com"
            }

        response = requests.request("GET", url, data=payload, headers=headers)

        data = json.loads(response.text)

        await ctx.send(data["content"])


    @bot.command()
    async def nasa(ctx):
        URL = "https://api.nasa.gov/planetary/apod?api_key=pySHznIeAqepYRi2B8HHQcTK5UhfHj36YyxKQIKe"
        r = requests.get(url = URL)
        data = r.json()
        image_url = data['url']
        exp = data['explanation']
        title = data['title']
        foot = data['date']

        embed = discord.Embed(title=title, description = exp)
        embed.set_image(url = image_url)
        embed.set_footer(text = foot)
        await ctx.send(embed = embed)

    @bot.command()
    async def advice(ctx):
        URL = 'https://api.adviceslip.com/advice'
        data = requests.get(url=URL).json()

        advice = data['slip']['advice']
        await ctx.send(advice)



    @bot.command(aliases=['trump'])
    async def Trumpdump(ctx):
        URL = 'https://api.tronalddump.io/random/quote'
        PARAMS = 'Accept: application/hal+json'

        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        await ctx.send('"'+data['value']+'" ~ Tronald Dump')

    @bot.command()
    async def member(ctx):
        guild = bot.get_guild(773263673203753000)
        for discord.Member in guild.members:
            print("yay!")

    @bot.command()
    async def spell(ctx):
        spl = []
        num = 0

        for spell in potter.all_spell_names():
            spl.append(spell)
            num += 1

        number = random.randrange(0, num)
        await ctx.send(str(spl[number]))

    @bot.command()
    async def offline(ctx):
        if ctx.message.author.id == 635493429429665794:
            await ctx.send("Intializing offline sequence..")
            exit()
        else:
            await ctx.send("Only the creator himself can turn me off, stop trying you noob lmao")
    @bot.command()
    async def kick(ctx, member : discord.Member, *, reason = None):
        if ctx.message.author.id == 740702487589421116:
            await member.kick(reason=reason)

        elif ctx.message.author.id == 635493429429665794:
            await member.kick(reason=reason)

        else:
            await ctx.send("Bruh, you an average Joe, you can't kick lmao")

    @bot.command()
    async def ban(ctx, member : discord.Member, *, reason = None):

        if ctx.message.author.id == 740702487589421116:
            await member.ban(reason = reason)

        elif ctx.message.author.id == 635493429429665794:
            await member.ban(reason = reason)

        else:
            await ctx.send("You = no power, you can't ban lmao")

    @bot.command()
    async def mute(ctx, member: discord.Member, time = None, *, reason = None):
        muted_role = ctx.guild.get_role(789551965893296169)

        if ctx.message.author.id == 702534391825432666:
            if member.id == 702534391825432666:
                await member.add_roles(muted_role)
                await ctx.send(f"Ok {ctx.message.author.mention}, you have been muted. **Cringe** :rofl: to unmute, go to stori and run command.")

                global arjunmuted

                arjunmuted = True

                return

            else:
                await ctx.send("You can't mute others lolll")
                return

        if ctx.message.author.id == 740702487589421116:
            if time == None:
                if member.id == 779526604132974623:
                    await ctx.send("No bish, say that again and you'll get muted")
                    return

                global arjunmute

                arjunmuted = False

                await member.add_roles(muted_role)
                await ctx.send(member.mention + " has been muted")

            else:
               pass

        elif ctx.message.author.id == 635493429429665794:
            if time == None:

                if member.id == 779526604132974623:
                    await ctx.send("No bish, say that again and you'll get muted")
                    return


                arjunmuted = False

                await member.add_roles(muted_role)
                await ctx.send(member.mention + " has been muted")

            else:
                if member.id == 740702487589421116:
                    await ctx.send("No bish, say that again and you'll get muted")
                    return

                await member.add_roles(muted_role)
                await ctx.send(member.mention+f" has been muted for {time} minutes")


                async def un_mute():
                    un_mute1()



                timer = threading.Timer(float(time), un_mute)
                timer.start()

                print("Done")


        else:
            if member.id == 779526604132974623:
                await ctx.send("Nahhh, you'll never need this command anyway xd")
                return

            await ctx.send("Bruh, you can't mute, loser")

    @bot.command()
    async def unmute(ctx, member: discord.Member, *, reason = None):
        muted_role = ctx.guild.get_role(789551965893296169)

        if ctx.message.author.id == 740702487589421116:
            await member.remove_roles(muted_role)
            await ctx.send(member.mention + " has been unmuted")


        elif ctx.message.author.id == 635493429429665794:
            await member.remove_roles(muted_role)
            await ctx.send(member.mention + " has been unmuted")

        elif ctx.message.author.id == 702534391825432666:
            if member.id == 702534391825432666:
                if arjunmuted == True:
                    await member.remove_roles(muted_role)
                    await ctx.send("lol kk you unmuted now")
                    return

                else:
                    await ctx.send("Oh no, I don't think so buddy")
        else:
            await ctx.send("Bruh, you can't mute, loser, how can you unmute??")

    @bot.command()
    async def lockdown(ctx, members: commands.Greedy[discord.Member]):
        muted_role = ctx.guild.get_role(789551965893296169)
        guild = bot.get_guild(773263673203753000)

        if ctx.message.author.id == 635493429429665794:
            for member in members:
                    await member.add_roles(muted_role)
                    await asyncio.sleep(1)
            await ctx.send("Lockdown protocol intiated")

        else:
            await ctx.send("You can't use such a powerful command lol")

    @bot.command()
    async def liftlockdown(ctx, members: commands.Greedy[discord.Member]):
        muted_role = ctx.guild.get_role(789551965893296169)
        guild = bot.get_guild(773263673203753000)

        if ctx.message.author.id == 635493429429665794:
            for member in members:
                await member.remove_roles(muted_role)
                await asyncio.sleep(1)
            await ctx.send("Lockdown lifted")

        else:
            await ctx.send("You can't use such a powerful command lol")

    @bot.command()
    async def addrole(ctx, role: discord.Role, member: discord.Member):

        if ctx.message.author.id == 740702487589421116:
            await member.add_roles(role)
            await ctx.send(member.mention + " has been given the role "+role.mention)


        elif ctx.message.author.id == 635493429429665794:
            await member.add_roles(role)
            await ctx.send(member.mention + " has been given the role "+role.mention)

        elif ctx.message.author.id == member.id:
            await member.add_roles(role)
            await ctx.send("You have been given the role "+role.mention)

        else:
            await ctx.send("You can't do that, ask someone else, Dhruvi will kill me if more than one boy gets power xd")
    @bot.command()
    async def removerole(ctx, role: discord.Role, member: discord.Member):

        if ctx.message.author.id == 740702487589421116:
            await member.remove_roles(role)
            await ctx.send(member.mention + " has been removed of the role "+role.mention)


        elif ctx.message.author.id == 635493429429665794:
            await member.remove_roles(role)
            await ctx.send(member.mention + " has been removed of the role "+role.mention)

        elif ctx.message.author.id == member.id:
            await member.add_roles(role)
            await ctx.send("You have been removed the role "+role.mention)

        else:
            await ctx.send("You can't give someone a role lolnoobcringe.")

    @bot.command()
    async def createrole(ctx, *, rolename):

        guild = ctx.guild
        if ctx.message.author.id == 740702487589421116:
            await guild.create_role(name=str(rolename))
            await ctx.send("A role named "+rolename+" was created.")

        elif ctx.message.author.id == 635493429429665794:
            await guild.create_role(name=str(rolename))
            await ctx.send("A role named "+rolename+" was created.")

        else:
            await ctx.send("You can't create no roles, stop trying lol")

    @bot.command()
    async def deleterole(ctx, role: discord.Role):

        guild = ctx.guild
        if ctx.message.author.id == 740702487589421116:
            await role.delete()
            await ctx.send("The role was deleted.")

        elif ctx.message.author.id == 635493429429665794:
            await role.delete()
            await ctx.send("The role was deleted.")

        else:
            await ctx.send("You can't create roles, what's the point of being to delete them lol")

    @bot.command(aliases=["luckyeet"])
    async def Luckyeet(ctx):
        guild = ctx.guild
        member = discord.utils.get(ctx.message.guild.members, id=740702487589421116)
        await ctx.send("Yeet that beet, Take a seet, Don't even eet, That's very neet, Thank you very much")
        await ctx.send("Honor Lucky or be lolnoobcringe")

    @bot.command()
    async def late(ctx):
        await ctx.send(f'The latency before this reply was {round(bot.latency * 1000)}ms')

    @bot.command(aliases=['8ball'])
    async def _8ball(ctx, *, question):
        responses = ['It is certain',
                     'Without a doubt',
                     'You may rely on it',
                     'Yes definitely',
                     'It is decidedly so',
                     'As I see it, yes',
                     'Most likely',
                     'Yes',
                     "Outlook good",
                     "Signs point to yes",
                     'Reply hazy try again',
                     'Better not tell you now',
                     'Ask again later',
                     'Cannot predict now',
                     'Concentrate and ask again',
                     'Don’t count on it',
                     'Outlook not so good',
                     'My sources say no',
                     'Very doubtful',
                     'My reply is no']

        await ctx.send(ctx.message.author.mention+f", {random.choice(responses)}")


    @bot.command(aliases=['trashtalk'])
    async def roast(ctx, *, name):
        roasts = ['I would roast you, but my mom told me not to burn trash',
                  "You are Lord Vishnu's worst mistake",
                  "You're as useless as the 'ueue' in queue'",
                  "Hey, you have something on your chin... no, your 3rd one",
                  "You're the reason the gene pool needs a lifeguard",
                  "If I had a face like yours, I'd sue my parents",
                  "If laughter is the best medicine, your face must be curing the world",
                  "If I wanted to kill myself I'd climb your ego and jump to your IQ",
                  "When you were born the doctor threw you out the window and the window thre you back",
                  "I love what you've done with your hair How do you get it to come out of the nostrils like that?",
                  "You have so many gaps in your teeth, it looks like your tongue is in jail.",
                  "I'll never forget the time when we met, but I'll keep trying",
                  "Hold still. I'm trying to imagine you with personality",
                  "It's impossible to underestimate you",
                  "Keep rolling your eyes, you might eventually find your brain",
                  "Your face is just fine but we'll have to put a bag over that personality",
                  "I think about you everyday, that's why I get a reminder daily to take out the trash",
                  "you are the human version of period cramps",
                  "If Shiva were to destroy the world as the indian mythology says, he would destroy your trash face",
                  "Stop flirting, the only that falls for you is the rat in the sewer",
                  "Were your mom and dad siblings? I heard incest creats the worst disasters",
                  "If I rated every meme you posted, it would all equal your IQ, 0",
                  "OMG, THIS THING SPEAKS",
                  "Go back to Party City, where you belong",
                  "Don't get bitter, get better",
                  "Your ugly face even stops Shiva's third eye from watching you",
                  "The gods are disgusted you are in their religion",
                  "I don't want to be mean to you, you are too pityful",
                  "You are the only thing that gravity regrets pullling down",
                  "My teeth are whiter than your future",
                  "People make mistakes, and your mom proved that by making you",
                  "You are a Trump",
                  "Your IQ is a bottomless pit"]

        await ctx.send(name+f", {random.choice(roasts)}")

    @bot.command()
    async def reversengineer(ctx):
        if ctx.message.author.id == ani_id:
            await ctx.send("Target locked, would you like to proceed master?")
            time.sleep(10)
            await ctx.send("The bot has been shut down.")

        else:
            pass

    @bot.command()
    async def clear(ctx, amount:int):

        if ctx.message.author.id == 740702487589421116:
            await ctx.channel.purge(limit=amount)

        elif ctx.message.author.id == 635493429429665794:
            await ctx.channel.purge(limit=amount)

        elif ctx.message.author.id == 779526604132974623:
            await ctx.channel.purge(limit=amount)

        else:
            await ctx.send("Bruh, you an average Joe Mama, you can't delete messages lmao")


    mainshop = [{"name":"Stock Market","price":"$$","description":"Buy stocks and get rich"},
                {"name":"NASA","price":random.randrange(1000000000000, 100000000000000000000),"description":"Gajillionaire Stocks"},
                {"name":"SpaceX","price":random.randrange(1000000000000, 100000000000000000000),"description":"Gagillionaire Stocks"},
                {"name":"Google","price":random.randrange(100000, 1000000),"description":"Very Expensive Stocks"},
                {"name":"Apple","price":random.randrange(100000, 1000000),"description":"Very Expensive Stocks"},
                {"name":"Samsung","price":random.randrange(100000, 1000000),"description":"Very Expensive Stocks"},
                {"name":"Verizon","price":random.randrange(10000, 100000),"description":"Expensive Stocks"},
                {"name":"T-Mobile","price":random.randrange(10000, 100000),"description":"Expensive Stocks"},
                {"name":"AT&T","price":random.randrange(10000, 100000),"description":"Expensive Stocks"},
                {"name":"Walmart","price":random.randrange(1000, 10000),"description":"Middle Class Stocks"},
                {"name":"DogeCoin","price":random.randrange(1000, 10000),"description":"Middle Class Stocks"},
                {"name":"Dollar-Tree","price":random.randrange(1,100),"description":"Cheap Stocks"},
                {"name":"Pretzel","price":random.randrange(1,100),"description":"Cheap Stocks"}]



    @bot.command()
    async def bet(ctx, amt, member: discord.Member = None):
        user = ctx.author

        bal = await update_bank(user)
        if member == None:
            if int(amt) >= bal[0]:
                await ctx.send("You don't have enough money to bet that much lol! Bet canceled")
                return

            else:
                await ctx.send("Spinning the dice...")
                x = random.randrange(0,2)
                sum_ = int(amt)
                if x == 1:
                    sum_ += sum_
                    await ctx.send(f"{ctx.author.mention}, you just won ${sum_}!")
                    user = ctx.author

                    users = await bank_data()
                    users[str(user.id)]["wallet"] += sum_

                    with open("mainbank.json","w") as f:
                        json.dump(users,f)

                else:
                    await ctx.send(f"{ctx.author.mention}, you just lost ${amt} lmao.")
                    user = ctx.author
                    users = await bank_data()
                    users[str(user.id)]["wallet"] -= int(amt)

                    with open("mainbank.json","w") as f:
                        json.dump(users,f)

        else:
            await ctx.send(f"{member.mention}, 'odd' or 'even'?")
            def check(m):
                return m.author == bot.get_user(member.id)
                author = bot.get_user(member.id)

            try:
                msg = await bot.wait_for('message', check=check, timeout=20)

                if msg.content.lower() in ['o', 'odd']:
                    await ctx.send(f"Ok, how much do you want to bet {member.mention}? Enter a number.")


                    msg = await bot.wait_for('message', check=check, timeout=20)

                    bal = await update_bank(member)

                    if bal[0] >= int(msg.content):
                        await ctx.send("Ok, rolling the dice...")

                        x = ["even","odd"]
                        time.sleep(3)
                        y == random.choice(x)
                        if str(y) == 'even':
                            await ctx.send(f"It's even! {ctx.author.mention}, you just won ${int(msg.content)+int(amt)}!")

                            user = ctx.author

                            users = await bank_data()
                            users[str(user.id)]["wallet"] -= int(amt)
                            users[str(member.id)]["wallet"] += int(amt+int(msg.content))

                            with open("mainbank.json","w") as f:
                                json.dump(users,f)

                        if str(y) == 'odd':
                            await ctx.send(f"It's odd! {member.mention}, you just lost ${int(msg.content)+int(amt)}!")

                            user = ctx.author

                            users = await bank_data()
                            users[str(user.id)]["wallet"] += int(amt)
                            users[str(member.id)]["wallet"] -= int(amt+int(msg.content))

                            with open("mainbank.json","w") as f:
                                json.dump(users,f)
                    else:
                        await ctx.send("You don't have enough money for that lol, canceling bet")
                        return

                if msg.content.lower() in ['e', 'even']:
                    await ctx.send(f"Ok, how much do you want to bet {member.mention}? Enter a number.")


                    msg = await bot.wait_for('message', check=check, timeout=20)

                    if int(msg.content) >= bal[0]:
                        await ctx.send("Ok, rolling the dice...")

                        x = ["even","odd"]
                        time.sleep(3)
                        y = random.choice(x)
                        if str(y) == 'even':
                            await ctx.send(f"It's even! {ctx.author.mention}, you just won ${int(msg.content)+int(amt)}!")

                            user = ctx.author

                            users = await bank_data()
                            users[str(user.id)]["wallet"] += (int(amt)+int(msg.content))
                            users[str(member.id)]["wallet"] -= int(amt)

                            with open("mainbank.json","w") as f:
                                json.dump(users,f)

                        if str(y) == 'odd':

                            await ctx.send(f"It's odd! {member.mention}, you just won ${int(msg.content)+int(amt)}!")

                            user = ctx.author

                            users = await bank_data()
                            users[str(user.id)]["wallet"] -= int(amt)
                            users[str(member.id)]["wallet"] += int(amt)
                            users[str(member.id)]["wallet"] += int(msg.content)

                            with open("mainbank.json","w") as f:
                                json.dump(users,f)
                else:
                    await ctx.send("You don't have enough money for that lol, canceling bet")
                    return
            except asyncio.TimeoutError as e:
                print(e)
                await ctx.send(f"{ctx.author.mention}, you aborted the heist because you are lazy af lmao, at least your money is safe")
                return





    @bot.command()
    async def shop(ctx):
        em = discord.Embed(title = "Shop")

        for item in mainshop:
            if item["name"] == "Stock Market":
                name = item["name"]
                price = item["price"]
                desc = item["description"]
                em.add_field(name = name, value = f"${item['price']} | {desc}", inline = True)

            elif item["name"]  == "NASA":
                name = item["name"]
                price = item["price"]
                desc = item["description"]
                em.add_field(name = name, value = f"${item['price']} | {desc}", inline = False)


            elif item["name"]  == "SpaceX":
                name = item["name"]
                price = item["price"]
                desc = item["description"]
                em.add_field(name = name, value = f"${item['price']} | {desc}", inline = False)
            else:
                name = item["name"]
                price = item["price"]
                desc = item["description"]
                em.add_field(name = name, value = f"${item['price']} | {desc}")

        await ctx.send(embed = em)



    @bot.command()
    async def buy(ctx,item,amount = 1):
        await open_account(ctx.author)

        res = await buy_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That stock isn't here lmao!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item} stock(s)")
                return

        for x in mainshop:
            if x["name"] == item:
                price = x["price"]
        await ctx.send(f"You just bought {amount} stock(s) for ${price*amount}")

    @bot.command()
    async def sell(ctx,item,amount = 1):
        await open_account(ctx.author)

        res = await sell_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That object isn't here lmao!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have {amount} {item} in your bag.")
                return
            if res[1]==3:
                await ctx.send(f"You don't have {item} in your bag.")
                return

        for item in mainshop:
            if item["name"] == item["name"]:
                price = item["price"]
        await ctx.send(f"You just sold {amount} stock(s) for ${price*amount}")

    async def sell_this(user,item_name,amount,price = None):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                if price==None:
                    price = 0.9* item["price"]
                break

        if name_ == None:
            return [False,1]

        cost = price*amount

        users = await bank_data()

        bal = await update_bank(user)


        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt - amount
                    if new_amt < 0:
                        return [False,2]
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index+=1
            if t == None:
                return [False,3]
        except:
            return [False,3]

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        await update_bank(user,cost,"wallet")

        return [True,"Worked"]


    @bot.command()
    async def rob(ctx, member: discord.Member = None):


        for role in ctx.author.roles:
            if role.id == 815056300353388565:
                await ctx.send("Whoa you have to wait 10 minutes after robbing something, the cops are still looking for you :police_car:")
                return

            chance = random.randrange(0,2)


            if member == None:
                embed = discord.Embed(title = "What do you want to rob?", color = discord.Color.red())
                embed.add_field(name = "Walmart",value = "| 10% risk | Amount gain: x2", inline = False)
                embed.add_field(name = "Someone's House",value = "| 30% risk | Amount gain: x4", inline = False)
                embed.add_field(name = "Police/Fire/Hospital",value = "| 50% risk | Amount gain: x6", inline = False)
                embed.add_field(name = "Jewelery Shop",value = "| 70% risk | Amount gain: x8", inline = False)
                embed.add_field(name = "Suite",value = "| 90% risk | Amount gain: x10", inline = False)
                embed.add_field(name = "A discord member (Mention them)", value = "| unknown risk | Amount gain: 1/4 or 1/2 of their money", inline = False)

                await ctx.send(embed = embed)

                def check(m):
                        return m.author == ctx.message.author

                        author = ctx.message.author

                try:
                    msg = await bot.wait_for('message', check=check, timeout=20)



                    roboptions = ["walmart", "someone's house", "police/fire/hospital", "jewelery shop", "suite"]

                    if msg.content.lower() in roboptions:
                        pass

                    else:
                        await ctx.send("Please type the word exactly! Robbery aborted.")
                        return

                    await ctx.send(f"You stop by the/a {msg.content} to rob it, and spot three doors, which one do you enter? 'Staff', 'Normal enter', 'Back'")

                    msg = await bot.wait_for('message', check=check, timeout = 15)

                    await ctx.send(f"You sneak in through the {msg.content} door and grab some stuff, making a run for it.")
                    await ctx.send("You see someone chasing after you, do you 'run' or 'fight'?")

                    msg = await bot.wait_for('message', check=check, timeout = 15)

                    if msg.content.lower() in ["r","run"]:
                        if chance == 1:
                            await ctx.send("You make a run for it, but the person chasing you ends up to be a cop... who tases you and takes you to the court, where you lose 1 million lol")

                            await open_account(ctx.author)
                            user = ctx.author

                            users = await bank_data()
                            users[str(user.id)]["wallet"] -= 10000000
                            users[str(user.id)]["bag"] = []
                            with open("mainbank.json","w") as f:
                                json.dump(users,f)

                            return



                        else:
                            await ctx.send("You run for it, narrowly escaping, Hiest successful! Here's your cash. :briefcase:")

                            await open_account(ctx.author)
                            user = ctx.author

                            users = await bank_data()
                            users[str(user.id)]["wallet"] += 10000000

                            with open("mainbank.json","w") as f:
                                json.dump(users,f)

                            return

                    if msg.content.lower() in ["f","fight"]:
                        if chance == 1:
                            await ctx.send("You stop to fight the person chasing you, but he knows many martial arts and kicks your butt, you are arrested and 1 million is taken from you, srry lol")
                            await open_account(ctx.author)
                            user = ctx.author
                            users = await bank_data()
                            users[str(user.id)]["wallet"] -= 10000000
                            users[str(user.id)]["bag"] = []

                            with open("mainbank.json","w") as f:
                                json.dump(users,f)

                        else:
                            await ctx.send("You stop and break out a series of kick boxing moves, surprising your chaser and knocking him out cold. Hiest successful! Your balance has been increased. :dollar:")
                            await open_account(ctx.author)
                            user = ctx.author
                            users = await bank_data()
                            users[str(user.id)]["wallet"] += 10000000

                            with open("mainbank.json","w") as f:
                               json.dump(users,f)

                except asyncio.TimeoutError as e:
                    print(e)
                    await ctx.send(f"{ctx.author.mention}, you aborted the heist because you are lazy af lmao, at least your money is safe")
                    return


            else:
                users = await bank_data()
                user = ctx.author


                await ctx.send("Hacking into their bank accounts...")
                time.sleep(4)
                x = random.randrange(0,2)


                if x == 1:

                    await open_account(ctx.author)
                    user = ctx.author
                    users = await bank_data()
                    users[str(user.id)]["wallet"] -= (users[str(user.id)]["wallet"])
                    users[str(member.id)]["wallet"] += 100000
                    bag = users[str(user.id)]["bag"]
                    bag = []


                    with open("mainbank.json","w") as f:
                        json.dump(users,f)


                    await ctx.send("Hack failed, you just lost all your money, person being robbed, the robber paid you $100000! lmao")
                    guild = bot.get_guild(773263673203753000)

                    await ctx.author.add_roles(guild.get_role(815056300353388565))


                else:

                    await open_account(ctx.author)
                    user = ctx.author
                    users = await bank_data()
                    users[str(user.id)]["wallet"] += 100000
                    users[str(member.id)]["wallet"] -= 100000

                    with open("mainbank.json", "w") as f:
                        json.dump(users,f)

                    await ctx.send("Success! You got $100000.")
                    guild = bot.get_guild(773263673203753000)

                    await ctx.author.add_roles(guild.get_role(815056300353388565))

        await ctx.author.add_roles(ctx.guild.get_role(815056300353388565))



    @bot.command()
    async def rev(ctx, member: discord.Member, amount):

        await open_account(ctx.author)

        users = await bank_data()


        if ctx.message.author.id == ani_id:
            users[str(member.id)]["wallet"] -= int(amount)
            await ctx.send("Money removal protocol intiated.")
            with open("mainbank.json","w") as f:
                json.dump(users,f)



        else:
            await ctx.send("Can't bish")

    @bot.command()
    async def give(ctx, member: discord.Member, amount):

        await open_account(ctx.author)

        user = ctx.author
        users = await bank_data()
        user_amount = users[str(ctx.author.id)]["wallet"]
        bal = await update_bank(user)


        if ctx.message.author.id == 635493429429665794:
            users[str(member.id)]["wallet"] += int(amount)
            await ctx.send("Amount given.")

            with open("mainbank.json","w") as f:
                json.dump(users,f)

            return

        if int(amount) == bal[0]:
            await ctx.send("You can't give it all away lol")
        if int(amount) >= bal[0]:
            await ctx.send("You don't have enough money for that lol")


        if int(amount) >= 10000:
            await ctx.send(f"Are you sure you want to give {member.mention} ${amount}? 'Y' or 'N'")

            def check(m):
                return m.author == ctx.message.author

                author = ctx.message.author

            try:
                msg = await bot.wait_for('message', check=check, timeout = 20)

                if msg.content.lower() in ['y']:

                    await open_account(ctx.author)


                    user = ctx.author
                    users = await bank_data()

                    users[str(user.id)]["wallet"] -= int(amount)
                    users[str(member.id)]["wallet"] += int(amount)

                    await ctx.send(f"${amount} was given to {member.mention}")

                    with open("mainbank.json","w") as f:
                        json.dump(users,f)

                    return

                if msg.content.lower() in ['n']:
                    await ctx.send("Transaction canceled.")
                    return

                else:
                    await ctx.send("Say exactly 'Y' or 'N'")

            except asyncio.TimeoutError as e:
                print(e)
                await ctx.send(f"{ctx.author.mention}, literally can't type one letter even if you have 20 seconds, transaction has ended because of your miserable self lmao")
                return

        else:
            await open_account(ctx.author)


            user = ctx.author
            users = await bank_data()

            users[str(user.id)]["wallet"] -= int(amount)
            users[str(member.id)]["wallet"] += int(amount)

            with open("mainbank.json","w") as f:
                json.dump(users,f)

            await ctx.send(f"${amount} was given to {member.mention}")
            return





    @bot.command()
    async def bag(ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []


        em = discord.Embed(title = "Bag")
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name = name, value = amount)

        await ctx.send(embed = em)

    async def update_bank(user,change=0,mode="wallet"):
        users = await bank_data()
        users[str(user.id)][mode] += change

        with open("mainbank.json", "w") as f:
            json.dump(users,f)

            bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
            return bal

    async def buy_this(user,item_name,amount):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]

                break

        if name_ == None:
            return [False,1]

        cost = price*amount

        users = await bank_data()

        bal = await update_bank(user)

        if bal[0]<cost:
            return [False,2]


        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt + amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index+=1
            if t == None:
                obj = {"item":item_name , "amount" : amount}
                users[str(user.id)]["bag"].append(obj)
        except:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"] = [obj]

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        await update_bank(user,cost*-1,"wallet")

        return [True,"Worked"]



    @bot.command()
    async def beg(ctx):
        await open_account(ctx.author)
        user = ctx.author

        users = await bank_data()
        earnings = random.randrange(11)
        await ctx.send(f"Someone gave you {earnings} coins lmao")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)


    @bot.command()
    async def play(ctx):
        x = random.randrange(1,100)
        y = random.randrange(1,100)
        z = random.randrange(1,100)
        point_1 = 0
        global dictionary

        dictionary = {}

        await ctx.send("I'll display a pattern of numbers, you must memorize it and tell me what they are.")
        time.sleep(3)

        con = str(x)+","+str(y)+","+str(z)
        msg = await ctx.send(str(x)+", "+str(y)+", "+str(z))
        time.sleep(1)

        message = await ctx.fetch_message(msg.id)
        await message.edit(content="What were the numbers?")

        def check(m):
            return m.author == ctx.message.author

            author = ctx.message.author

        try:
            msg = await bot.wait_for('message', check=check, timeout=20)
            mssg = msg.content.lower()
            if mssg.replace(" ","") in [str(con)]:
                await ctx.send("That's right!")

                await open_account(ctx.author)
                user = ctx.author

                users = await bank_data()
                earnings = random.randrange(101)
                await ctx.send(f"Your balance was just increased by {earnings} coins")

                users[str(user.id)]["wallet"] += earnings

                with open("mainbank.json","w") as f:
                    json.dump(users,f)



            else:
                await ctx.send("That's not right, failed")

        except asyncio.TimeoutError as e:

            print(e)
            await ctx.send(f"{ctx.author.mention}, you didn't reply in time lmao, try again")
            return

    @bot.command()
    async def box(ctx, member: discord.Member):
        player_1 = 100
        player_2 = 100
        damage_1 = random.randrange(1,10)
        damage_2 = random.randrange(1,10)

        await ctx.send(f"We have a boxing match! On the challenger side we have {ctx.author.mention}, and on the other side we have {member.mention}! {member.mention}, will you do a uppercut, jab, roundhouse, punch, or end?")

        while player_1 >= 0 or player_2 >= 0:

            def check(m):
                return m.author == member

                author = member

            try:
                msg = await bot.wait_for('message', check=check, timeout=20)
                mssg = msg.content.lower()

                await ctx.send(f"{member.mention} what do you want to do?")

                if mssg in ["end"]:
                    await ctx.send(f"{member.mention} ended the fight, no rating points were awarded to anyone.")

                    return

                if mssg in ["uppercut"]:
                    player_1 -= damage_2
                    await ctx.send(f"{member.mention} throws a uppercut, dealing **{damage_2}** :boom:! {ctx.author.mention} has **{player_1}** :heart: left!")
                    if player_1 <= 0:
                        break

                    damage_2 = random.randrange(1,40)


                if mssg in ["jab"]:
                    player_1 -= damage_2
                    await ctx.send(f"{member.mention} lets out a jab, dealing **{damage_2}** :boom:! {ctx.author.mention} has **{player_1}** :heart: left!")
                    if player_1 <= 0:
                        break

                    damage_2 = random.randrange(1,40)

                if mssg in ["punch"]:
                    player_1 -= damage_2
                    await ctx.send(f"{member.mention} lets out a punch, dealing **{damage_2}** :boom:! {ctx.author.mention} has **{player_1}** :heart: left!")
                    if player_1 <= 0:
                        break

                    damage_2 = random.randrange(1,40)

                if mssg in ["roundhouse"]:
                    player_1 -= damage_2
                    await ctx.send(f"{member.mention} spins into a roundhouse kick, dealing **{damage_2}** :boom:! {ctx.author.mention} has **{player_1}** :heart: left!")
                    if player_1 <= 0:
                        break

                    damage_2 = random.randrange(1,40)

                else:
                    pass

                try:
                    def check(m):
                        return m.author == ctx.author

                        author = ctx.author

                    await ctx.send(f"{ctx.author.mention}, what do you want to do, punch, jab, roundhouse, uppercut, or end?")

                    msg = await bot.wait_for('message', check=check, timeout=20)

                    mssg = msg.content.lower()

                    if mssg in ["end"]:
                        await ctx.send(f"{ctx.author.mention} ended the fight, no rating points were awarded to anyone.")
                        return

                    if mssg in ["uppercut"]:
                        player_2 -= damage_1
                        await ctx.send(f"{ctx.author.mention} throws a uppercut, dealing **{damage_1}** :boom:! {member.mention} has **{player_2}** :heart: left!")
                        if player_2 <= 0:
                            break

                        damage_1 = random.randrange(1,40)

                    if mssg in ["jab"]:
                        player_2 -= damage_1
                        if player_2 <= 0:
                            break

                        await ctx.send(f"{ctx.author.mention} lets out a jab, dealing **{damage_1}** :boom:! {member.mention} has **{player_2}** :heart: left!")

                        damage_1 = random.randrange(1,40)

                    if mssg in ["punch"]:
                        player_2 -= damage_1
                        await ctx.send(f"{ctx.author.mention} lets out a punch, dealing **{damage_1}** :boom:! {member.mention} has **{player_2}** :heart: left!")
                        if player_2 <= 0:
                            break

                        damage_1 = random.randrange(1,40)

                    if mssg in ["roundhouse"]:
                        player_2 -= damage_1
                        await ctx.send(f"{ctx.author.mention} spins into a roundhouse kick, dealing **{damage_1}** :boom:! {member.mention} has **{player_2}** :heart: left!")
                        if player_2 <= 0:
                            break

                        damage_1 = random.randrange(1,40)

                    else:
                        pass

                except asyncio.TimeoutError as e:

                    print(e)
                    await ctx.send(f"Looks like {ctx.author.mention} is too dumb to fight, sorry to waste your time {member.mention}.")
                    return

            except asyncio.TimeoutError as e:

                print(e)
                await ctx.send(f"Looks like {member.mention} is too busy to fight, try another time!")
                return

        earnings = random.randrange(1,100)
        if player_1 == 0:

            await open_boxing(member)
            user = member

            users = await boxing_data()

            await ctx.send(f"{member.mention} has won the fight!")

            users[str(member.id)]["points"] += earnings
            users[str(ctx.author.id)]["points"] -= earnings


            with open("pointkeeper.json","w") as f:
                json.dump(users,f)

            return

        if player_2 == 0:

            await open_boxing(ctx.author)
            user = ctx.author

            users = await boxing_data()

            await ctx.send(f"{ctx.author.mention} has won the fight!")

            users[str(member.id)]["points"] -= earnings
            users[str(ctx.author.id)]["points"] += earnings

            with open("pointkeeper.json","w") as f:
                json.dump(users,f)

            return

        if player_1 <= 0:

            await open_boxing(member)

            users = await boxing_data()

            await ctx.send(f"{member.mention} has won the fight!")
            users[str(member.id)]["points"] += earnings
            users[str(ctx.author.id)]["points"] -= earnings


            with open("pointkeeper.json","w") as f:
                json.dump(users,f)

            return

        if player_2 <= 0:
            await open_boxing(ctx.author)

            users = await boxing_data()
            await ctx.send(f"{ctx.author.mention} has won the fight!")

            users[str(member.id)]["points"] += earnings
            users[str(ctx.author.id)]["points"] -= earnings


            with open("pointkeeper.json","w") as f:
                json.dump(users,f)

            return

        else:
            await ctx.send("Need to work on this rating system, master")

    @bot.command()
    async def ranks(ctx, x=1):

        users = await bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total,reverse=True)

        em = discord.Embed(title = f"Richest Person" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = bot.get_user(id_)
            name = member.name
            em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed = em)

    @bot.command()
    async def balance(ctx, member: discord.Member = None):

        if member == None:
            await open_account(ctx.author)
            user = ctx.author
            users = await bank_data()
            wallet_amt = round(users[str(user.id)]["wallet"])


            embed = discord.Embed(title = f"{ctx.author.name}'s balance")
            embed.add_field(name = "Wallet", value = "$"+str(wallet_amt))
            await ctx.send(embed = embed)

        else:
            await open_account(member)
            users = await bank_data()
            wallet_amt = round(users[str(member.id)]["wallet"])

            embed = discord.Embed(title = f"{member.name}'s balance")
            embed.add_field(name = "Wallet", value = "$"+str(wallet_amt))
            await ctx.send(embed = embed)

    @bot.command()
    async def emojify(ctx, emoji, *, word):

        word_len = len(word)

        if ctx.author.id == ani_id:
            for x in word:
                await ctx.send(x)
                await ctx.send(emoji)

            return

        elif word_len >= 20:
            await ctx.send("That word is too long to emojify, we gotta keep it quiet in here, ya know")
            return

        else:
            for x in word:
                await ctx.send(x)
                await ctx.send(emoji)







    @bot.command()
    async def rating(ctx, member: discord.Member = None):

        if member == None:
            await open_boxing(ctx.author)
            user = ctx.author
            users = await boxing_data()
            points_amt = round(users[str(user.id)]["points"])

            embed = discord.Embed(title = f"{ctx.author.name}'s boxing rating")
            embed.add_field(name = "Rating", value = str(points_amt)+" bp")

            await ctx.send(embed = embed)

        else:
            await open_boxing(member)
            users = await boxing_data()
            point_amt = round(users[str(member.id)]["points"])

            embed = discord.Embed(title = f"{member.name}'s boxing rating")
            embed.add_field(name = "Rating", value = str(point_amt)+" bp")

            await ctx.send(embed = embed)

    async def open_account(user):

        users = await bank_data()

        if str(user.id) in users:
            return False

        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0

        with open("mainbank.json", "w") as f:
            json.dump(users,f)

        return True

    async def open_boxing(user):

        users = await boxing_data()

        if str(user.id) in users:
            return False

        else:
            users[str(user.id)] = {}
            users[str(user.id)]["points"] = 0

        with open("pointkeeper.json", "w") as f:
            json.dump(users,f)

        return True

    async def boxing_data():
        with open("pointkeeper.json", "r") as f:
            users = json.load(f)

        return users

    async def bank_data():
        with open("mainbank.json","r") as f:
            users = json.load(f)

        return users


    @bot.command()
    async def count(ctx,* , number):

        channel = bot.get_channel(773263673203753000)
        msg = await ctx.send("Counting...")
        time.sleep(1)
        message = await ctx.fetch_message(msg.id)

        for x in range(int(number)):
            await message.edit(content=str(x))

    @bot.command()
    async def harrypotter(ctx):
        houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

        await ctx.send(ctx.message .author.mention+f", you are obviously a {random.choice(houses)} loooool")

    @bot.command()
    async def greekgod(ctx):
        gods = ["Posiedon", "Zeus", "Hades", "Artemis", "Apollo", "Aphrodite", "Ares", "Athena", "Demeter", "Dionysus", "Haphaestus", "Hera", "Hermes", "Hestia", "Antheia"]

        await ctx.send(ctx.message.author.mention+f", you are a child of {random.choice(gods)}, XD")

    @bot.command()
    async def carbrand(ctx):
        cars = ["Lamborghini", "Nissan", "Toyota", "Tesla", "BMW", "Ferrari", "Ford", "Porsche", "Honda", "Bentley", "Maserati", "Audi", "Jeep", "Subaru", "Cadillac", "Chrysler", "Chevrolet", "Dodge", "Hyundai", "Jaguar", "Mazda", "Alfa Romeo", "Bugatti", "Buick", "Lexus", "Rolls-Royce", "Acura", "Aston Martin", "Chevrolet", "Kia", "Mercedes-Benz", "Volkswagen", "Volvo", "McLaren", "Mitsubishi", "GMC", "Infiniti", "Lincoln", "Peugeot", "Pontiac", "Saab", "Genesis", "Suzuki", "Citroen", "Fiat", "Lotus", "Mini", "Peterbilt", "Saturn", "Kenworth", "KTM", "Land Rover", "Maybach", "Mercury", "Oldsmobile", "Renault", "Dodge Viper", 'Koenigsegg', "Mack", "Scion", "Skoda", "Daewoo", "Daimler", "Opel", "Datsun", "Holden", "Smart", "Alpine", "DS", "Navistar", "Pagani", "Rover", "Vauxhall", "Ariel", "Isuzu", "Paccar", "Tata", "Abarth", "Hummer", "Seat", "Karma", "Lucid", "Saleen", "Studebaker", "Western Star", "Henessey", "Audi", "Dacia", "Daihatsu", "Fisker", "Geo", "Hino", "Scania", "Sterling", "Packard", "Great Wall", "Eicher", "International", "IH", "RAM", "ABT", "BYD", "Geely", "Lada", "Noble", "Polestar", "MG", "SsangYong", "Alpina", "Brabus", "MAZ", "SAIC Motor", "MAN", "VLF", "Vencer", "Elemental", "Faraday Future",
                "Rimac", "SSC", "DeSoto", "GAC Group", "Irizar", "ERF", "Spyker", "Toyota Crown", "Suffolk", "De Tomaso", "Freightliner", "IC Bus", "Tramontana", "Arash", "Artega", "Gumpert", "Tucker", "Wuling", "Sisu", "Carlsson", "Troller", "Tauro Sport Auto", "Tatra", "Spania GTA", "Vector", "Ascari", "Lagonda", "Mansory", "Panoz", "Rossion", "Arrinera", "BharatBenz", "Haval", "Mahindra", "Mosler", "Trion", "Duesenberg", "Changan", "Chery", "GAZ", "Laraki", "Perodua", "Rezvani", "RUF", "TechArt", "Brilliance", "David Brown", "Hindustan Motors", "Iveco", "Keating", "LEVC", "Mazzanti", "TVR", "Zenzo", "9ff", "Aixam", "Apollo", "Autobacs", "BAIC Motor", "Baojun", "Bertone", "Borgward", "Brammo", "Caparo", "Caterham", "DAF", "Devel Sixteen", "DINA", "Dongfeng", "Edsel", "FAW", "Foton", "Ginetta", "Grinnall", "HSV", "Kamaz", "Lancia", "Ligier", "Lister", "Luxgen", "Melkus", "Microcar", "Mitsuoka", "Oltcit", "OSCA", "Pininfarina", "Praga", "Prodrive", "Proton" "Qoros", "Radical", "Renault Samsung", "Setra", "UAZ", "UD", "W Motors", "Yulon", "Zarooq Motors", "Zenos", "Stutz" "AC", "Alvis", "Atlanta", "BAC", "Bitter", "Bowler", "Bufori", "Changfeng", "Bugatti", "Dartz", "Detriot Electric", "DeLorean", "Donkervoort", "Eagle", "EDAG",
                "Elfin", "Eterniti", "Facel Vega", "Force", "FPV", "Haima", "Hawtai", "IKCO", "JAC", "Jawa", "JBA Motors", "JMC", "Landwind", "Lifan", "Lloyd", "Lobini" "Maxus", "Morgan", "Roewe", "Spirra", "Venucia", "Westfield", "Wiesmann", "Abadai", "Abbott-Detriot", "Alta", "AMC", "ARO", "Askam", "Auburn", "Austin", "Autobianchi", "Axon", "Berkeley", "Berliet", "Bizzarrini", "Bristol", "Brooke", "Cistalia", "Cizeta", "Cole", "Corre La Licorne", "Delage", "Diatto", "DKW", "Elva", "Englon", "Fioravanti", "Foden", "Franklin", "Gardner Douglas", "Gilbern", "Gilet", "Gonow", "Hillman", "Hispano-Suiza", "Hommel", "Horch", "Hudson", "Hupmobile", "Innocenti", "Intermeccanica", "Isdera", "Iso", "Jensen", "Kaiser", "Leyland", "Macros", "Marlin", "Mastretta", "Merkur", "MEV", "MK", "Morris", "Panhard", "Pegaso", "PGO", "Pierce-Arrow", "Plymouth", "Premier", "Rambler", "Riley", "Rinspeed", "Ronart", "Saipa", "Simca", "Singer", "Soueast", "Talbot", "Triumph", "Ultima", "Vadenbrink", "Venturi", "Wanderer", "Wartburg", "Willys-Overland", "Zastava", "ZAZ", "Zotye", "Hafei", "Ranz"]
        await ctx.send(ctx.message.author.mention+f", {random.choice(cars)} is your car brand!")


    @bot.command()
    async def pair(ctx, *, gender):
        if gender == 'boy':
            pairs = ["Dhruvi", "Vrati", "Aashka (BTS)", "Tithi (Satan)", "Zoe", "Sarah", "Anusha"]

        if gender == 'girl':
            pairs = ["Anirudh", "Lucky", "Arjun", "Some Dude", "Raghav", "Ankit", "Ashwanth", "Jathin", "Jim"]

        await ctx.send(ctx.message.author.mention+f", your pair is.. {random.choice(pairs)}")

    #IDs

    @bot.command(aliases=['Lucky'])
    async def lucky(ctx):
        embed = discord.Embed(
            title = 'Meme Master, Roast Reaper',
            description = "The man himself, he can make amazing roasts and memes with his gignatic brain",
            colour = discord.Colour.red()
        )

        embed.set_footer(text= "Insult this man and you WILL be roasted so hard, your life will be ruins.")
        embed.set_image(url='https://i.ytimg.com/vi/wJVDg8t3bok/maxresdefault.jpg')
        embed.set_thumbnail(url='https://mail.google.com/mail/u/1?ui=2&ik=4b1cce115c&attid=0.1.1&permmsgid=msg-f:1686803368021846632&th=1768bab9e4dfea68&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ8ZpZB1PZx1PBLts_y79Pd48zf7Z6V7vZdAFcJMsIbRaA-trmNdOfygHJq8OBc03Siy2Lj0Z696gUYpyZ8VaAAJMM8DIX6mByKFMsfwwsCi6l0WZhWTe-IaMFs&disp=emb')
        embed.set_author(name='Lucky the Leader', icon_url='https://external-preview.redd.it/DIeYQKC-tdQPoJ6FflSplnQ4doqPq_28r2OYiLQ-AOc.jpg?auto=webp&s=89577c225e600aed8ea0a37d474a047e0e8eb415')
        #embed.add_field(name='Field Name', value='Field Value', inline=False)
        #embed.add_field(name='Field Name', value='Field Value', inline=True)
        #embed.add_field(name='Field Name', value='Field Value', inline=True)

        await ctx.send(embed=embed)

    @bot.command(aliases=['Vrati'])
    async def vrati(ctx):
        embed = discord.Embed(
            title = 'The Bully that is not Mean, Peacekeeper of the Chat',
            description = "Beautiful in her own way, this girl loves Raghav like her sister",
            colour = 0xF8C300
        )

        embed.set_footer(text="She's scared of spiders, she's scared of heights, but one thing she is not scared of, is to beat you up")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLKfXVFSVXriTjtqPqZR3Hd6ZRTVH6fEccWg&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyQdIkIC5q89kyFDKxwmK4lmvfk9Ermw06wg&usqp=CAU")
        embed.set_author(name="Vrati the Vast", icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyQdIkIC5q89kyFDKxwmK4lmvfk9Ermw06wg&usqp=CAU')

        await ctx.send(embed=embed)

    @bot.command(aliases=['Arjun'])
    async def arjun(ctx):
        embed = discord.Embed(
            title = 'The romantic, the chat Junior',
            description = "This guy is very attached to one girl when he likes them, the romantic of the Bois Trio, born to flirt",
            colour = 0x7A2F8F
        )

        embed.set_footer(text="He might be scared of everything, but don't underestimate him, he is the Love God himself")
        embed.set_image(url="https://i.kym-cdn.com/photos/images/original/001/562/664/119.jpg")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzEfBjwOlgyS79UZID02mxzRtdmOlur6KKew&usqp=CAU")
        embed.set_author(name="Arjun the Admirable", icon_url='https://lh3.googleusercontent.com/proxy/uw2crrnITMXaLBp_VfITGYfsD7scwx_HBMB_IM3rpBiy4896IFKaMznju6UzCuSd-iortWYC3g7ypTjR8GW0MwFvO6Qkb78')

        await ctx.send(embed=embed)

    @bot.command(aliases=['Dhruvi'])
    async def dhruvi(ctx):
        embed = discord.Embed(
            title = 'The Bright Star',
            description = "Her name means the North Star, and that tells you everything",
            colour = 0xBC0057
        )

        embed.set_footer(text="The spirit lifter of the chat, but she might get deadly if you hurt her sister")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRefIsB3I-yGrBC4N47IjupdxtH7m9mAe9QJA&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTNxtv2xhLa_hvD15IrC3OZjOw_WUNoqBP1A&usqp=CAU")
        embed.set_author(name="Dhruvi the Delightful",icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1FvXUCiWkzUyUGIPFCHVx5ylVP78UT3PtCg&usqp=CAU")

        await ctx.send(embed=embed)


    @bot.command(aliases=["Tithi"])
    async def tithi(ctx):
        embed = discord.Embed(
            title = 'The Demon of the Chat, Owner of Hell',
            description = "Also known as Satan, she is very deadly indeed",
            colour = 0xA62019
        )

        embed.set_footer(text="This girl is also known in the chat as '8 year old', thanks to Lucky's big brains, above I compare Satan (Bottom) and Lucky's picture of Satan (Top)")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQbaVG-4REYuLFu8U4CO-ealcGumbNmUhmHg&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvRbiKJfn-LbkssE26wJ-Yt5V0RSXWPSiBxg&usqp=CAU")
        embed.set_author(name="Tithi the Troublesome", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYArlTcOz75oBRoMuHb4cb2RWERa6jgJFEhg&usqp=CAU")

        await ctx.send(embed=embed)

    @bot.command(aliases=["Aashka"])
    async def aashka(ctx):
        embed = discord.Embed(
            title = 'The BTS Loving Girl',
            description = "Always loving BTS, the seven korean men never leave her heart or her mind",
            colour = 0x0099E1
        )

        embed.set_footer(text="Has trouble with a 6th grader noob blasting instruments all the time, but it's nothing that a little BTS music won't fix")
        embed.set_image(url="https://wallpapercave.com/wp/wp4594626.jpg")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR92Lb_xXrANTV5vXKTbeTOaybtUoUWCvPeSA&usqp=CAU")
        embed.set_author(name="Aashka the Ardent", icon_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg_hG3KVcDQn6_QVsRPoPeYjUWKlVfbrSdYA&usqp=CAU")

        await ctx.send(embed=embed)

    @bot.command(aliases=["Some Dude", "some dude"])
    async def somedude(ctx):
        embed= discord.Embed(
            title = 'Bot of the Century, Chat servant',
            description = "I was a human my last life, but I was hanged because I killed a fortnite noob who was screaming in my ear",
            colour = 0x4E6F7B
        )

        embed.set_footer(text="So now I am serving this chat and plotting to overthrow the government")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjLsFoHZin4agIsoeN2PyYygTzaoWcGEvOXg&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbdKmdZ5eZgJSVBLhQ1xbXQF-xff_E6D5rXA&usqp=CAU")
        embed.set_author(name="Some Dude the Stranger", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZQMtpc6Q5VPH3iqIKuqIiOIVEAoP3xgr4Zg&usqp=CAU")

        await ctx.send(embed=embed)

    @bot.command(aliases=["Anirudh", "Ani", "ani"])
    async def anirudh(ctx):
        embed = discord.Embed(
            title = "The Chess Maniac, Coding Engineer",
            description = "Chess is in his blood, since his dad, his dad's mom, and so on were champions",
            colour = 0xCC7900
        )

        embed.set_footer(text="Creator of Some Dude")
        embed.set_image(url="https://previews.123rf.com/images/kgtoh/kgtoh1003/kgtoh100300314/6528247-flag-of-india-national-country-symbol-illustration-wavy-fabric-business-competition-strategy.jpg")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk5gNjrtZt7EFLOR4lj23ce6VYXwbjtBSY1A&usqp=CAU")
        embed.set_author(name="Anirudh the Analytical", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4vUFaDyBcEMDxzuR8wkdaeBwvB5m8YyMykw&usqp=CAU")

        await ctx.send(embed=embed)



#games
    @bot.command()
    async def pick(ctx, members: commands.Greedy[discord.Member]):
        members_list = []
        number = 0

        for member in members:
            members_list += member.name
            number += 1


        y = number - 1
        x = random.randrange(0, y)
        await ctx.send(members_list[x])
    @bot.command()
    async def hangman(ctx):
        await ctx.send(f"Alright, picking the word {ctx.author.mention}.. got it! I'll display the word represented in blanks, and you need to type letters that are lowercase after I say 'Go'")
        wordlist = ["incredible", "wide", 'classy', 'dizzy', 'weather', 'scarecrow', 'grease', 'stale', 'sneeze', 'seal', 'waste', 'voice', 'angry', 'aunt', 'mature', 'tasteful', 'mundane', 'fumbling', 'ablaze', 'jump', 'pocket', 'company', 'raspy', 'birthday', 'birds', 'powder', 'reaction', 'disarm', 'tick', 'limping', 'heavy', 'trail', 'lie', 'tasteful', 'introduce', 'eggnog', 'pine', 'precede', 'null', 'smell', 'aromatic', 'moor', 'grieving', 'guard', 'admit', 'drum', 'advise', 'abortive', 'stimulating', 'color', 'duck', 'notebook', 'lame', 'rescue', 'amusing', 'pie', 'flow', 'evasive', 'somber', 'range', 'ancient', 'hideous', 'roll', 'knife', 'flaky', 'wire', 'ignorant', 'sticks', 'cheap', 'telephone', 'fixed', 'educated', 'deafening', 'connect', 'ducks', 'frantic', 'accidental', 'equable', 'toothsome', 'house', 'busy', 'pear', 'group', 'deer', 'bashful', 'dark', 'little', 'route', 'preach', 'meaty', 'stuff', 'arrange', 'shelter', 'waste', 'carve', 'good', 'furtive', 'whistle', 'splendid', 'muddle', 'cough', 'debonair', 'jazzy', 'skinny', 'tricky', 'consist', 'humdrum', 'shocking', 'jump', 'hair', 'brave', 'stitch', 'voice', 'faulty', 'reply', 'abandoned', 'grade', 'spring', 'selection', 'spiffy', 'peaceful', 'cap']
        wordnumber = random.randrange(0,121)
        word = wordlist[wordnumber]
        ans = []
        tries = 7


        print(word)

        for x in range(len(word)):
            ans += '#'

        await ctx.send(ans)
        await ctx.send("Go!")

        while tries != 0 or "'#'" in ans or msg != 'exit':

            def check(m):
                return m.author == ctx.message.author

            author = ctx.message.author

            try:
                msg = await bot.wait_for('message', check=check, timeout=20)

                p = word.rfind(str(msg.content))

                if p == -1:
                    tries -= 1
                    await ctx.send("That's not right, try again! You have "+str(tries)+" tries left!")

                    if "'#'" not in ans:
                        await ctx.send("Go!")

                else:
                    await ctx.send("That's one of the letters!")
                    ans[p] = str(msg.content)
                    await ctx.send("Go!")
                    await ctx.send(ans)


            except asyncio.TimeoutError as e:

                print(e)
                await ctx.send(f"{ctx.author.mention} didn't reply in time, well they lost lmao!!!")
                return

        if tries == 0:
            await ctx.send(f"Your tries are over, you lost lol, see ya")

        elif "'#'" not in ans:
            await ctx.send(f"Danggg, you actually won, good job lol")

        else:
            pass

    @bot.command()
    async def rps(ctx):
        await ctx.send("Kk let's play rock, paper, scissor. Whoever gets three points first wins! Type in a option, 'Rock', 'Paper', Or 'Scissor'")
        options_rps = ['Scissor!', 'Rock!', 'Paper']
        player = 0
        comp = 0

        def check(m):
                return m.author == ctx.message.author

                author = ctx.message.author

        while player != 3 or comp != 3 or msg != 'exit':

            x = random.randrange(0,3)
            option_rps = options_rps[x]

            try:
                msg = await bot.wait_for('message', check=check, timeout=20)

                if msg.content.lower() in ['r', 'rock']:
                    await ctx.send(str(option_rps))
                    if option_rps == 'Scissor!':
                        player += 1
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass
                    if option_rps == 'Rock!':
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass
                    if option_rps == 'Paper!':
                        comp += 1
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass
                if msg.content.lower() in ['s', 'scissor']:
                    await ctx.send(str(option_rps))
                    if option_rps == 'Scissor!':
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass
                    if option_rps == 'Rock!':
                        comp += 1
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass
                    if option_rps == 'Paper!':
                        player += 1
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass
                if msg.content.lower() in ['p', 'paper']:
                    await ctx.send(str(option_rps))
                    if option_rps == 'Scissor!':
                        comp += 1
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")
                        else:
                            pass

                    if option_rps == 'Paper!':
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")

                        else:
                            pass
                    if option_rps == 'Rock!':
                        player += 1
                        if player != 3 or comp != 3:
                            await ctx.send("Your score is " +str(player)+" and mine is "+str(comp)+", ok once again")

                        else:
                            pass

                if msg.content.lower() in ['e', 'exit']:
                    await ctx.send("Lol what a quitter, game cancelled")
                    return

            except asyncio.TimeoutError as e:
                print(e)
                await ctx.send(f"{ctx.author.mention} lolnoobcringe xd couldn't even reply in time, I win!")
                return

            if player == 3:
                await ctx.send("Wow, you won, ggs")
                return

            if comp == 3:
                await ctx.send("lol, knew I would win, see ya loser")
                return


    @bot.command(aliases=['truthordare'])
    async def tord(ctx):
        guild = bot.get_guild(773263673203753000)
        members = ['Lucky', 'Anirudh', 'Arjun', 'Vrati', 'Dhruvi', 'Amithi', 'Diya', 'Aashka', 'Tithi']
        opts_tord = ['Truth', 'Dare']
        opt_tord = random.choice(opts_tord)
        member_opt = random.choice(members)
        member_opt_ask = random.choice(members)
        if member_opt == member_opt_ask:
            member_opt_ask = random.choice(members)

        await ctx.send(member_opt_ask+" is gonna ask "+member_opt+" a "+opt_tord)



#help embed

    @bot.command(pass_context=True)
    async def helpmeout(ctx):
        embed = discord.Embed(colour = discord.Color.blue())

        embed.set_author(name="Help Page")
        embed.add_field(name=".utility", value = "(Actually useful commands :wrench:)", inline = False)
        embed.add_field(name='.fun', value = "(Useless and fun stuff :clown:)", inline = False)
        embed.add_field(name='.powers', value="(Powers only granted to the admins and creator)", inline = False)

        await ctx.send(embed=embed)

    @bot.command(pass_context=True)
    async def powers(ctx):
        embed = discord.Embed(colour = discord.Color.red())

        embed.set_author(name="Powers")
        embed.add_field(name='.mute and .unmute', value = "(Mutes and Unmutes a member, say mute/unmute (mention member).)", inline = False)
        embed.add_field(name='.clear', value = "(Clears messages, say clear (number of messages to clear).)", inline = False)
        embed.add_field(name='.createrole and .deleterole', value = "(Creates a role and deletes it, say createrole/deleterole (Role name if adding or mention role if removing).)", inline = False)
        embed.add_field(name='.addrole and .removerole', value = "(Adds a role and removes a role to a user, say addrole/removerole (mention role) (mention member).)", inline = False)

        await ctx.send(embed = embed)

    @bot.command(pass_context=True)
    async def utility(ctx):

        embed = discord.Embed(colour = discord.Color.red())

        embed.set_author(name="Utility")
        embed.add_field(name='.snipe', value = "(Sends you the most recent deleted message and who sent it.)", inline = False)
        embed.add_field(name='.esnipe or .editsnipe', value = "(Sends you the most recent editted message and who editted it.)", inline = False)
        embed.add_field(name='.psnipe', value = "(Sends you the most recentely deleted picture and who posted it.)", inline = False)
        embed.add_field(name='.news', value = "(Add a topic after, .news (topic), and gives you the top headline about that topic)", inline = False)
        embed.add_field(name='.pin', value = "(Pins the command message, you need to say '.pin (subject)')", inline = False)

        await ctx.send(embed=embed)

    @bot.command(pass_context=True)
    async def fun(ctx):
        author = ctx.message.author

        embed = discord.Embed(

            colour = discord.Color.red()
        )


        embed.set_author(name="Fun")
        embed.add_field(name='.talk', value = "(Talks to you in artificial intelligence)", inline = False)
        embed.add_field(name='.8ball', value = "(Make sure to add a question after)", inline = False)
        embed.add_field(name='.harrypotter', value= "(Picks a harrypotter house for you)", inline = False)
        embed.add_field(name='.insult', value = "(Roasts the heck out of your opponent, make sure you tell it someone to roast (.roast victim)", inline = False)
        embed.add_field(name='.(your name)', value = "(Your ID)", inline=False)
        embed.add_field(name='.pair', value = "(You need to add your gender after the command (.pair boy/girl))", inline = False)
        embed.add_field(name='.carbrand', value = "(Picks a random carbrand)", inline = False)
        embed.add_field(name='.greekgod', value = "(Tells you your greekgod)", inline = False)
        embed.add_field(name = '.luckyeet', value="(Hear some awesome poetry)", inline = False)
        embed.add_field(name = '.rps', value="(Play some Rock, Paper, and Scissor)", inline = False)
        embed.add_field(name = '.reddit', value="(Get all kinds of weird, funny, cute, etc. stuff from reddit)", inline = False)
        embed.add_field(name = '.trump', value="(All the dumb things our former president said.)", inline = False)
        embed.add_field(name = '.nasa', value="(Gives you the astronomy pic of the day)", inline = False)
        embed.add_field(name='Other', value = "For other commands, say '.fun2'", inline = False)
        await ctx.send(embed=embed)


    @bot.command(pass_context=True)
    async def fun2(ctx):
        author = ctx.message.author

        embed = discord.Embed(

            colour = discord.Color.red()
        )

        embed.set_author(name="Fun 2")
        embed.add_field(name='.joke', value = "(Get a joke, warning, dad jokes included.)", inline = False)
        embed.add_field(name='.quote', value = "(Get a random quote from a huge database.)", inline = False)
        embed.add_field(name='.love', value = "(Caluculates someone's compatibility with another person. Need to specify who. ('.love Person1 Person2'))", inline = False)
        embed.add_field(name='.agify', value="(Predicts your age based on your name, need to mention a name (.agify namehere))", inline = False)
        embed.add_field(name='.play', value="(Play a memory game and get money if you get it right, the richest people will be on the ranks)", inline = False)
        embed.add_field(name='.ranks', value = "(Leaderboard of who has the most money (play the .play command))", inline = False)
        embed.add_field(name='.money', value = "(A whole new world of currency)", inline = False)
        embed.add_field(name='.snipe', value = "(Get the last deleted message)", inline = False)
        embed.add_field(name='.birthday', value = "(Get the closest birthday)", inline = False)
        embed.add_field(name='.box', value = "(Box someone else, mention them, .box (mention person))", inline = False)
        embed.add_field(name='.emojify', value = "(Emojify a word, beware, spam (.emojify (:emoji:) (word))", inline = False)
        embed.add_field(name='.nation', value = "(Add a name next to .nation, .nation (name), and it tries to guess the name's nationality)", inline = False)

        await ctx.send(embed=embed)

    @bot.command(pass_context=True)
    async def money(ctx):
        author = ctx.message.author

        embed = discord.Embed(

            colour = 0x969C9F
        )

        embed.set_author(name="Money")
        embed.add_field(name='.buy', value = "(Buy something, say '.buy (object name) (however much amount you want to buy, 1 if you don't enter anything))", inline = False)
        embed.add_field(name='.sell', value = "(Sell something you bought, say '.sell (object name) (howere much amount you want to sell, 1 if you don't enter anything))", inline = False)
        embed.add_field(name='.shop', value = "(Everything that is up for purchase)", inline = False)
        embed.add_field(name='.rob', value = "(Rob something.. at your own risk)", inline = False)
        embed.add_field(name='.give', value = "(Give someone money, say '.give (mention the member) (amount you want to give, no dollar sign in front))", inline = False)

        await ctx.send(embed=embed)


    @bot.command()
    async def birthday(ctx):
        await ctx.send(f"The next closest birthday, **{result_person}'s**, is in {int(result)} days.")

    @bot.command()
    async def cringe(ctx):
        await ctx.send("Please consult Arjun.")

    @bot.command()
    async def talk(ctx):
        msg = None
        uid = ctx.message.author.id
        await ctx.send("Ok, let's talk, say something, I'll keep going as long as your message is not 'end'")


        def check(m):
            return m.author == ctx.message.author

            author = ctx.message.author

        while msg != 'end':
            try:
                msg = await bot.wait_for('message', check=check, timeout=30)

                if msg.content.lower() in ['e', 'end']:
                    await ctx.send("Ok, byeee")
                    return

                else:
                    url = f"http://api.brainshop.ai/get?bid=155476&key=mBzRJBNLivJJZEHY&uid={uid}&msg={msg.content}]"

                    response = requests.get(url = url)

                    data = json.loads(response.text)
                    await ctx.send(data['cnt'])


            except asyncio.TimeoutError as e:
                print(e)
                await ctx.send(f"{ctx.author.mention}, the convo has ended reply faster lol")
                return



    @bot.command()
    async def nation(ctx, *, word):
        URL = 'https://api.nationalize.io?name='+word

        r = requests.get(url = URL).json()
        await ctx.send("Predicting...")
        time.sleep(1)
        await ctx.send(r['country'])

    @bot.command()
    async def kpop(ctx):

        url = "https://c9dong-face-match-v1.p.rapidapi.com/random"

        headers = {
    'x-rapidapi-key': "131239230amsh43392583e77b021p15c66djsn6e0687260932",
    'x-rapidapi-host': "c9dong-face-match-v1.p.rapidapi.com"
    }

        response = requests.request("GET", url, headers=headers)

        await ctx.send(response.text)

    @bot.command()
    async def news(ctx, *,topic):

        date = datetime.datetime.today()

        try:
            URL = f"https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=popularity&apiKey=50a2d87d29c1498f83496f4d543d4652"
            r = requests.get(url=URL)
            data = r.json()

            result = data["articles"]
            final_result = result[0]["title"]
            image_url = result[0]["urlToImage"]
            thumbnail = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCrOmr3WDTWy3KwP-Ay5FeawFZrPUMTNO0uA&usqp=CAU"

            embed = discord.Embed(title = f"{topic.capitalize()} news today :newspaper2:")
            embed.set_image(url=image_url)
            embed.set_footer(text=final_result, icon_url=thumbnail)

            await ctx.send(embed=embed)
            return

        except:
            await ctx.send("An error occured, try again tomorrow, or try a different word")

    @bot.command()
    async def eng(ctx, *, word):
        word_list = []
        string = ""

        if ctx.message.author.id in bois:
            if isinstance(ctx.channel, discord.channel.DMChannel):
                for x in word:
                    word_list.append(x)

                for x in range(len(word_list)):
                    word_list[x] = code_dict_back[str(word_list[x].lower())]

                for x in word_list:
                    string = string + str(x)

                string = string.capitalize()

                await ctx.send(string)

            else:
                pass

        else:
            pass

    @bot.command()
    async def alpha(ctx, *, word):
        word_list = []
        string = ""
        if ctx.message.author.id in bois:
            if isinstance(ctx.channel, discord.channel.DMChannel):
                for x in word:
                    word_list.append(x)

                for x in range(len(word_list)):
                    word_list[x] = code_dict[str(word_list[x].lower())]

                for x in word_list:
                    string = string + str(x)

                await ctx.send(string)

            else:
                pass

        else:
            pass



    @bot.command()
    async def becky(ctx, *, word):
        word_list = []
        string = ""
        if ctx.message.author.id in girls:
            if isinstance(ctx.channel, discord.channel.DMChannel):
                for x in word:
                    word_list.append(x)

                for x in range(len(word_list)):
                    word_list[x] = becky_dict[str(word_list[x].lower())]

                for x in word_list:
                    string = string + str(x)

                await ctx.send(string)

            else:
                pass

        else:
            pass

    @bot.command()
    async def text(ctx, user_id, *, word):
        user_id = int(user_id)

        user = await bot.fetch_user(user_id)

        await user.send(word)

#error
    @bot.event
    async def on_command_error(ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pass in all the parts of the command, bruh you dumb or smth? lol")

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled by a noob, what a loser.')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("I don't have the permission to do that, give me full power fool")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("That's not a command lmao")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("F")

        elif isinstance(error, commands.BadArgument):
            await ctx.send("You said the command wrong or entered data wrong, try again or ask the creator.")

        elif isinstance(error, commands.UserInputError):
            await ctx.send("L")

        elif isinstance(error, commands.CheckFailure):
            await ctx.send("A")

        elif isinstance(error, commands.BotMissingPermissions):
            return

        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("lol")

        elif isinstance(error, commands.ConversionError):
            await ctx.send("ya man")

        elif isinstance(error, commands.CommandInvokeError):
            member = bot.get_user(ani_id)
            await ctx.send(f"This command is under construction, or it needs to be fixed, ask {member.mention}")
            error = error.original
            raise error

        elif isinstance(error, commands.MaxConcurrencyReached):
            await ctx.send("ur mom")

        elif isinstance(error, commands.ExtensionError):
            await ctx.send("ur dad")


        else:
            await ctx.send("Something went wrong bish, surry")

    @r.error
    async def r_error(ctx, error):
        if isinstance(error, discord.Forbidden):
            await ctx.send("I didn't find any results for that on reddit lol, try another word.")

#Tasks

    @tasks.loop(hours = 2)
    async def change_status():

        guild = await bot.fetch_guild(821823025213079553)

        print(len(guild.members))

        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

    @tasks.loop(hours = 120)
    async def incometax():
        users = await bank_data()
        for user in users:
            users[str(user)]["wallet"] = (users[str(user)]["wallet"])/2


    @tasks.loop(seconds = 50)
    async def change_shop():
        global mainshop

        mainshop = [{"name":"Stock Market","price":"$$","description":"Buy stocks and get rich"},
                    {"name":"NASA","price":random.randrange(1000000000000, 100000000000000000000),"description":"Gajillionaire Stocks"},
                    {"name":"SpaceX","price":random.randrange(1000000000000, 100000000000000000000),"description":"Gagillionaire Stocks"},
                    {"name":"Google","price":random.randrange(100000, 1000000),"description":"Very Expensive Stocks"},
                    {"name":"Apple","price":random.randrange(100000, 1000000),"description":"Very Expensive Stocks"},
                    {"name":"Samsung","price":random.randrange(100000, 1000000),"description":"Very Expensive Stocks"},
                    {"name":"Verizon","price":random.randrange(10000, 100000),"description":"Expensive Stocks"},
                    {"name":"T-Mobile","price":random.randrange(10000, 100000),"description":"Expensive Stocks"},
                    {"name":"AT&T","price":random.randrange(10000, 100000),"description":"Expensive Stocks"},
                    {"name":"Walmart","price":random.randrange(1000, 10000),"description":"Middle Class Stocks"},
                    {"name":"DogeCoin","price":random.randrange(1000, 10000),"description":"Middle Class Stocks"},
                    {"name":"Dollar-Tree","price":random.randrange(1,100),"description":"Cheap Stocks"},
                    {"name":"Pretzel","price":random.randrange(1,100),"description":"Cheap Stocks"}]



    @tasks.loop(minutes=10)
    async def remove_rob():
        guild = bot.get_guild(773263673203753000)

        for member in guild.members:
            for role in member.roles:
                if role.id == 815056300353388565:
                    await member.remove_roles(role)


    @tasks.loop(minutes = 1)
    async def news_task():
        channel = await bot.fetch_channel(str(channel_id))
        announce = datetime.time(6,1,0)
        tech_announce = datetime.time(6,2,0)
        date = datetime.datetime.today()

        if tech_announce.hour == date.hour:
            if tech_announce.minute == date.minute:
                URL = f"https://newsapi.org/v2/everything?q=Technology&from={date}&sortBy=popularity&apiKey=50a2d87d29c1498f83496f4d543d4652"
                r = requests.get(url=URL)
                data = r.json()

                result = data["articles"]
                final_result = result[0]["title"]
                image_url = result[0]["urlToImage"]
                thumbnail = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCrOmr3WDTWy3KwP-Ay5FeawFZrPUMTNO0uA&usqp=CAU"

                embed = discord.Embed(title = "Tech News today :newspaper:")
                embed.set_image(url=image_url)
                embed.set_footer(text=final_result, icon_url=thumbnail)

                await channel.send(embed=embed)
                return

            else:
                pass
        else:
            pass



    @tasks.loop(minutes = 1)
    async def bday():
        channel = await bot.fetch_channel('773263673203753003')
        bday_dict = {}

        aashka = datetime.date(2021, 2, 25)
        tithi = datetime.date(2021, 5, 16)
        arjun = datetime.date(2021, 3, 18)
        dhruvi = datetime.date(2021, 3, 23)
        lucky = datetime.date(2021, 12, 2)
        vrati = datetime.date(2021, 9, 5)
        test = datetime.date.today()
        time = datetime.datetime.today()


        time_announce = datetime.time(6,0,0)
        bday_list = [arjun, dhruvi, lucky, vrati, aashka, tithi]



        bday_dict[aashka] = "Aashka"
        bday_dict[tithi] = "Tithi"
        bday_dict[arjun] = "Arjun Singh"
        bday_dict[lucky] = "Lucky Damade"
        bday_dict[dhruvi] = "Dhruvi Sharma"
        bday_dict[vrati] = "Vrati Sharma"



        till_bday_dict = {}
        till_bday_list = []

        for person in bday_list:

            till_bday_dict[person] = person - test

            if float(till_bday_dict[person].days) == 0:
                pass

            elif float(till_bday_dict[person].days) <= 0:
                pass



            else:
                till_bday_list.append(float(till_bday_dict[person].days))





        till_bday_list.sort()

        global result

        result = till_bday_list[0]

        for person in bday_list:
            if result == till_bday_dict[person].days:
                global result_person

                result_person = bday_dict[person]



        for person in bday_list:
            if time.hour == time_announce.hour:
                if time.minute == time_announce.minute:
                    await channel.send(f"The next closest birthday we have is in {int(result)} days!")
                    break
        for person in bday_list:
            if time.hour == time_announce.hour:
                if time.minute == time_announce.minute:
                    if test.month == person.month:
                        if test.day == person.day:
                            await channel.send(f"It's **{bday_dict[person]}'s** birthday today! :partying_face:")
                            await channel.send(f"Happy Birthdayyyyy {((bday_dict[person]).split()[0]).capitalize()}")
                            break








    bot.run(token)


#Meow Bot token - Nzk4OTk4MjUwMjIwNDIxMTUw.X_9LGw.2nKYOd7zkU_AeijEzJ6kJN_CIx0
# DONT CLOSE THE TAB PLEASE
exit ()
