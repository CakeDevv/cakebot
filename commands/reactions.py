import discord
from discord.ext import commands

class Reactions(commands.Cog):
    """ React with user"""
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "🤨":
            role = user.guild.get_role(1046511061236465754)
            await user.add_roles(role)        

async def setup(bot):
    await bot.add_cog(Reactions(bot))
