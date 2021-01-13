from client.bot import log

RULES_MSG_ID = 798307288463966238
emoji_to_role = {
    745653631264751797: 798316379622604820  # YuekoShock : Kappa
}


async def add_follower(bot, payload):
    if payload.message_id != RULES_MSG_ID:
        return

    role_id = emoji_to_role.get(payload.emoji.id, None)
    if role_id == None:
        # No role for Emoji used
        return

    guild = bot.get_guild(payload.guild_id)
    role = guild.get_role(role_id)

    try:
        await payload.member.add_roles(role)
        await log("Role Successfully Added")
    except Exception:
        print("Something Bad Happened")
        return


async def remove_follower(bot, payload):
    if payload.message_id != RULES_MSG_ID:
        return

    role_id = emoji_to_role.get(payload.emoji.id, None)
    if role_id == None:
        # No role for Emoji used
        return

    guild = bot.get_guild(payload.guild_id)
    role = guild.get_role(role_id)
    member = guild.get_member(payload.user_id)

    try:
        await member.remove_roles(role)
        await log("Role Successfully Removed")
    except Exception:
        print("Something Bad Happened")
        return
