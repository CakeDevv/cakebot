import discord
from discord.ext import commands

class Talks(commands.Cog):
    """ Talks with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="iae")
    async def send_hello(self, ctx):
        name = ctx.author.name
        resposta = 'Iae, ' + name
        await ctx.send(resposta)
    @commands.command(name='bolo')
    async def secret(self, ctx):
        try:
            await ctx.author.send("Você ganhou um bolo 🍰")
        except discord.errors.Forbiden:
            await ctx.send("Não posso te dar um bolo, habilite enviar mensagens")
            
async def setup(bot):
   await bot.add_cog(Talks(bot))
