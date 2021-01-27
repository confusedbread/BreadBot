import pykakasi
from client.bot import log
from .kakasi import KKS

HIHONGO_CHANNEL_ID = 804115491047079966

async def translate(bot, payload):

    if payload.channel.id != HIHONGO_CHANNEL_ID:
        return

    msg = payload.content
    no_kanji = True
    hiragana_help_str = ""

    transliterate_str = KKS.convert(msg)

    for phrase in transliterate_str:
        if phrase['orig'] == phrase['hira'] or phrase['orig'] == phrase['kana'] :
            hiragana_help_str += "{}  ".format(phrase['orig'])
        else:
            no_kanji = False
            hiragana_help_str += "{}[{}]  ".format(phrase['orig'], phrase['hira'])

    if not no_kanji:
        try:
            await payload.channel.send(hiragana_help_str)
        except Exception as e :
            print("Something Bad Happened {}".format(e))
            return
