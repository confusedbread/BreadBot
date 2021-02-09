import discord
from discord.ext import commands
import logging


intents = discord.Intents.default()
intents.members = True
intents.presences = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', description='beep boop bot', intents=intents)
        self._DISCORD_LOG_CHANNEL_ID = 765949576796176424
        self._logger = self._init_logger()

    def _init_logger(self):
        logger = logging.getLogger('discord')
        logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

        return logger

    async def discord_log(self, msg, channel_id=None):
        if not channel_id:
            channel_id = self._DISCORD_LOG_CHANNEL_ID

        channel = self.get_channel(channel_id)
        await channel.send(msg)

    async def log(self, msg, level='INFO', e=None):
        if level == 'INFO':
            self._logger.info(msg)
        elif level == 'DEBUG':
            self._logger.debug(msg)
        elif level == 'WARNING':
            self._logger.warning(msg)
        else:
            self._logger.error(msg, e)

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
        await self.discord_log('Bread Bot Reporting for Duty!')


breadBot = Bot()