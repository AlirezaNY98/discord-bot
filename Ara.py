from lib2to3.pgen2 import token
import discord
import Token
import urllib.request
import json
import random

client = discord.Client()
good_words = ['afarin', 'ahsant', 'barikala', 'mashala', 'bos', 'damet garm', 'ghorbonet', 'nokaretam', 'mokhlesam' ]


def meme():
    web_url = urllib.request.urlopen("https://api.codebazan.ir/jok/json/")
    data = web_url.read()
    meme_JSon = json.loads(data)
    return meme_JSon["result"]["jok"]
    

@client.event
async def on_ready():
    print('we have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("$help"):
      await message.channel.send("This is ARA guid commands:\n\t$hello => bot say hello to you\n\t \
        $meme => send joke in channel")

    if any(word in msg for word in good_words):
        await message.channel.send("nice...")

    if msg.startswith("$meme"):
        await message.channel.send(meme())



client.run(Token.Token())