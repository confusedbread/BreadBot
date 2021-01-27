from client.bot import log
from ..kakasi import KKS

async def romaji(bot , message):

    msg_list = message.content.split()

    if len(msg_list) < 2:
        await message.channel.send('Invalid Number of Args')
        return 
    
    msg = "".join(msg_list[1:])

    transliterate_str = KKS.convert(msg)
    romaji_help_str = ""

    for phrase in transliterate_str:
        romaji_help_str += "{}[{}] ".format(phrase['orig'], phrase['hepburn'])

    try:
        await message.channel.send(romaji_help_str)
    except Exception as e:
        print("Something Bad Happened {}".format(e))
        return 