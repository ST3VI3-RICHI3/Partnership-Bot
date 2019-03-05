#Partnership-Bot by ST3VI3 RICHI3#5015

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os
import threading

print("Bot loading token from file TOKEN.txt")

Reader = open("TOKEN.txt", "r")
TOKEN = str(Reader.readline())

print("Bot loading...")

bot = commands.Bot(command_prefix='p!')#sets the prefix for the bot.
client = bot
bot.remove_command('help')
@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="p!help"), status=discord.Status("online"), afk=False)
	print("Bot is running & ready!")
	
bot.run(TOKEN)
