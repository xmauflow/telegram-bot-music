import random

from cilik import ub
from cilik.core.mongo import mongodb

db = mongodb.assistants

assistantdict = {}


async def get_client(assistant: int):
    if int(assistant) == 1:
        return ub.one
    elif int(assistant) == 2:
        return ub.two
    elif int(assistant) == 3:
        return ub.three
    elif int(assistant) == 4:
        return ub.four
    elif int(assistant) == 5:
        return ub.five
    elif int(assistant) == 6:
        return ub.six
    elif int(assistant) == 7:
        return ub.seven
    elif int(assistant) == 8:
        return ub.eight
    elif int(assistant) == 9:
        return ub.nine
    elif int(assistant) == 10:
        return ub.ten



async def set_assistant(chat_id):
    from cilik.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    ub = await get_client(ran_assistant)
    return ub


async def get_assistant(chat_id: int) -> str:
    from cilik.core.userbot import assistants

    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await db.find_one({"chat_id": chat_id})
        if not dbassistant:
            ub = await set_assistant(chat_id)
            return ub
        else:
            got_assis = dbassistant["assistant"]
            if got_assis in assistants:
                assistantdict[chat_id] = got_assis
                ub = await get_client(got_assis)
                return ub
            else:
                ub = await set_assistant(chat_id)
                return ub
    else:
        if assistant in assistants:
            ub = await get_client(assistant)
            return ub
        else:
            ub = await set_assistant(chat_id)
            return ub


async def set_calls_assistant(chat_id):
    from cilik.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await db.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    return ran_assistant


async def group_assistant(self, chat_id: int) -> int:
    from cilik.core.userbot import assistants

    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await db.find_one({"chat_id": chat_id})
        if not dbassistant:
            assis = await set_calls_assistant(chat_id)
        else:
            assis = dbassistant["assistant"]
            if assis in assistants:
                assistantdict[chat_id] = assis
                assis = assis
            else:
                assis = await set_calls_assistant(chat_id)
    else:
        if assistant in assistants:
            assis = assistant
        else:
            assis = await set_calls_assistant(chat_id)
    if int(assis) == 1:
        return self.one
    elif int(assis) == 2:
        return self.two
    elif int(assis) == 3:
        return self.three
    elif int(assis) == 4:
        return self.four
    elif int(assis) == 5:
        return self.five
    elif int(assis) == 6:
        return self.six
    elif int(assis) == 7:
        return self.seven
    elif int(assis) == 8:
        return self.eight
    elif int(assis) == 9:
        return self.nine
    elif int(assis) == 10:
        return self.ten    
