from discord.ext import commands


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count = 0

    @commands.command(help_command="!ansh",
                      description="hehehe",
                      help="hehehe")
    @commands.cooldown(1, 600, commands.BucketType.user)
    @commands.check_any(commands.has_role("Organizer"))
    async def ansh(self, ctx):
        ansh = self.bot.get_user(520856194190147595)
        # ansh = self.bot.get_user(173263365777522688)
        dm = await ansh.create_dm()
        await dm.send("Get anshed hehehehehehe")
        self.count += 1
        await ctx.send("Ansh has been disturbed %d times" % self.count)


def setup(bot):
    bot.add_cog(Troll(bot))
