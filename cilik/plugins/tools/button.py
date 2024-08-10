from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                            Message)
from cilik import cilik
from cilik.misc import SUDOERS

@cilik.on_message(filters.command(["button", "btn"], [".", "^", "-", "!", "/"]) & SUDOERS)
async def buttoncilik(_, message: Message):
    if not message.reply_to_message:
        await message.reply_text("**Usage:**\n/button {text} {link} reply to message") 
    elif message.reply_to_message:
        msg = message.reply_to_message
        cilik = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
        a = cilik[1:]
        text = str(cilik[0])
        link = str(userbot[0])
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{text}", url=f"t.me/{link}")]])
        await msg.copy(message.chat.id, reply_markup=reply_markup)
