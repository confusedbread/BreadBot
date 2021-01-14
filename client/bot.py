import discord
import logging

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

CHANNEL_ID = 765949576796176424

logging.basicConfig(level=logging.INFO)


async def log(msg, channel_id=CHANNEL_ID):
    channel = bot.get_channel(channel_id)
    await channel.send(msg)


def console_log(msg):
    print(msg)
