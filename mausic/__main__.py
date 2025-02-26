import asyncio
import importlib
import sys
from atexit import register
from os import execl
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS

from mausic import LOGGER, mausic, ub
from mausic.core.call import Yukki
from mausic.plugins import ALL_MODULES
from mausic.utils.database import get_banned_users, get_gbanned



loop = asyncio.get_event_loop()


async def auto_restart():
    while not await asyncio.sleep(43200):

        def _():
            execl(sys.executable, sys.executable, "-m", "mausic")

        register(_)
        sys.exit(0)


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
        and not config.STRING6
        and not config.STRING7
        and not config.STRING8
        and not config.STRING9
        and not config.STRING10
    ):
        LOGGER("mausic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("mausic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await mausic.start()
    for all_module in ALL_MODULES:
        importlib.import_module("mausic.plugins" + all_module)
    LOGGER("mausic.plugins").info("Successfully Imported Modules ")
    await ub.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("mausic").error(
            "[ERROR] - \n\nHarap aktifkan Obrolan Suara di Grup Logger Anda. Pastikan Anda tidak pernah menutup/mengakhiri panggilan Obrolan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    asyncio.create_task(auto_restart())
    LOGGER("mausic").info("mausic Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("mausic").info("Stopping mausic Music Bot! GoodBye")
