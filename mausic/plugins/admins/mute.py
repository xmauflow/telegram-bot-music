
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from mausic import mausic
from mausic.core.call import Yukki
from mausic.utils.database import is_muted, mute_on
from mausic.utils.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@mausic.on_message(
    filters.command(MUTE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await Yukki.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
