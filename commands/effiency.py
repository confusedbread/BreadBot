from commands import bot
from utils.shanten import calculate_shanten
from utils.hand_to_emoji import hand_to_emoji

@bot.command(name='eff')
async def effiency(ctx, hand=None):
    if not hand:
        await ctx.send("Invalid Hand {}".format(hand))

    emoji_hand = hand_to_emoji(hand)
    shanten = calculate_shanten(hand)
    await ctx.send("{} \n Shanten-{}".format(emoji_hand, shanten))
