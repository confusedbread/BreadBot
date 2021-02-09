from commands import bot

@bot.command()
async def pet(ctx, to_pet=None):

    if not to_pet:
        return

    if to_pet == 'bot' or to_pet == 'breadbot':
        eliisa_emoji = ctx.bot.get_emoji(804134994871189504)
        await ctx.send(str(eliisa_emoji))
