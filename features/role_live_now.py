from discord.ext import commands


class LiveNow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.LIVE_NOW_ROLE_ID = 804029421488046160

    async def set_role_live_now(self, member, role):
        try:
            await member.add_roles(role)
            await self.bot.discord_log("Member {} is now live".format(member.name))
            await self.bot.log("Member {} assigned {} role".format(member.name, role.name))
        except Exception as e:
            err_msg = "Failed to assign role {} to member {}.".format(
                role.name, member.name)
            await self.bot.log(err_msg, "ERROR", e)
        return

    async def remove_role_live_now(self, member, role):
        try:
            await member.remove_roles(role)
            await self.bot.discord_log("Member {} is no longer live".format(member.name))
            await self.bot.log("{} role removed from member {}".format(role.name, member.name))
        except Exception as e:
            err_msg = "Failed to remove role {} to member {}.".format(
                role.name, member.name)
            await self.bot.log(err_msg, "ERROR", e)
        return

    @commands.Cog.listener()
    async def on_member_update(self, before, after):

        was_streaming = None
        now_streaming = None

        for activity in before.activities:
            if activity.type.name == 'streaming':
                was_streaming = True
                break

        for activity in after.activities:
            if activity.type.name == 'streaming':
                now_streaming = True
                break

        if (was_streaming and now_streaming) or (not was_streaming and not now_streaming):
            return

        role = after.guild.get_role(self.LIVE_NOW_ROLE_ID)
        if role is None:
            await self.bot.log("Live now could not be found in guild {}".format(after.guild.name), "DEBUG")
            return

        if was_streaming and not now_streaming:
            await self.remove_role_live_now(after, role)
        elif not was_streaming and now_streaming:
            await self.set_role_live_now(after, role)

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:

            live_members = []
            not_live_members = []
            blacklist = ['Streamcord']

            role = guild.get_role(self.LIVE_NOW_ROLE_ID)

            if not role:
                continue

            for member in guild.members:
                streaming = False

                if member.name in blacklist:
                    continue

                for activity in member.activities:
                    if activity.type.name == 'streaming':
                        streaming = True
                        live_members.append(member)
                        break

                if role in member.roles:
                    if not streaming:
                        not_live_members.append(member)

            for member in live_members:
                await self.set_role_live_now(member, role)

            for member in not_live_members:
                await self.remove_role_live_now(member, role)
