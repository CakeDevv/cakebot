import discord
from discord.ext import commands

class Images(commands.Cog):
    """ Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="foto")
    async def get_random_image(self, ctx):
        url_image = "https://cdn.discordapp.com/attachments/1046512645525733386/1046525037554962432/wallpapersden.com_a-fool-moon-night-space-traveler-art_1920x1080.jpg"
        embed = discord.Embed(
            title = "Imagem",
            description = "PS: Resultado da busca da imagem",
            color = 0x0030FF,
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_footer(text= "Feito por: " + self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.add_field(name="API", value="Usamos a API do https://cdn.discordapp.com/attachments/1046512645525733386/1046525037554962432/wallpapersden.com_a-fool-moon-night-space-traveler-art_1920x1080.jpg")
        embed.add_field(name="Parametros", value="{altura}/{largura}")
        embed.add_field(name="Exemplo", value=url_image, inline=False)
        embed.set_image(url=url_image)
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Images(bot))
