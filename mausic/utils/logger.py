from config import LOG, LOG_GROUP_ID
from mausic import mausic
from mausic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
📮 **MAUSIC PLAY LOG**

💬 **Chat:** {message.chat.title} [`{message.chat.id}`]
👨🏻‍🚀 **User:** {message.from_user.mention}
🔖 **Username:** @{message.from_user.username}
🆔 **User ID:** `{message.from_user.id}`
🔗 **Chat Link:** {chatusername}
🏷 **Query:** {message.text}
💽 **StreamType:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await mausic.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
