import os
from client.bot import breadBot

import commands
import features

with open('.bot-key') as f:
    BOT_KEY = f.read()
BOT_KEY = os.environ.get('BOT_KEY', BOT_KEY)

breadBot.run(BOT_KEY)
