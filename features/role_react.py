from client.bot import log

RULES_MSG_ID = 759172101641994251 # Confusedbread's Oven
emoji_to_role = {
    '🍞' : 759165501472636991,
    '🍝' : 801162743850991636
}


async def add_follower(bot, payload):
    if payload.message_id != RULES_MSG_ID:
        return

    role_id = emoji_to_role.get(
        payload.emoji.id, 
        emoji_to_role.get(payload.emoji.name, None)
    ) 

    if role_id == None:
        return

    guild = bot.get_guild(payload.guild_id)
    role = guild.get_role(role_id)

    try:
        await payload.member.add_roles(role)
        await log("Role Successfully Added")
    except Exception as e:
        print("Something Bad Happened {}".format(e))
        return


async def remove_follower(bot, payload):
    if payload.message_id != RULES_MSG_ID:
        return

    role_id = emoji_to_role.get(
        payload.emoji.id, 
        emoji_to_role.get(payload.emoji.name, None)
    )

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
