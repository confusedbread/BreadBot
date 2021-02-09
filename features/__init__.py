from client.bot import breadBot as bot
from features.role_react import ReactionRoles
from features.role_live_now import LiveNow
from features.japanese_support import JapaneseSupport

bot.add_cog(ReactionRoles(bot))
bot.add_cog(LiveNow(bot))
bot.add_cog(JapaneseSupport(bot))