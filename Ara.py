from lib2to3.pgen2 import token
import discord
import Token
import random

client = discord.Client()
good_words = ['afarin', 'ahsant', 'barikala', 'mashala', 'bos', 'damet garm', 'ghorbonet', 'nokaretam', 'mokhlesam' ]

@client.event
async def on_ready():
    print('we have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("$help"):
      await message.channel.send("This is ARA guid commands:\n\t$hello => bot say hello to you\n\tif you use bad words bot reactioned to your message")

    if any(word in msg for word in good_words):
        await message.channel.send("nice...")



client.run(Token.Token())