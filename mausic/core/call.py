import asyncio
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.errors import (ChatAdminRequired,
                             ChannelInvalid,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls
from ntgcalls import TelegramServerError
from pytgcalls.exceptions import (AlreadyJoinedError,
                                  NoActiveGroupCall)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update, AudioPiped, AudioVideoPiped, StreamAudioEnded)

import config
from strings import get_string
from mausic import LOGGER, YouTube, mausic
from mausic.misc import db
from mausic.utils.database import (add_active_chat,
                                       add_active_video_chat,
                                       get_assistant,
                                       get_audio_bitrate, get_lang,
                                       get_loop, get_video_bitrate,
                                       group_assistant, is_autoend,
                                       music_on, mute_off,
                                       remove_active_chat,
                                       remove_active_video_chat,
                                       set_loop)
from mausic.utils.exceptions import AssistantErr
from mausic.utils.inline.play import (stream_markup,
                                          telegram_markup)
from mausic.utils.stream.autoclear import auto_clean
from mausic.utils.thumbnails import gen_thumb

autoend = {}
counter = {}
AUTO_END_TIME = 3


async def _clear_(chat_id):
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)


class Call(PyTgCalls):
    def __init__(self):
        self.userbot1 = Client(
            name="Ubot1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.one = PyTgCalls(
            self.userbot1,
            cache_duration=100,
        )
        self.userbot2 = Client(
            name="Ubot2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.two = PyTgCalls(
            self.userbot2,
            cache_duration=100,
        )
        self.userbot3 = Client(
            name="Ubot3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.three = PyTgCalls(
            self.userbot3,
            cache_duration=100,
        )
        self.userbot4 = Client(
            name="Ubot4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.four = PyTgCalls(
            self.userbot4,
            cache_duration=100,
        )
        self.userbot5 = Client(
            name="Ubot5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.five = PyTgCalls(
            self.userbot5,
            cache_duration=100,
        )
        self.userbot6 = Client(
            name="Ubot6",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING6),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.six = PyTgCalls(
            self.userbot6,
            cache_duration=100,
        )
        self.userbot7 = Client(
            name="Ubot7",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING7),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.seven = PyTgCalls(
            self.userbot7,
            cache_duration=100,
        )
        self.userbot8 = Client(
            name="Ubot8",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING8),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.eight = PyTgCalls(
            self.userbot8,
            cache_duration=100,
        )
        self.userbot9 = Client(
            name="Ubot9",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING9),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.nine = PyTgCalls(
            self.userbot9,
            cache_duration=100,
        )
        self.userbot10 = Client(
            name="Ubot10",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING10),
            app_version="9.6.5",
            device_model="Macbook Pro 13 M1",
            system_version="macOS Ventura 13.0.1",
        )
        self.ten = PyTgCalls(
            self.userbot10,
            cache_duration=100,
        )      

        
    async def pause_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.pause_stream(chat_id)

    async def resume_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.resume_stream(chat_id)

    async def mute_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.mute_stream(chat_id)

    async def unmute_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.unmute_stream(chat_id)

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            await _clear_(chat_id)
            await assistant.leave_group_call(chat_id)
        except:
            pass

    async def force_stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            check = db.get(chat_id)
            check.pop(0)
        except:
            pass
        await remove_active_video_chat(chat_id)
        await remove_active_chat(chat_id)
        try:
            await assistant.leave_group_call(chat_id)
        except:
            pass

    async def skip_stream(
        self, chat_id: int, link: str, video: Union[bool, str] = None
    ):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        stream = (
            AudioVideoPiped(
                link,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
            )
            if video
            else AudioPiped(
                link, audio_parameters=audio_stream_quality
            )
        )
        await assistant.change_stream(
            chat_id,
            stream,
        )

    async def seek_stream(
        self, chat_id, file_path, to_seek, duration, mode
    ):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        stream = (
            AudioVideoPiped(
                file_path,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
                additional_ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
            )
            if mode == "video"
            else AudioPiped(
                file_path,
                audio_parameters=audio_stream_quality,
                additional_ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
            )
        )
        await assistant.change_stream(chat_id, stream)

    async def stream_call(self, link):
        assistant = await group_assistant(self, config.LOG_GROUP_ID)
        await assistant.join_group_call(
            config.LOG_GROUP_ID,
            AudioVideoPiped(link),
        )
        await asyncio.sleep(0.5)
        await assistant.leave_group_call(config.LOG_GROUP_ID)

    async def join_assistant(self, original_chat_id, chat_id):
        language = await get_lang(original_chat_id)
        _ = get_string(language)
        userbot = await get_assistant(chat_id)
        try:
            try:
                get = await mausic.get_chat_member(chat_id, userbot.id)
            except ChatAdminRequired:
                raise AssistantErr(_["call_1"])
            if get.status == "banned" or get.status == "kicked":
                raise AssistantErr(
                    _["call_2"].format(userbot.username, userbot.id)
                )
        except UserNotParticipant:
            chat = await mausic.get_chat(chat_id)
            if chat.username:
                try:
                    await userbot.join_chat(chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    raise AssistantErr(_["call_3"].format(e))
            else:
                try:
                    try:
                        try:
                            invitelink = chat.invite_link
                            if invitelink is None:
                                invitelink = (
                                    await mausic.export_chat_invite_link(
                                        int(chat_id)
                                    )
                                )
                        except:
                            invitelink = (
                                await mausic.export_chat_invite_link(
                                    int(chat_id)
                                )
                            )
                    except ChatAdminRequired:
                        raise AssistantErr(_["call_4"])
                    except Exception as e:
                        raise AssistantErr(e)
                    m = await mausic.send_message(
                        original_chat_id, _["call_5"]
                    )
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", "https://t.me/joinchat/"
                        )
                    await asyncio.sleep(3)
                    await userbot.join_chat(invitelink)
                    await asyncio.sleep(4)
                    await m.edit(_["call_6"].format(userbot.name))
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    raise AssistantErr(_["call_3"].format(e))

    async def join_call(
        self,
        chat_id: int,
        original_chat_id: int,
        link,
        video: Union[bool, str] = None,
    ):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        stream = (
            AudioVideoPiped(
                link,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
            )
            if video
            else AudioPiped(
                link, audio_parameters=audio_stream_quality
            )
        )
        try:
            await assistant.join_group_call(
                chat_id,
                stream,
            )
        except (ChannelInvalid, NoActiveGroupCall):
            try:
                await self.join_assistant(original_chat_id, chat_id)
            except Exception as e:
                raise e
            try:
                await assistant.join_group_call(
                    chat_id,
                    stream,
                )
            except Exception as e:
                raise AssistantErr(
                    "**Obrolan Suara Aktif Tidak Ditemukan**\n\nPastikan obrolan suara grup diaktifkan. Jika sudah diaktifkan, harap akhiri dan mulai obrolan suara baru lagi dan jika masalah berlanjut, coba /restart"
                )
        except AlreadyJoinedError:
            raise AssistantErr(
                "**Asisten Sudah di Obrolan Suara**\n\nSistem telah mendeteksi bahwa asisten sudah ada di obrolan suara, masalah ini biasanya muncul saat Anda memainkan 2 kueri secara bersamaan.\n\nJika asisten tidak ada di obrolan suara, harap akhiri obrolan suara dan mulai obrolan suara baru lagi dan jika masalah berlanjut, coba /restart"
            )
        except TelegramServerError:
            raise AssistantErr(
                "**Telegram Server Error**\n\nTelegram mengalami beberapa masalah server internal, Silakan coba putar lagi.\n\n Jika masalah ini terus muncul setiap saat, harap akhiri obrolan suara Anda dan mulai obrolan suara baru lagi."
            )
        await add_active_chat(chat_id)
        await mute_off(chat_id)
        await music_on(chat_id)
        if video:
            await add_active_video_chat(chat_id)
        if await is_autoend():
            counter[chat_id] = {}
            users = len(await assistant.get_participants(chat_id))
            if users == 1:
                autoend[chat_id] = datetime.now() + timedelta(
                    minutes=AUTO_END_TIME
                )

    async def change_stream(self, client, chat_id):
        check = db.get(chat_id)
        popped = None
        loop = await get_loop(chat_id)
        try:
            if loop == 0:
                popped = check.pop(0)
            else:
                loop = loop - 1
                await set_loop(chat_id, loop)
            if popped:
                if config.AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await _clear_(chat_id)
                return await client.leave_group_call(chat_id)
        except:
            try:
                await _clear_(chat_id)
                return await client.leave_group_call(chat_id)
            except:
                return
        else:
            queued = check[0]["file"]
            language = await get_lang(chat_id)
            _ = get_string(language)
            title = (check[0]["title"]).title()
            user = check[0]["by"]
            original_chat_id = check[0]["chat_id"]
            streamtype = check[0]["streamtype"]
            audio_stream_quality = await get_audio_bitrate(chat_id)
            video_stream_quality = await get_video_bitrate(chat_id)
            videoid = check[0]["vidid"]
            check[0]["played"] = 0
            if "live_" in queued:
                n, link = await YouTube.video(videoid, True)
                if n == 0:
                    return await mausic.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                stream = (
                    AudioVideoPiped(
                        link,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                    if str(streamtype) == "video"
                    else AudioPiped(
                        link, audio_parameters=audio_stream_quality
                    )
                )
                try:
                    await client.change_stream(chat_id, stream)
                except Exception:
                    return await mausic.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                img = await gen_thumb(videoid)
                button = telegram_markup(_, chat_id)
                run = await mausic.send_photo(
                    original_chat_id,
                    photo=img,
                    caption=_["stream_1"].format(
                        user,
                        f"https://t.me/{mausic.username}?start=info_{videoid}",
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            elif "vid_" in queued:
                mystic = await mausic.send_message(
                    original_chat_id, _["call_10"]
                )
                try:
                    file_path, direct = await YouTube.download(
                        videoid,
                        mystic,
                        videoid=True,
                        video=True
                        if str(streamtype) == "video"
                        else False,
                    )
                except:
                    return await mystic.edit_text(
                        _["call_9"], disable_web_page_preview=True
                    )
                stream = (
                    AudioVideoPiped(
                        file_path,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                    if str(streamtype) == "video"
                    else AudioPiped(
                        file_path,
                        audio_parameters=audio_stream_quality,
                    )
                )
                try:
                    await client.change_stream(chat_id, stream)
                except Exception:
                    return await mausic.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                img = await gen_thumb(videoid)
                button = stream_markup(_, videoid, chat_id)
                await mystic.delete()
                run = await mausic.send_photo(
                    original_chat_id,
                    photo=img,
                    caption=_["stream_1"].format(
                        user,
                        f"https://t.me/{mausic.username}?start=info_{videoid}",
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            elif "index_" in queued:
                stream = (
                    AudioVideoPiped(
                        videoid,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                    if str(streamtype) == "video"
                    else AudioPiped(
                        videoid, audio_parameters=audio_stream_quality
                    )
                )
                try:
                    await client.change_stream(chat_id, stream)
                except Exception:
                    return await mausic.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                button = telegram_markup(_, chat_id)
                run = await mausic.send_photo(
                    original_chat_id,
                    photo=config.STREAM_IMG_URL,
                    caption=_["stream_2"].format(user),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            else:
                stream = (
                    AudioVideoPiped(
                        queued,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                    if str(streamtype) == "video"
                    else AudioPiped(
                        queued, audio_parameters=audio_stream_quality
                    )
                )
                try:
                    await client.change_stream(chat_id, stream)
                except Exception:
                    return await mausic.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                if videoid == "telegram":
                    button = telegram_markup(_, chat_id)
                    run = await mausic.send_photo(
                        original_chat_id,
                        photo=config.TELEGRAM_AUDIO_URL
                        if str(streamtype) == "audio"
                        else config.TELEGRAM_VIDEO_URL,
                        caption=_["stream_3"].format(
                            title, check[0]["dur"], user
                        ),
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                    db[chat_id][0]["mystic"] = run
                    db[chat_id][0]["markup"] = "tg"
                elif videoid == "soundcloud":
                    button = telegram_markup(_, chat_id)
                    run = await mausic.send_photo(
                        original_chat_id,
                        photo=config.SOUNCLOUD_IMG_URL,
                        caption=_["stream_3"].format(
                            title, check[0]["dur"], user
                        ),
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                    db[chat_id][0]["mystic"] = run
                    db[chat_id][0]["markup"] = "tg"
                else:
                    img = await gen_thumb(videoid)
                    button = stream_markup(_, videoid, chat_id)
                    run = await mausic.send_photo(
                        original_chat_id,
                        photo=img,
                        caption=_["stream_1"].format(
                            user,
                            f"https://t.me/{mausic.username}?start=info_{videoid}",
                        ),
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                    db[chat_id][0]["mystic"] = run
                    db[chat_id][0]["markup"] = "stream"

    async def ping(self):
        pings = []
        if config.STRING1:
            pings.append(await self.one.ping)
        if config.STRING2:
            pings.append(await self.two.ping)
        if config.STRING3:
            pings.append(await self.three.ping)
        if config.STRING4:
            pings.append(await self.four.ping)
        if config.STRING5:
            pings.append(await self.five.ping)
        if config.STRING6:
            pings.append(await self.six.ping)
        if config.STRING7:
            pings.append(await self.seven.ping)
        if config.STRING8:
            pings.append(await self.eight.ping)
        if config.STRING9:
            pings.append(await self.nine.ping)
        if config.STRING10:
            pings.append(await self.ten.ping)            
        return str(round(sum(pings) / len(pings), 3))

    async def start(self):
        LOGGER(__name__).info("Starting PyTgCalls Client\n")
        if config.STRING1:
            await self.one.start()
        if config.STRING2:
            await self.two.start()
        if config.STRING3:
            await self.three.start()
        if config.STRING4:
            await self.four.start()
        if config.STRING5:
            await self.five.start()
        if config.STRING6:
            await self.six.start()
        if config.STRING7:
            await self.seven.start()
        if config.STRING8:
            await self.eight.start()
        if config.STRING9:
            await self.nine.start()
        if config.STRING10:
            await self.ten.start()
            
    async def decorators(self):
        @self.one.on_kicked()
        @self.two.on_kicked()
        @self.three.on_kicked()
        @self.four.on_kicked()
        @self.five.on_kicked()
        @self.six.on_kicked()
        @self.seven.on_kicked()
        @self.eight.on_kicked()
        @self.nine.on_kicked()
        @self.ten.on_kicked()        
        @self.one.on_closed_voice_chat()
        @self.two.on_closed_voice_chat()
        @self.three.on_closed_voice_chat()
        @self.four.on_closed_voice_chat()
        @self.five.on_closed_voice_chat()
        @self.six.on_closed_voice_chat()
        @self.seven.on_closed_voice_chat()
        @self.eight.on_closed_voice_chat()
        @self.nine.on_closed_voice_chat()
        @self.ten.on_closed_voice_chat()        
        @self.one.on_left()
        @self.two.on_left()
        @self.three.on_left()
        @self.four.on_left()
        @self.five.on_left()
        @self.six.on_left()
        @self.seven.on_left()
        @self.eight.on_left()
        @self.nine.on_left()
        @self.ten.on_left()        
        async def stream_services_handler(_, chat_id: int):
            await self.stop_stream(chat_id)

        @self.one.on_stream_end()
        @self.two.on_stream_end()
        @self.three.on_stream_end()
        @self.four.on_stream_end()
        @self.five.on_stream_end()
        @self.six.on_stream_end()
        @self.seven.on_stream_end()
        @self.eight.on_stream_end()
        @self.nine.on_stream_end()
        @self.ten.on_stream_end()        
        async def stream_end_handler1(client, update: Update):
            if not isinstance(update, StreamAudioEnded):
                return
            await self.change_stream(client, update.chat_id)

        @self.one.on_participants_change()
        @self.two.on_participants_change()
        @self.three.on_participants_change()
        @self.four.on_participants_change()
        @self.five.on_participants_change()
        @self.six.on_participants_change()
        @self.seven.on_participants_change()
        @self.eight.on_participants_change()
        @self.nine.on_participants_change()
        @self.ten.on_participants_change()        
        async def participants_change_handler(client, update: Update):
            if not isinstance(
                update, JoinedGroupCallParticipant
            ) and not isinstance(update, LeftGroupCallParticipant):
                return
            chat_id = update.chat_id
            users = counter.get(chat_id)
            if not users:
                try:
                    got = len(await client.get_participants(chat_id))
                except:
                    return
                counter[chat_id] = got
                if got == 1:
                    autoend[chat_id] = datetime.now() + timedelta(
                        minutes=AUTO_END_TIME
                    )
                    return
                autoend[chat_id] = {}
            else:
                final = (
                    users + 1
                    if isinstance(update, JoinedGroupCallParticipant)
                    else users - 1
                )
                counter[chat_id] = final
                if final == 1:
                    autoend[chat_id] = datetime.now() + timedelta(
                        minutes=AUTO_END_TIME
                    )
                    return
                autoend[chat_id] = {}


Yukki = Call()
