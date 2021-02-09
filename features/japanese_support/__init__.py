from client.bot import breadBot as bot
from .hiragana_helper import JapaneseSupport


bot.add_cog(JapaneseSupport(bot))
