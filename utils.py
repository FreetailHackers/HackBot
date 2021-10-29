import random
import json
import os
from settings_files import *
import discord
from discord.ext import commands
from asyncio import TimeoutError
from discord.utils import get


def in_bot_commands():
    def predicate(ctx):
        user = ctx.message.author
        role = get(user.guild.roles, name="Organizer")
        return ctx.message.channel.name == "bot-commands" or (role in ctx.author.roles)
    return commands.check(predicate)


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

left = "⬅"
right = "➡"


async def paginate_embed(bot, channel, embeds):
    """
    async def modifier_func(type, curr_page) type: 1 for forward, -1 for backward.
    """
    total_pages = len(embeds)

    curr_page = 0

    og_msg = await channel.send(embed=embeds[curr_page].set_footer(text=f"Page {curr_page+1}/{total_pages}"))
    if total_pages <= 1:
        return

    await og_msg.add_reaction(left)
    await og_msg.add_reaction(right)

    def check(reaction, user):
        return not user.bot and reaction.message.channel == channel and reaction.message.id == og_msg.id

    try:
        while True:
            reaction, user = await bot.wait_for("reaction_add", timeout=120.0, check=check)
            if str(reaction.emoji) == right:
                if curr_page < total_pages - 1:
                    curr_page += 1
                    await og_msg.edit(embed=embeds[curr_page].set_footer(text=f"Page {curr_page+1}/{total_pages}"))
                await og_msg.remove_reaction(right, user)
            elif str(reaction.emoji) == left:
                if curr_page > 0:
                    curr_page -= 1
                    await og_msg.edit(embed=embeds[curr_page].set_footer(text=f"Page {curr_page+1}/{total_pages}"))
                await og_msg.remove_reaction(left, user)
            else:
                continue
    except TimeoutError:
        await og_msg.remove_reaction(left, bot.user)
        await og_msg.remove_reaction(right, bot.user)
        return


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)


def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

    return text


async def create_channel(guild, author, users):
    private_category = None
    for category in guild.categories:
        if category.name == "Private Voice Channels":
            private_category = category
            break
    if private_category is None:
        return
    channel_name = "%s's room" % author.name
    for channel in guild.voice_channels:
        if channel.name == channel_name.lower():
            await channel.delete()
            break
    await guild.create_voice_channel(channel_name, category=private_category)
    private_channel = None
    for channel in guild.voice_channels:
        if channel.name == channel_name.lower():
            private_channel = channel
            break
    if private_channel is None:
        return
    hacker_role = None
    for role in guild.roles:
        if role.name == "Hacker":
            hacker_role = role
            break
    if hacker_role is None:
        hacker_role = guild.default_role
    await private_channel.set_permissions(guild.default_role, view_channel=False, send_messages=False)
    await private_channel.set_permissions(hacker_role, view_channel=False, send_messages=False)
    await private_channel.set_permissions(author, view_channel=False, send_messages=False)
    for user in users:
        await private_channel.set_permissions(user, view_channel=True, send_messages=True)
    return private_channel
