import discord
import os
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


client.run(os.environ['key'])
