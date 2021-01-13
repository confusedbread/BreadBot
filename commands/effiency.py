from client.bot import log
from utils.shanten import calculate_shanten
from utils.hand_to_emoji import hand_to_emoji

async def effiency(bot, message):
    
    args = message.content.split()

    if len(args) != 2:
        await message.channel.send('Invalid Number are elements sent')

    hand = args[1]

    emoji_hand = hand_to_emoji(hand)
    shanten = calculate_shanten(hand)
    await message.channel.send("{} \n Shanten-{}".format(emoji_hand, shanten))