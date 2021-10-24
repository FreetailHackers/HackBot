from datetime import timedelta, timezone as tz, datetime as dt
from functools import partial

from utils import *

import discord
from discord.ext import commands

# hackathon time zone
cst = tz(timedelta(hours=-5))  # cst is 5h behind utc

# hackathon start and end times
start = dt.fromtimestamp(1635613200, tz=cst)  # 12pm cst oct 30 2021
end = dt.fromtimestamp(1635699600, tz=cst)  # 12pm cst oct 31 2021

austin = partial(dt.now, tz=cst)  # gives current time in austin, use instead of dt.now() for uniformity

# October 30-31, 2021
# event format is (time, event name, event link if available)
sched = {
    30: [
        ("10:00 am", "Breakfast Served", ""),
        ("11:00 am", "Opening Ceremony", ""),
        ("11:00 am", "Intro to Git (GDC 5.302)", ""),
        ("12:00 pm", "Hacking Starts", ""),
        ("12:00 pm", "Intro to Python (GDC 5.302)", ""),
        ("1:00 pm", "Team Matching", ""),
        ("1:00 pm", "Intro to App Dev (GDC 5.302)", ""),
        ("2:00 pm", "Intro to Web Dev (GDC 5.302)", ""),
        ("3:00 pm", "Hackathon Olympics (GDC Courtyard)", ""),
        ("4:00 pm", "How to Recruit (GDC 5.302)", ""),
        ("8:00 pm", "Resume Reviews (GDC 5.302)", ""),
        ("9:00 pm", "Smash Bros Ultimate Tourney (GDC 5.302)", ""),
        ("10:00 pm", "Karaoke/Movie Night (GDC 5.302)", ""),
    ],
    31: [
        ("11:00 am", "Office Hours", ""),
        ("12:00 pm", "Hacking Ends", ""),
        ("12:00 pm", "Lunch Served", ""),
        ("1:00 pm", "Judging Starts", ""),
        ("3:00 pm", "Judging Ends", ""),
        ("4:00 pm", "Closing Ceremony (GDC 2.216)", ""),
    ],
}


def time_left(event):
    # returns string with duration composed
    diff = event - austin()
    d = diff.days
    h, m = divmod(diff.seconds, 3600)  # 3600 seconds in an hour
    m, s = divmod(m, 60)

    return (
        (f"{d} day{'s' * bool(d - 1)}, " if d else "")
        + (f"{h} hour{'s' * bool(h - 1)}, " if h else "")
        + (f"{m} minute{'s' * bool(m - 1)}" if m else "")
    )


def time_elapsed(event):
    # returns string with time since event started
    diff = austin() - event
    d = diff.days
    h, m = divmod(diff.seconds, 3600)  # 3600 seconds in an hour
    m, s = divmod(m, 60)

    return (
        (f"{d} day{'s' * bool(d - 1)}, " if d else "")
        + (f"{h} hour{'s' * bool(h - 1)}, " if h else "")
        + (f"{m} minute{'s' * bool(m - 1)}" if m else "")
    )


class Times(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 60, commands.BucketType.user)
    @in_bot_commands()
    @commands.command(name="when",
                      help_command="!when",
                      description="Check when the hackathon starts or ends",
                      help="Check when the hackathon starts or ends"
                      )
    async def hack_times(self, ctx):
        if start > austin():
            event = start  # hackathon yet to start
        else:
            event = end  # hackathon started so give time till end
        if austin() > end:
            breakdown = "HackTX 2021 has ended. Come back next year :))"
        else:
            # compose string accordingly
            breakdown = (
                "HackTX 2021 " + ("begins " if start > austin() else "ends ") + "in " + time_left(event)
            )

        await ctx.send(breakdown)

    @commands.cooldown(1, 60, commands.BucketType.guild)
    @in_bot_commands()
    @commands.command(name="schedule",
                      help_command="!schedule",
                      description="See the hackathon schedule",
                      help="See the hackathon schedule"
                      )
    async def schedule(self, ctx):
        embeds = []

        for day, events in sched.items():
            if day >= austin().day:
                full_day = ["Saturday", "Sunday"][day - 30]  # 30 since that was the first day

                embed = discord.Embed(
                    title="HackTX 2021 Schedule :scroll:",
                    description=f"**{full_day}, October {day}** \nso much fun to be had :')",
                    color=discord.Colour.dark_purple(),
                )

                for num, event in enumerate(events):
                    event_time, event_name, link = event
                    left = dt.strptime(f"2021 Oct {day} {event_time}", "%Y %b %d %I:%M %p").replace(tzinfo=cst)
                    if left > austin():  # check if event hasn't already passed
                        embed.add_field(
                            name=f"{num + 1}. {event_name} at {event_time}",
                            value=(f"in {time_left(left)} CT" + (f", [**link**]({link})" if link else "")),
                            inline=False,
                        )

                embeds.append(embed)

        await paginate_embed(self.bot, ctx.channel, embeds)

    @commands.cooldown(1, 60, commands.BucketType.guild)
    @in_bot_commands()
    @commands.command(name="soon",
                      help_command="!soon",
                      description="Check on upcoming events.",
                      help="Check on upcoming events."
                      )
    async def soon(self, ctx):
        embeds = []

        val = 1
        for day, events in sched.items():
            if day >= austin().day:
                full_day = ["Saturday", "Sunday"][day - 8]  # 8 since that was the first day

                embed = discord.Embed(
                    title="Upcoming Events! :alarm_clock:",
                    description="See what's happening in the next hour!",
                    color=discord.Colour.dark_purple(),
                )

                #assumes events in list are in chronological order
                for num, event in enumerate(events):
                    event_time, event_name, link = event
                    left = dt.strptime(f"2021 Oct {day} {event_time}", "%Y %b %d %I:%M %p").replace(tzinfo=cst)
                    if left > austin(): #check that event hasn't passed
                        if (dt.__sub__(left, austin()).total_seconds()) <= 60:  # event happening in the next minute
                            text = f"{event_name} starting now!"
                            embed.add_field(
                                name=f"{val}. {event_name} at {event_time} CT",
                                value=("in < 1 minute" + (f", [**link**]({link})" if link else "")),
                                inline=False,
                            )
                        elif (dt.__sub__(left, austin()).total_seconds()) <= 3600:  # event happening in the next hour 
                            embed.add_field(
                                name=f"{val}. {event_name} at {event_time} CT",
                                value=(f"in {time_left(left)}" + (f", [**link**]({link})" if link else "")),
                                inline=False,
                            )
                            val = val + 1
                        else: 
                            break

                if val == 1: 
                    embed.add_field(
                        name="No upcoming events!",
                        value="Check the schedule to see future events.",
                        inline=False,
                    )
                embeds.append(embed)
                break
        await paginate_embed(self.bot, ctx.channel, embeds)

    @commands.cooldown(1, 60, commands.BucketType.guild)
    @in_bot_commands()
    @commands.command(name="time",
                      help_command="!time",
                      description="Check when a certain event is",
                      help="Check when a certain event is"
                      )
    async def time(self, ctx, *, contents):

        text = "Oops! This event isn't on the schedule!" 
        for day, events in sched.items():

            for num, event in enumerate(events):
                event_time, event_name, link = event             
                if(contents == event_name):
                    left = dt.strptime(f"2021 Oct {day} {event_time}", "%Y %b %d %I:%M %p").replace(tzinfo=cst)
                    if left > austin(): # check if event hasn't already passed 
                        text = f"{event_name} starts at {event_time} CT (in {time_left(left)})"
                        # if event is starting within one minute, otherwise 
                        if (dt.__sub__(left, austin()).total_seconds()) <= 60:  
                            text = f"{event_name} starts now at {event_time} CT!"

                    else:
                        text = f"{event_name} has already passed! Try the \"!soon\" command to see what's coming up."
                        #event might be going on if it started within 2 hrs ago
                        if (dt.__sub__(austin(), left).total_seconds()) <= (2*3600): 
                            text = f"{event_name} started at {event_time} CT ({time_elapsed(left)} ago)!"


                    break
 
        await ctx.send(text)


def setup(bot):
    bot.add_cog(Times(bot))
