import discord
from discord.ext import commands

class Music(commands.Cog):
    """ React with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    @commands.command
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Music(bot))
