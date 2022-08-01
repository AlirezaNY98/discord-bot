from lib2to3.pgen2 import token
import discord
import Token
import random

client = discord.Client()
bad_words = ['kir', 'kos', 'kon', 'fuck']
against_bw = ['bi adab nabashim', 'kore khar fosh nade', 'dahaneto ab bemal', 'bia bokhoresh', 'na omid shodam azat -_-']


@client.event
async def on_ready():
    print('we have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith("$hello"):
        await message.channel.send("hello darlin !!!")

    if any(word in msg for word in bad_words):
        await message.channel.send(random.choice(against_bw))

    if msg.startswith("$help"):
      await message.channel.send("This is ARA guid commands:\n\t$hello => bot say hello to you\n\tif you use bad words bot reactioned to your message")

client.run(Token.Token())