import discord
from discord.ext import commands
import os
import asyncio
from decouple import config

TOKEN = config("TOKEN")

bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')

async def load_extensions():
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")
    for file in os.listdir("tasks"):
        if file.endswith(".py"):
            await bot.load_extension(f"tasks.{file[:-3]}")
    for file in os.listdir("music"):
        if file.endswith(".py"):
            await bot.load_extension(f"music.{file[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())

load_extensions(bot)

bot.run(TOKEN)