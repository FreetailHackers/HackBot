from discord.ext import commands
from discord.utils import get
import discord
import datetime


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help_command="!unload <cog>", description="Unload a cog")
    @commands.has_role("Tech")
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload cog")
            print(e)
            return
        await ctx.send("Cog unloaded")

    @commands.command(help_command="!load <cog>", description="Load a cog")
    @commands.has_role("Tech")
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load cog")
            print(e)
            return
        await ctx.send("Cog loaded")

    @commands.command(help_command="!reload <cog>", description="Reload a cog")
    @commands.has_role("Tech")
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not reload cog")
            return
        await ctx.send("Cog reloaded")

    @commands.command(help_command="!stats", description="Get server stats")
    @commands.has_role("Organizer")
    async def stats(self, ctx):
        guild = ctx.guild
        num_voice_channels = len(guild.voice_channels)
        num_text_channels = len(guild.text_channels)
        embed = discord.Embed(description="Server Stats", colour=discord.Colour.dark_purple())
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        online = 0
        verified = 0
        unverified = 0
        total = 0
        mentors = 0
        sponsors = 0
        hacker = get(guild.roles, name="Hacker")
        mentor = get(guild.roles, name="Mentor")
        sponsor = get(guild.roles, name="Sponsor")
        members = guild.members
        for member in members:
            # print("%s's status: %s" % (member, member.status))
            if member.status != discord.Status.offline and not member.bot:
                online += 1
            if hacker in member.roles:
                verified += 1
            if sponsor in member.roles:
                sponsors += 1
            if mentor in member.roles:
                mentors += 1
            if not member.bot:
                total += 1
            if len(member.roles) == 1:
                unverified += 1
        embed.add_field(name="Online members", value=str(online))
        embed.add_field(name="Total members", value=str(total))
        embed.add_field(name="--------------------", value="--------------------", inline=False)
        embed.add_field(name="Verified hackers", value=str(verified))
        embed.add_field(name="Unverified hackers", value=str(unverified))
        embed.add_field(name="--------------------", value="--------------------", inline=False)
        embed.add_field(name="Mentors", value=str(mentors))
        embed.add_field(name="Sponsors", value=str(sponsors))

        # embed.add_field(name="# Voice Channels", value=str(num_voice_channels), inline=False)
        # embed.add_field(name="# Text Channels", value=str(num_text_channels))
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=str(datetime.datetime.now()))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
