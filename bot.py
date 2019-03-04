#Partnership-Bot by ST3VI3 RICHI3#5015

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import json
import os
import threading
import random

TOKEN = open("TOKEN.txt", "r")
TOKEN = TOKEN.readline()

bot = commands.Bot(command_prefix='p!')#sets the prefix for the bot.
client = bot
bot.remove_command('help')
@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="p!help"), status=discord.Status("online"), afk=False)

bot.run(TOKEN)