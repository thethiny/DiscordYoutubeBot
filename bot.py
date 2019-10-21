# Work with Python 3.6
import discord
from keys import TOKEN
from youtubeAPI import get_sub_count

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('?sub'):
        print(f"{message.author}: {message.content}")
        response = get_sub_count(message.content)
        await message.channel.send(f"{response}, {message.author.mention}")
        print(response)
        return
    
    #if message.content.startswith('!hello'):
        #msg = 'Hello {0.author.mention}'.format(message)
        #await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as:', client.user.name)
    print(client.user.id)
    print()
    

client.run(TOKEN)