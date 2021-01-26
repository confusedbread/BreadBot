import discord
import logging

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

CHANNEL_ID = 765949576796176424

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

#Logs to discord logs Channel
async def log(msg, channel_id=CHANNEL_ID):
    channel = bot.get_channel(channel_id)
    await channel.send(msg)


def info_log(msg):
    logger.info(msg)


def debug_log(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg, e):
    logger.error(msg, e)
