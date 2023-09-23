from ast import main
import asyncio
import time
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler
from telethon.sync import TelegramClient, events

app = Client("my_account")
atackers = []
@app.on_message()
async def attack(client, message):  
        if message.from_user.id == 707686507 and message.chat.id == -1001753741231:
            await app.delete_messages(message.chat.id, message.id)
        #if message.text == 'hill': 
            #await message.reply('/rusak')
        
        global atackers
        #try:
        #if message.from_user.id == 707686507 and message.chat.id == -1001753741231:
        #    await app.send_reaction(-1001753741231, message.id, "🤡")
        #except: pass
       
        if message.text == 'start' and message.from_user.id != 987864213:
                if message.from_user.id not in atackers:
                        atackers.append(int(message.from_user.id))
                        await message.reply("ok")
        elif message.text == 'stop':
                if message.from_user.id in atackers:
                        atackers.remove(int(message.from_user.id))
                        await message.reply("ok")
        try:
                if message.from_user.id in atackers and 'починає битву русаків!' in message.text:
                        #try:
                        if message.id % 40 == 0:
                                await app.send_message("@RandomUA3bot", "/shop")
                        try:
                                await client.request_callback_answer(
                                chat_id = message.chat.id,
                                message_id = message.id,
                                        callback_data = "fight"+str(message.from_user.id)
                                )
                        except: pass               
	
                elif message.chat.id == 1466731329:
                        await client.request_callback_answer(
                        chat_id=message.chat.id,
                        message_id=message.id,
                        callback_data = "aid_kit"
                        )
        except: pass
        if '🫀 Русак лежить весь в крові.' in message.text:
                        await message.reply("@AnastasiyaKJ хіл")
        if 'лікар' in message.text:
                        await message.reply("/swap")
        if 'Лікар' in message.text:
                        await message.reply("/swap")
        if 'Хакер' in message.text:
                        await message.reply("/swap")
        if 'хакер' in message.text:
                        await message.reply("/swap")


        try:

                if '/hill' in message.text:
                        await app.send_message(-783660629, "/rusak")
                if message.chat.id == -783660629:
                        await app.send_message("@RandomUA3bot", "/shop")
                        await client.request_callback_answer(
                        chat_id=message.chat.id,
                        message_id=message.id,
                        callback_data = "aid_kit"
                        )

                if message.text == 'hill':
                        await app.send_message("@RandomUA3bot", "/shop")
                if message.text == 'Ось опис товарів, які можна придбати:':
                        await client.request_callback_answer(
                        chat_id = message.chat.id,
                        message_id = message.id,
                        callback_data = "aid_kit"
                
                )
              
        except: pass
        

app.run()

if __name__ == "__main__":
	asyncio.run(main())