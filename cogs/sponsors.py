from discord.ext import commands
from discord.utils import get
import discord

class Sponsors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help_command="!likewize",
                      description="Learn about Likewize who helped host this event!",
                      help="Learn about Likewize who helped host this event!")
    async def likewize(self, ctx):
        await ctx.send("Likewize is setting the standards in customer experience through solving technology problems. Whether a customer needs to report a lost, stolen, damaged, or malfunctioning device, is in need of an upgrade, or just needs support in how to use their technology - Likewise has a solution and is working to enhance these offerings and experiences every day.")

    @commands.command(help_command="!matrix",
                      description="Learn about Matrix who helped host this event!",
                      help="Learn about Matrix who helped host this event!")
    async def matrix(self, ctx):
        await ctx.send("Matrix is a gamified platform for content creators, esport teams, and other digital brands. Brands are able to create quests, which fans complete to earn NFT prizes. However, this is only the first step. Matrix seeks to democratize entertainment, by rewarding fans with ownership in the brands that they participate in. Matrix recently raised $3.5M from investors such as Samsung, Warner Music Group, Galaxy, and others. They are hiring for a myriad of roles, including frontend developers, backend developers, and designers!")

    @commands.command(help_command="!gcp",
                      description="Learn about Google Cloud Platform who helped host this event!",
                      help="Learn about Google Cloud Platform who helped host this event!")
    async def gcp(self, ctx):
        await ctx.send("Google Cloud Platform, offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail, Google Drive, and YouTube.")
    
    @commands.command(help_command="!devrev",
                      description="Learn about DevRev who helped host this event!",
                      help="Learn about DevRev who helped host this event!")
    async def devrev(self, ctx):
        await ctx.send("Coming soon...")

    @commands.command(help_command="!linode",
                      description="Learn about Linode who helped host this event!",
                      help="Learn about Linode who helped host this event!")
    async def linode(self, ctx):
        await ctx.send("Linode accelerates innovation with simple, affordable, and accessible Linux cloud solutions and service.  Easily launch and enrich applications, hosted services, websites, AI & machine learning workloads, gaming services, and more! Before the hackathon, sign up for $20 in free credit to use towards your project. Getting started is simple. Sign up here: https://login.linode.com/sigmup?promo=HACK21 to create your account. Your $20 credit will be applied automatically upon new account creation. Not sure where to start? Check out our docs page: https://www.linode.com/docs/ and our Getting Started Guide: https://www.linode.com/docs/guides/getting-started/.")

    @commands.command(help_command="!prizes ",
                      description="Learn about the prizes and challenges!",
                      help="Learn about the prizes and challenges!")
    async def prizes(self, ctx):
        embed = discord.Embed(description="Prizes", colour=discord.Colour.dark_purple())
        embed.add_field(name="Overall", value="Prompt: The project with the best overall hack in terms of presentation, implementation (frontend and backend), and societal impact.", inline=False)
        embed.add_field(name="First Place", value="Facebook Portals to each team member", inline=False)
        embed.add_field(name="Second Place", value="Prize of choosing of up to $100 to each team member", inline=False)
        embed.add_field(name="Third Place", value="Prize of choosing of up to $50 to each team member", inline=False)
        embed.add_field(name="GCP", value="--------------------", inline=False)
        embed.add_field(name="PROMPT: Best Use of Google Cloud category challenge", value="Use one  or more Google Cloud products in your hackathon project (Firebase and Maps API count).", inline=False)
        embed.add_field(name="First Place", value="Google Cloud branded backpack", inline=False)
        embed.add_field(name="Second Place", value="Google Cloud Swag Box", inline=False)
        embed.add_field(name="Likewize", value="--------------------", inline=False)
        embed.add_field(name="PROMPT", value="Design a software component that will in real-time identify the emotions of a customer via voice recognition. The software should gauge the emotion of the customer : whether a  customer is satisfied or happy or agitated or angry or frustrated. The thresholds for each emotion should be configurable. The web service can be stubbed out and need not be implemented.", inline=False)
        embed.add_field(name="PRIZES", value="First place winners will receive Likewize branded FitBits", inline=False)
        embed.add_field(name="Matrix", value="--------------------", inline=False)
        embed.add_field(name="PROMPT", value="Implement Solidity in some way in your project, team that implements solidity with the best real life application in crypto wins. ", inline=False)
        embed.add_field(name="1st Place", value="Entire team will receive $500 worth of ETH that they can distribute amongst themselves", inline=False)
        embed.add_field(name="2nd Place", value="Entire team will receive $250 worth of ETH that they can distribute amongst themselves", inline=False)
        embed.add_field(name="3rd Place", value=" Entire team will receive $100 worth of ETH that they can distribute amongst themselves", inline=False)

        await ctx.send(embed=embed) 



    @commands.command(help_command="!sponsor",
                      description="Learn about our sponsors!",
                      help="Learn about our sponsors!")
    async def sponsor(self, ctx):
        await ctx.send("Use !likewize, !matrix, !devrev or !gcp to learn more")



def setup(bot):
    bot.add_cog(Sponsors(bot))

