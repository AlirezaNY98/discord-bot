from lib2to3.pgen2 import token
import discord
import Token
import urllib.request
import json

client = discord.Client()
good_words = ['afarin', 'ahsant', 'barikala', 'mashala', 'bos', 'damet garm', 'ghorbonet', 'nokaretam', 'mokhlesam' ]


def meme():
    meme_url = urllib.request.urlopen("https://api.codebazan.ir/jok/json/")

    meme_data = meme_url.read()
    meme_JSon = json.loads(meme_data)
    return meme_JSon["result"]["jok"]

def quote():
    quote_url = urllib.request.urlopen("http://api.codebazan.ir/hadis/")

    quote_data = quote_url.read()
    return quote_data.decode()

@client.event
async def on_ready():
    print('we have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("$help"):
      await message.channel.send("This is ARA guid commands:\n\n\t$hello => bot say hello to you\n\t\
        $meme => send joke in channel\n\n\t$quote => send a quote for you")

    if any(word in msg for word in good_words):
        await message.channel.send("nice...")

    if msg.startswith("$meme"):
        await message.channel.send(meme())

    if msg.startswith("$delete 5"):
        await message.channel.purge(limit = 5)

    if msg.startswith("$quote"):
        await message.channel.send(quote())

client.run(Token.Token())