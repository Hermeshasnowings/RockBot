import discord
import os
import json
import requests
import random
from discord.ext.commands import has_role
from discord.utils import get
from keep_alive import keep_alive

Quote = [
    "What is this? Am I in a movie?",
    "Hey, boss... Don't you remember? Well, you should! I'm already dead. You said it, remember? And by the way, my name is Rock now!",
    "Hm. Is money... your God?",
    "I wish I hadn't heard that. I'm sorry.",
    "Huh?",
    "I wonder... maybe you can tell me who kept the church from becoming a bloodbath today? It's just like the old lady said: you can't solve everything with a gun.",
    "In that case! I'll say it again! I didn't make any mistake! I have nothing to apologize for! That's what I'm saying!",
    "Why don't you write: 'there's no cure for a fool with a gun'? ",
    "Rrrgh! See that? There are some problems you can't solve with a gun!",
    "There’s a noose that hangs at the entrance to the city. It’s a message to be read by all who encounter it. For the cautious, the sane, it’s a warning. For the reckless, the wild at heart, an invitation they cannot refuse. The worst of the criminal underworld gather here. They come here from across the world to butt heads and jostle for power. An evil city caught between the east and the west founded during the Cold War and nurtured by many who came here to ride the wave of the illegal drug trade sweeping across the continent. The edge of the world, the crucible of hypocrisy, a place where those whose souls have been destroyed in the relentless search for money and power reside. A final stop on the way to hell. How have I managed to stay alive this long?",
    "Surely you must still have some sense of justice!",
    "Ms. Balalaika. Your victory here is assured. And... You no longer have anything to lose, so - isn't that -Isn't that enough for you?!",
    "You're misunderstanding!",
    "I'm sorry I brought this up... Look, I --",
    "...A medal...and a skull...",


]


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if discord.utils.get(message.author.roles, name="Rock"):
        await message.channel.send(random.choice(Quote))

keep_alive()
client.run(os.environ['TOKEN'])
