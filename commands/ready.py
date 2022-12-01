import discord
from discord.ext import commands

class Ready(commands.Cog):
    """ React with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if 'puta' in message.content:
            await message.channel.send("Para de xingar krl")
        if 'nao' in message.content:
            await message.channel.send("Meu pau na sua mao")
        if 'guri' in message.content:
            await message.channel.send("Gurista")
        if 'haru' in message.content:
            await message.delete()
            await message.channel.send(f"Sem polemicas {message.author.name}")
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Ready(bot))
