import discord
import asyncio
import time

#id = 582085045561458692
messages = joined = 0

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()


@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.idle, activity= discord.Game("Despacito"))

    print('test ready')

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"""Time: {int(time.time())}, Messages: {messages}, Members joined: {joined}\n""")
                messages = 0
                joined = 0

                await asyncio.sleep(60)
        except Exception as e:
            print(e)
            await asyncio.sleep(60)

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("becky") > 0:
            last = before.nick
            if last:
                await after.edit(nick = last)
            else:
                await after.edit(nick = "Cannot change nickname")

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}!""")


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(582085045561458692)

    #ALL DATA SETS INITIALIZED
    channels = ["bot-commands", "general"]
    valid_users = ["Azer#0001","Daddy Azer's offspring#4652"]
    commands = ["!test", "!membercount", "!mute", "!say"]

    #CHECK VALIDITY OF COMMAND ISSUE
    if str(message.channel) in channels and str(message.author) in valid_users:

        #TEST COMMAND
        if message.content.find(commands[0]) != -1:
            await message.channel.send("success")
            await message.delete()

        #MEMBERCOUNT COMMAND
        elif message.content.startswith(commands[1]):
            await message.channel.send(f"""# of Members: {id.member_count} """)
            #await message.delete()

        elif message.content == commands[2]:
            msg = str(message.content)
            msg = str.replace(commands[2],'')
            await client.add_roles


        #SAY COMMAND
        elif message.content.startswith(commands[3]):
            msg = str(message.content)
            msg = msg.replace('!say','')
            await message.delete()
            await message.channel.send(msg)

    elif str(message.content) in commands:
        await message.channel.send(f"""User: {message.author} insufficient permissions for command, channel: {message.channel}""")
client.loop.create_task(update_stats())
client.run(token)

