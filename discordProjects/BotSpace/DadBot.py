import discord
import asyncio
import time
import random

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.online, activity=discord.Game("Frisbee"))

    print('test ready')

@client.event
async def on_message(message):
    print(message.content)
    print(message.author.id)
    print("")
    usermsg = str(message.content.upper())
    if (usermsg.startswith(("I’M ", "I'M ", "IM ")) or (any([keyword in message.content.upper() for keyword in (" I’M ", " I'M "," IM ")]))
            and str(message.author.id) != "584303865441026068"):

        print('Joke made')
        msg = str(message.content)

        if "I’m" in msg:
            msg = msg.partition("I’m")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "I'm" in msg:
            msg = msg.partition("I'm")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "I’M" in msg:
            msg = msg.partition("I’M")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "I'M" in msg:
            msg = msg.partition("I'M")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "IM" in msg:
            msg = msg.partition("IM")[2]
            await message.channel.send(f"""hi{msg}, I'm dad!""")
            return
        if "im" in msg:
            msg = msg.partition("im")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "Im" in msg:
            msg = msg.partition("Im")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "i’m" in msg:
            msg = msg.partition("i’m")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
        if "i'm" in msg:
            msg = msg.partition("i'm")[2]
            await message.channel.send(f"""hi{msg}, I’m dad!""")
            return
    elif message.content.startswith("!dadjoke"):
        randomnum = random.randint(0,9)
        if randomnum == 0:
            await message.channel.send("I bought some shoes from a drug dealer. I don't know what he "
                                       "laced them with, but I was tripping all day!")
        elif randomnum == 1:
            await message.channel.send("If you see a robbery at an Apple Store does that make you an iWitness?")

        elif randomnum == 2:
            await message.channel.send("Justice is a dish best served cold, if it were served warm it would be "
                                       "justwater.")
        elif randomnum == 3:
            await message.channel.send("Don't trust atoms. They make up everything!")
        elif randomnum == 4:
            await message.channel.send("KID: 'Dad, make me a sandwich!' DAD: 'Poof, you’re a sandwich!'")
        elif randomnum == 5:
            await message.channel.send("Why did the invisible man turn down the job offer? He couldn't see himself doing it.")
        elif randomnum == 6:
            await message.channel.send("What's the best part about living in Switzerland? I don't know, but the flag is a big plus.")
        elif randomnum == 7:
            await message.channel.send("How many tickles does it take to make an octopus laugh? Ten-tickles.")
        elif randomnum == 8:
            await message.channel.send("Can February March? No, but April May!")
        elif randomnum == 9:
            await message.channel.send("What does an angry pepper do? It gets jalapeño your face.")
        return

client.run(token)
