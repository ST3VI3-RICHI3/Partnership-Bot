#Partnership-Bot by ST3VI3 RICHI3#5015

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

print("Bot loading token from file TOKEN")

TOKEN = open(str("TOKEN"), "r")
TOKEN = str(TOKEN.readline())

print("Done!")
print("Bot loading...")

bot = commands.Bot(command_prefix='p!')#sets the prefix for the bot.
client = bot
bot.remove_command('help')
@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="p!help"), status=discord.Status("online"), afk=False)
	print("Done! Bot is running & ready!")

@bot.command(pass_context = True)
async def help(ctx):
	await bot.say("This is the help command, it is not implemented.")

@bot.command(pass_context = True)
async def Config(ctx, File : str, Property : str, Value : str):
	print("Not implemented")

@bot.command(pass_context = True)
async def restart(ctx):
	await bot.change_presence(game=discord.Game(name="Restarting..."), status=discord.Status("dnd"), afk=False)
	print("Restarting...")
	os.system("start bot.py")
	exit(0)

@bot.command(pass_context = True)
async def update(ctx):
	await bot.change_presence(game=discord.Game(name="Updating..."), status=discord.Status("dnd"), afk=False)
	print("Downloading update from git...")
	os.system("cd C:/Users/%username%/Documents/GitHub/Partnership-Bot/ | git pull | echo.")
	os.system("start bot.py")
	exit(0)

bot.run(TOKEN)
