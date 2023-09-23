from ast import main
import asyncio
import time
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler

api_id = 21788005
api_hash = "beae7dc11037ecdf5b3ecdb586064486"

app = Client("baranki")
atackers = []
@app.on_message()
async def attack(client, message):

        global atackers

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
        except: pass
        if '🫀 Русак лежить весь в крові.' in message.text:
                await message.reply("@AnastasiyaKJ хіл")
app.run()

if __name__ == "__main__":
	asyncio.run(main())
               