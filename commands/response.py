import discord
from discord.ext import commands

class Response(commands.Cog):
    """ Response user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        match message.content:
            case("puta"):
                return message.channel.send("Para de xingar krl")
            case("nao"):
                return message.channel.send("Meu pau na sua mao")
            case("guri"):
                return message.channel.send("Gurista")   
            case("haru"):
                return message.channel.send(f"Sem polemicas aqui {message.author.name}")
                await message.delete()
            case("livia"):
                return message.channel.send(f"Sem polemicas aqui {message.author.name}")
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Response(bot))
