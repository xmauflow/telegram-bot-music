#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters, enums
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from cilik import cilik
from cilik.utils.database import set_cmode
from cilik.utils.decorators.admins import AdminActual

### Multi-Lang Commands
CHANNELPLAY_COMMAND = get_command("CHANNELPLAY_COMMAND")


async def get_admins(chat_id):
    return [admins async for admins in cilik.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]

async def get_own(admins):
    for users in admins:
        if users.status == enums.ChatMemberStatus.OWNER:
            creatorid = users.user.id
            return creatorid

@cilik.on_message(
    filters.command(CHANNELPLAY_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminActual
async def playmode_(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(
            _["cplay_1"].format(
                message.chat.title, CHANNELPLAY_COMMAND[0]
            )
        )
    query = message.text.split(None, 2)[1].lower().strip()
    if (str(query)).lower() == "disable":
        await set_cmode(message.chat.id, None)
        return await message.reply_text("Channel Play Disabled")
    else:
        try:
            if "https://t.me/" in query:
                memek = query.replace("https://t.me/", "")
            else:
                memek = int(query)
                
            chat = await cilik.get_chat(memek)
        except Exception as e:
            return await message.reply_text(str(e))
        if chat.type != enums.ChatType.CHANNEL:
            return await message.reply_text(_["cplay_5"])
        try:
            admins = await get_admins(chat.id)
        except:
            return await message.reply_text(_["cplay_4"])
        own = await get_own(admins)
        if own != message.from_user.id:
            return await message.reply_text(
                _["cplay_6"].format(chat.title, own)
            )
        await set_cmode(message.chat.id, chat.id)
        return await message.reply_text(
            _["cplay_3"].format(chat.title, chat.id)
        )
