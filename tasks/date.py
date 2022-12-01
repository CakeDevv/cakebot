import discord
import datetime
from discord.ext import commands,tasks

class Date(commands.Cog):
    """ React with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("O bolo acabou de sair do forno")
        self.current_time.start()
    @tasks.loop(hours=1)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y as %H:%M:%S")
        channel = self.bot.get_channel(1046496232870248488)
        await channel.send("Data atual: " + now)

async def setup(bot):
    await bot.add_cog(Date(bot))