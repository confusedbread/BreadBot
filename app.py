import os
from features import role_react, role_live_now
from client.bot import bot, log
from commands.effiency import effiency
from features.japanese_support import hiragana_helper
from features.japanese_support.commands.romaji import romaji


with open('.bot-key') as f:
    BOT_KEY = f.read()
BOT_KEY = os.environ.get('BOT_KEY', BOT_KEY)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await log('Bread Bot Reporting for Duty!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! Me Bot {}'.format('🀇'))
    #Temp Commands Fix Later
    elif message.content.startswith('!eff'):
        await effiency(bot, message)
    elif message.content.startswith('!rom'):
        await romaji(bot, message)
    else:
        await hiragana_helper.translate(bot, message)


@bot.event
async def on_member_update(before, after):
    await role_live_now.update_live_now(bot, before, after)


@bot.event
async def on_raw_reaction_add(payload):
    await role_react.add_follower(bot, payload)


@bot.event
async def on_raw_reaction_remove(payload):
    await role_react.remove_follower(bot, payload)

bot.run(BOT_KEY)
