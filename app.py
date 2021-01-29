import os
from features import role_react, role_live_now
from client.bot import bot, log

from commands import simple_commands
from features import japanese_support

with open('.bot-key') as f:
    BOT_KEY = f.read()
BOT_KEY = os.environ.get('BOT_KEY', BOT_KEY)

commands_lookup = {}

commands_lookup.update(simple_commands)
commands_lookup.update(japanese_support.commands)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await log('Bread Bot Reporting for Duty!')
    await role_live_now.check_live_status(bot)



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #Message is empty. Example: picture
    if not message.content:
        return 

    first_arg = message.content.split()[0]
    
    if commands_lookup.setdefault(first_arg, None) != None:
        await commands_lookup[first_arg](bot, message)
    else:
        await japanese_support.translate(bot, message)


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
