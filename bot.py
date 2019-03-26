#Partnership-Bot by ST3VI3 RICHI3#5015

from __future__ import print_function
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os


print("Bot loading token from file TOKEN [0%]", end = "\r")

if os.path.isfile("TOKEN"): 
	TOKEN = open(str("TOKEN"), "r")
	print("Bot loading token from file TOKEN [50%]", end = "\r")
	TOKEN = str(TOKEN.readline())
	print("Bot loaded token from file TOKEN [100%]", end = "\n")
else:
	print("Loading failed, file does not exist.")
	TOKEN = input("Please enter the bot token.")
	with open("TOKEN" "w") as Writer:
		Writer.write(TOKEN)
		Writer.close()
		print("Token saved, if your bot is on GitHub make sure to add \"TOKEN\" to your gitnore.")

print("Bot loading  [0%]", end = "\r")

Sudo_owner = "ST3VI3 RICHI3#5015"
Owners = ["ST3VI3 RICHI3#5015"]
with open("Owners.txt", "r") as f:
	for line in f:
		Owners.append(line)
	f.close()

print("Bot loading [50%]", end = "\r")
bot = commands.Bot(command_prefix='p!')#sets the prefix for the bot.
client = bot
bot.remove_command('help')
@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="p!help"), status=discord.Status("online"), afk=False)
	print("Bot loaded [100%]")
	print("Bot running.")

@bot.command(pass_context = True)
async def help(ctx):
	await bot.say("This is the help command, it is not implemented.")

@bot.command(pass_context = True)
async def Config(ctx, File: str, Property: str, Value: str):
	if str(ctx.message.author) == Sudo_owner:
		print("Not implemented")
	else:
		await bot.say(":warning: Warning: <@" + ctx.message.author.id + "> has insufficient permissions to configure the bot. :warning:")

@bot.command(pass_context = True)
async def AddOwner(ctx, user: discord.Member):
	if str(ctx.message.author) == Sudo_owner:
		if str(user) != Sudo_owner and Owners:
			with open("Owners.txt", "a") as f:
				f.write(str(user) + "\n")
				f.close()
			print("Added " + str(user) + " to the owners list.")
			Owners.append(str(user))
			await bot.say(":ballot_box_with_check: Succsessfully added <@" + str(user.id) + "> to the owners list!")
		else:
			await bot.say(":x: Error: user is already an owner.")
		
	else:
		await bot.say(":warning: Warning: <@" + ctx.message.author.id + "> has insufficient permissions to add owners to the bot. :warning:")

@bot.command(pass_context = True)
async def restart(ctx):
	if str(ctx.message.author) == Sudo_owner:
		await bot.change_presence(game=discord.Game(name="Restarting..."), status=discord.Status("dnd"), afk=False)
		print("Restarting...")
		os.system("start bot.py")
		exit(0)
	else:
		await bot.say(":warning: Warning: <@" + ctx.message.author.id + "> has insufficient permissions to restart the bot. :warning:")
@bot.command(pass_context = True)
async def update(ctx):
	if str(ctx.message.author) == Sudo_owner:
		await bot.change_presence(game=discord.Game(name="Updating..."), status=discord.Status("dnd"), afk=False)
		print("Downloading update from git...")
		os.system("cd C:/Users/%username%/Documents/GitHub/Partnership-Bot/ | git pull | echo.")
		os.system("start bot.py")
		exit(0)
	else:
		await bot.say(":warning: Warning: <@" + ctx.message.author.id + "> has insufficient permissions to update the bot. :warning:")

bot.run(TOKEN)
