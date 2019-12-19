# *********************
# PROGRAM BY JAMES URE
# AUGUST 2019
# CLASH ROYALE STATS BOT
# can retrieve info of the players in-game statistics
# and making a branching statement accordingly

import discord
import urllib.request
import json


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


def read_apitoken():
    with open("apitoken.txt") as f:
        my_key = f.readlines()
        return my_key[0].strip()


token = read_token()
client = discord.Client()


@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.idle, activity= discord.Game("!rank <hashtag>"))

    print('test ready')


@client.event
async def on_message(message):
    print(message)
    if message.content.startswith("!rank") and str(message.author.id) != "608066453341470725":
        print('success')
        msg = str(message.content)
        msg = msg.partition("!rank ")[2]
        msg = msg.replace("#", "%23")
        base_url = "https://api.clashroyale.com/v1"
        endpoint = "/players/"+msg
        print(base_url + endpoint)
        try:
            request = urllib.request.Request(base_url + endpoint, None, {"Authorization": "Bearer %s" % read_apitoken()})
            response = urllib.request.urlopen(request).read().decode("utf-8")

        except:
            await message.channel.send("invalid hash")
            return

        print(response)

        data = json.loads(response)
        print('test')

        if data["bestTrophies"] > 6999:

            await message.channel.send("You're an ultimate champ (aka jungle arena)!")
            print('success')
            try:
                guild = client.get_guild(582085045561458692)
                role = guild.get_role(608144312257216518)
                await message.author.add_roles(role)
            except AttributeError:
                print('ERROR: failed to add role')
            return

        elif data["bestTrophies"] > 5999 and data["bestTrophies"] < 7000:
            await message.channel.send("You're in Champs!")
            print('success')
            try:
                guild = client.get_guild(582085045561458692)
                role = guild.get_role(608241681879269376)
                await message.author.add_roles(role)
            except AttributeError:
                print('ERROR: failed to add role')
            return

        elif data["bestTrophies"] > 4999 and data["bestTrophies"] < 6000:
            await message.channel.send("You're in Master!")
            print('success')
            try:
                guild = client.get_guild(582085045561458692)
                role = guild.get_role(608241822216618015)
                await message.author.add_roles(role)
            except AttributeError:
                print('ERROR: failed to add role')
            return

        elif data["bestTrophies"] > 3999 and data["bestTrophies"] < 5000:
            await message.channel.send("You're in Challenger!")
            print('success')
            try:
                guild = client.get_guild(582085045561458692)
                role = guild.get_role(608241914705215488)
                await message.author.add_roles(role)
            except AttributeError:
                print('ERROR: failed to add role')
            return
        else:
            await message.channel.send("You're a noob!")
            print('success1')
            try:
                guild = client.get_guild(582085045561458692)
                role = guild.get_role(608242010918354944)
                await message.author.add_roles(role)
            except AttributeError:
                print('ERROR: failed to add role')
            return

client.run(token)


#base_url = "https://api.clashroyale.com/v1"
#endpoint = "/clans/%239V2CG29C/members"
#request = urllib.request.Request(base_url + endpoint,None, {"Authorization": "Bearer %s" % read_apitoken()})
#response = urllib.request.urlopen(request).read().decode("utf-8")

#print("Best Trophies: %d\n" % data["bestTrophies"])

#for item in data["items"]:
    #print("Name: %s\nrole: %s\nTag: %s\n\n" % (item["name"],item["role"],item["tag"]))