import aiohttp
import discord
from discord.ext import commands
from discord.utils import get
import requests
import json
from utils import *


class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help_command="!verify <toke>",
                      description="Verify your HackTX admission.",
                      help="Verify your HackTX admission.")
    # @commands.cooldown(1, 60, commands.BucketType.user)
    @in_bot_commands()
    async def verify(self, ctx):
        user = ctx.message.author
        msg = ctx.message.content.split(" ")
        token = msg[1]
        data = {'token': token, 'user': user}
        url = 'https://register.hacktx.com/auth/discord/verify_user/'
        # url = 'http://localhost:3000/auth/discord/verify_user/'
        response = requests.post(url, data=data)
        channel = await ctx.author.create_dm()
        if response.ok:
            json_format = json.loads(response.text)
            print(json_format)
            if json_format["status"]["confirmed"] is True:
                print(user.guild.roles)
                if json_format["sponsor"] is True:
                    role = get(user.guild.roles, name="Sponsor")
                else:
                    role = get(user.guild.roles, name="Hacker")
                await user.add_roles(role)
                await channel.send("You have been successfully verified! Happy hacking.")
                await ctx.message.delete()
            else:
                await channel.send("Verification failed. Please contact an organizer if you think this is incorrect.")
                await ctx.message.delete()
        else:
            print(json.loads(response.text))
            await channel.send(json.loads(response.text)["message"])
            await channel.send("Verification failed. Please contact an organizer if you think this is incorrect.")
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(Verify(bot))
