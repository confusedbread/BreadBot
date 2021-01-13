import discord
import logging

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

CHANNEL_ID = 798299047025836163

logging.basicConfig(level=logging.INFO)


async def log(msg, channel_id=CHANNEL_ID):
    channel = bot.get_channel(channel_id)
    await channel.send(msg)


def console_log(msg):
    print(msg)
