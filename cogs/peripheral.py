import discord
from discord.ext import commands
from discord.utils import get
from utils import *


class Peripheral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = 839627125577351168
        user = payload.user_id
        member = payload.member
        
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
        role = get(member.guild.roles, name="Hacker")
        
        if not payload.guild_id:
            return

        if payload is not None:
            if payload.message_id == message_id:
                if str(payload.emoji) == "✅":
                    await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = 839627125577351168
        user = payload.user_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
        member = await guild.fetch_member(payload.user_id)
        role = get(member.guild.roles, name="Hacker")

        if not payload.guild_id:
            return

        if payload is not None:
            print(payload.message_id)
            if payload.message_id == message_id:
                if str(payload.emoji) == "✅":
                    await member.remove_roles(role)
        

def setup(bot):
    bot.add_cog(Peripheral(bot))