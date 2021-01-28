from client.bot import log

async def pet(bot, message):
    
    args = message.content.split()

    if len(args) != 2:
        return

    args[1] = args[1].lower()

    if args[1] == 'bot' or args[1] == 'breadbot':
        eliisa_emoji = bot.get_emoji(804134994871189504)
        await message.channel.send(str(eliisa_emoji))