import requests
import base64
from cilik import cilik
from pyrogram import filters


async def list_messages(messages):
    combined_messages = []

    for mes in messages: 
        combined_message = {
            "entities": [],
            "chatId": mes.chat.id,
            "avatar": True,
            "from": {
                "id": mes.from_user.id,
                "first_name": mes.from_user.first_name,
                "last_name": mes.from_user.last_name,
                "username": mes.from_user.username,
                "language_code": "id",
                "title": "mymusic",
                "photo": {
                    "small_file_id": mes.chat.photo.small_file_id,
                    "small_file_unique_id": mes.chat.photo.small_photo_unique_id,
                    "big_file_id": mes.chat.photo.big_file_id,
                    "big_file_unique_id": mes.chat.photo.big_photo_unique_id
                },
                "type": "private",
                "name": mes.from_user.first_name
            },
            "text": mes.text,
            "replyMessage": {}
        }
        combined_messages.append(combined_message)
    return combined_messages


async def create_quotly(messages, bg_color):
    list = await list_messages(messages)
    json = {
      "type": "quote",
      "format": "png",
      "backgroundColor": bg_color,
      "width": 512,
      "height": 768,
      "scale": 2,
      "messages": list
    }
    return json

async def create_quotly_user(message, user, bg_color):
    r = message.reply_to_message
    json = {
      "type": "quote",
      "format": "png",
      "backgroundColor": bg_color,
      "width": 512,
      "height": 768,
      "scale": 2,
      "messages": [
        {
          "entities": [],
          "chatId": message.chat.id,
          "avatar": True,
          "from": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "language_code": "id",
            "title": "mymusic",
            "photo": {
              "small_file_id": user.photo.small_file_id,
              "small_file_unique_id": user.photo.small_photo_unique_id,
              "big_file_id": user.photo.big_file_id,
              "big_file_unique_id": user.photo.big_photo_unique_id
            },
            "type": "private",
            "name": user.first_name
          },
          "text": r.text,
          "replyMessage": {}
        }
      ]
    }
    return json
      
def getArg(message) -> str:
    arg = message.text.strip().split(None, 1)[1].strip()
    return arg
    
  
def isArgInt(message) -> bool:
    count = getArg(message)
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]
        

@cilik.on_message(filters.command("q"))
async def _(client, message):
    if not message.reply_to_message:
        return await message.reply(
            """
            Reply to message!
            
**Format:**
/q
/q {colour}
/q 1-5
/q @username 
/q @username {colour}
            
**Colour:**
{black, white, green, blue, yellow, brown, red, purple, orange, grey, pink}
""",
        )
    else:     
        warna = {
            "black": "#1b1429", 
            "white": "#ffffff",
            "green": "#00ff00",
            "blue": "#0000ff",
            "yellow": "#ffff00",
            "brown": "#964b00",
            "red": "#ff0000",
            "purple": "#800080",
            "orange": "#ffa500",
            "grey": "#808080",
            "pink": "#FFC0CB"
        }        
        if len(message.command) > 1:
            arg = isArgInt(message)
            color_command = message.text.split()[1]
            if color_command in warna:
                bg_color = warna[color_command]
                reply_message = await client.get_messages(
                    message.chat.id,
                    message.reply_to_message.id,
                    replies=1,
                )
                messages = [reply_message]                
                json = await create_quotly(messages, bg_color)
            elif "@" in color_command:
                user = await client.get_users(color_command.replace("@", ""))
                if len(message.command) > 2:
                    bg_color = warna[message.text.split()[2]]
                else:
                    bg_color = "#1b1429"       
                json = await create_quotly_user(message, user, bg_color)     
            elif arg[0]:
                if arg[1] < 2 or arg[1] > 5:
                    return await message.reply("Argument must be between 2-5.")
                count = arg[1]
                messages = await client.get_messages(
                    message.chat.id,
                    [
                        i
                        for i in range(
                            message.reply_to_message.id,
                            message.reply_to_message.id + count,
                        )
                    ],
                    replies=0,
                )    

                bg_color = "#1b1429"
                json = await create_quotly(messages, bg_color)               
            else:
                return await message.reply("tidak ada warna tersebut")
        else:
            reply_message = await client.get_messages(
                message.chat.id,
                message.reply_to_message.id,
                replies=1,
            )
            messages = [reply_message]            
            bg_color = "#1b1429" 
            json = await create_quotly(messages, bg_color)            
        try:
            response = requests.post('https://bot.lyo.su/quote/generate', json=json).json()
            buffer = base64.b64decode(response['result']['image'].encode('utf-8'))
            open('Quotly.webp', 'wb').write(buffer)
            await message.reply_sticker('Quotly.webp')
        except Exception as e:
            await message.reply(str(e))
