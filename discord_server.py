#!/usr/bin/python3

import discord
import random
from ws_client import Client


token = open('token.priv','r').readline()
bot_client = discord.Client()

@bot_client.event
async def on_ready():
    print('Logged in as')
    print(bot_client.user.name)
    print(bot_client.user.id)
    print('------')

@bot_client.event
async def on_message(message):
    if message.author == bot_client.user: return

    # book command
    if message.content.startswith('!book'):
        await bot_client.send_message(message.channel, 'The daily book today is:')
        web_scrapping_client = Client()
        web_scrapping_client.run()
        await bot_client.send_file(message.channel, 'book_cover.jpg')
        book_info = open("book_info.txt", "r")
        for line in book_info:
            await bot_client.send_message(message.channel, line)

bot_client.run(token)
