import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message

from config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from strings import get_command
from mausic import mausic
from mausic.core.call import Yukki
from mausic.misc import db
from mausic.utils.database import get_authuser_names, get_cmode
from mausic.utils.decorators import (ActualAdminCB, AdminActual,
                                      language)
from mausic.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@mausic.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = []
        async for admin in mausic.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            admins.append(admin)
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.privileges.can_manage_video_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "Failed to reload admincache. Make sure Bot is admin in your chat."
        )


@mausic.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"Please Wait.. Restarting {MUSIC_BOT_NAME} for your chat.."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Yukki.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await mausic.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Yukki.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        "Successfully restarted. Try playing now.."
    )


@mausic.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@mausic.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@mausic.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "Downloading already Completed.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "Downloading already Completed or Cancelled.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "Downloading Cancelled", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"Download Cancelled by {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "Failed to stop the Downloading.", show_alert=True
            )
    await CallbackQuery.answer(
        "Failed to recognize the running task", show_alert=True
    )
