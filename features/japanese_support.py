from discord.ext import commands
import pykakasi


class JapaneseSupport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.jp_channels = [804115491047079966]
        self.KKS = pykakasi.kakasi()

    def translate_hiragana(self, msg):

        no_kanji = True
        hiragana_help_str = ""
        transliterate_str = self.KKS.convert(msg)

        for phrase in transliterate_str:
            if phrase['orig'] == phrase['hira'] or phrase['orig'] == phrase['kana']:
                hiragana_help_str += "{}  ".format(phrase['orig'])
        else:
            no_kanji = False
            hiragana_help_str += "{}[{}]  ".format(
                phrase['orig'], phrase['hira'])

        if no_kanji:
            return ""
        else:
            return hiragana_help_str

    @commands.Cog.listener()
    async def on_message(self, msg):
        ctx = await self.bot.get_context(msg)

        if ctx.valid:
            return
    
        if msg.author.bot:
            return 

        if msg.channel.id not in self.jp_channels:
            return

        jp_str = msg.content
        hiragana_help_str = self.translate_hiragana(jp_str)

        if hiragana_help_str:
            try:
                await msg.channel.send(hiragana_help_str)
            except Exception as e:
                await self.bot.log("Error Sending Hira JP {}".format(hiragana_help_str), "Error", e)

    @commands.command(name='rom')
    async def translate_romaji(self, ctx, *, jp_str=None):
        if not jp_str:
            await ctx.send("Nothing to translate here.")
            return

        transliterate_str = self.KKS.convert(jp_str)
        romaji_help_str = ""

        for phrase in transliterate_str:
            romaji_help_str += "{}[{}] ".format(
                phrase['orig'], phrase['hepburn'])

        try:
            await ctx.send(romaji_help_str)
        except Exception as e:
            await self.bot.log("Error Sending Romaji JP {}".format(romaji_help_str), "Error", e)

    @commands.command(name='hira')
    async def hira_command(self, ctx, *, jp_str=None):
        if not jp_str:
            await ctx.send("Nothing to translate here.")
            return

        hiragana_help_str = self.translate_hiragana(jp_str)

        if not hiragana_help_str:
            hiragana_help_str = "There's no Kanji here."

        try:
            await ctx.channel.send(hiragana_help_str)
        except Exception as e:
            await self.bot.log("Error Sending Hira JP {}".format(hiragana_help_str), "Error", e)

    @commands.command(name='jpmode')
    async def jp_mode_toggle(self, ctx):
        confirmation_str = ""
        if ctx.channel.id in self.jp_channels:
            self.jp_channels.remove(ctx.channel.id)
            confirmation_str = "JP Mode Off"
        else:
            self.jp_channels.append(ctx.channel.id)
            confirmation_str = "JP Mode On"

        try:
            await ctx.send(confirmation_str)
        except Exception as e:
            await self.bot.log("Error Replying JP Mode", "ERROR", e)
