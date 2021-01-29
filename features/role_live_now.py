from client.bot import log

LIVE_NOW_ROLE_ID = 804029421488046160

async def update_live_now(bot, before, after):

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

    if was_streaming and now_streaming:
        return
    elif not was_streaming and not now_streaming:
        return 

    role = after.guild.get_role(LIVE_NOW_ROLE_ID)

    try:
        if was_streaming and not now_streaming:
            await after.remove_roles(role)
            await log("Member {} is no longer live".format(after.name))
        elif not was_streaming and now_streaming:
            await after.add_roles(role)
            await log("Member {} is now live".format(after.name))
    except Exception:
        print("Unable to assign/remove Live Now Role")
        return

async def check_live_status(bot):

    for guild in bot.guilds:

        live_members = []
        not_live_members = []
        role = guild.get_role(LIVE_NOW_ROLE_ID)

        if not role:
            continue

        for member in guild.members:
            streaming = False

            if member.name == 'Streamcord':
                continue

            for activity in member.activities:
                if activity.type.name == 'streaming':
                    streaming = True
                    live_members.append(member)
                    break

            if role in member.roles:
                if not streaming:
                    not_live_members.append(member)

        try:
            for member in live_members:
                await member.add_roles(role)
                await log("Member {} is now live".format(member.name))
            
            for member in not_live_members:
                await member.remove_roles(role)
                await log("Member {} is no longer live".format(member.name))

        except Exception as e:
            print(e)
            print("Unable to assign/remove Live Now Role")
            return
