from discord.ext import commands

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji_to_role = {
            '🍞' : 759165501472636991,
            '🍝' : 801162743850991636
        }
        self.RULES_MSG_ID = 759172101641994251

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.RULES_MSG_ID:
            return
        
        role_id = self.emoji_to_role.setdefault(
            payload.emoji.id,
            self.emoji_to_role.setdefault(payload.emoji.name, None)
        )

        if role_id == None:
            self.bot.log("Unknown Emoji {}, no role found".format(payload.emoji.name), "INFO")
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            self.bot.log("Guild could not be found id:{}".format(payload.guild_id), "DEBUG")
            return

        role = guild.get_role(role_id)
        if role is None:
            self.bot.log("Role id {} could not be found in guild {}".format(role_id, guild.name), "DEBUG")
            return
        
        try:
            await payload.member.add_roles(role)
            await self.bot.discord_log("Role {} Successfully Added to {}".format(role.name, payload.member.name))
            self.bot.log("Role {} Successfully Added to {}".format(role.name, payload.member.name), "INFO")
        except Exception as e:
            self.bot.log("Error Assigning Role to {}".format(payload.member.name), "ERROR", e)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.RULES_MSG_ID:
            return
        
        role_id = self.emoji_to_role.setdefault(
            payload.emoji.id,
            self.emoji_to_role.setdefault(payload.emoji.name, None)
        )

        if role_id == None:
            self.bot.log("Unknown Emoji {}, no role found".format(payload.emoji.name), "INFO")
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            self.bot.log("Guild could not be found id:{}".format(payload.guild_id), "DEBUG")
            return

        role = guild.get_role(role_id)
        if role is None:
            self.bot.log("Role id {} could not be found in guild {}".format(role_id, guild.name), "DEBUG")
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            self.bot.log(
                "Member({}) id:{} could not be found in guild {}".format(
                    payload.member.name,
                    payload.user_id,
                    guild.name
                )
            )
            return 

        try:
            await member.remove_roles(role)
            await self.bot.discord_log("Role {} Successfully Removed from {}".format(role.name, member.name))
            self.bot.log("Role {} Successfully Removed from {}".format(role.name, member.name), "INFO")
        except Exception as e:
            self.bot.log("Error Removing Role to {}".format(payload.member.name), "ERROR", e)
