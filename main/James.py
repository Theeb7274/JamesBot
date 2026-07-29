# Import stuff we need
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

stuff = ""
jamesID = 
fishID = 

load_dotenv() # Pull env variables from .env
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"It's James Time, for my name is {bot.user.name}")
        
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "james" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} dont use that word")

    if random.random() < 0.01:
        await message.add_reaction(stuff)
        # await message.channel.send(f"{message.author.mention} Silence")

    if "say that again" in message.content.lower() or "what are we some kind of" in message.content.lower():
        await message.channel.send("https://tenor.com/view/say-that-again-gif-968943876633031890")

    if "hello" in message.content.lower():
        await message.channel.send("https://tenor.com/view/smiling-friends-mr-frog-adult-swim-mr-frog-for-president-coming-to-get-you-gif-9163994796921148334")

    await bot.process_commands(message)

@bot.command()
async def bonk(ctx):
    await ctx.send(f"BONK {ctx.author.mention}!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG) # Runs the bot
