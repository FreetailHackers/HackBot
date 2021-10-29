import os
import discord
from discord.ext import commands
from settings import *

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

for file in os.listdir("./cogs"):
    if file.endswith(".py") and file != "__init__.py":
        bot.load_extension(f'cogs.{file[:-3]}')

bot.run(DISCORD_TOKEN)
