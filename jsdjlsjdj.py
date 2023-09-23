from ast import main
import asyncio
import time
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler

app = Client("baranki")
atackers = []
@app.on_message()
async def attack(client, message):  
        #if message.from_user.id == 707686507 and message.chat.id == -1001753741231:
            #await app.delete_messages(message.chat.id, message.id)
        #if message.text == 'hill': 
        #    await message.reply('/rusak')
        
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
                                await app.send_message("@Random_UAbot", "/shop")
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
        if 1==1:     
            if 'Рейди можна проводити один раз в годину.' in message.text and message.from_user.id == 1466731329:
                print('f')
                text = message.text.replace('Рейди можна проводити один раз в годину.', '')
                text = text.replace('\n', '')
                text = text.replace('Залишилось ', '')
                text = text.replace('хв.', '')
                timme = int(text)
                timme = timme - 3
                if timme < 0:
                    timme = 60-(3-(timme+-timme)*-1)
                a = time.ctime()
                a = a.split(' ')
                a = a[3]
                    
                b = a[0] + a[1]
                b = int(b)
                c = a[6] + a[7]
                c = int(c)
                a = a[3] + a[4]
                a = int(a)
                
                timhe = b
                
                timme = timme + a
        
                if timme > 59:
                        timme = timme-60
                        timhe = timhe+1
                print(str(timhe) + ':' + str(timme))
        
        try:
        #    if 'Проведено рейд на ' in message.text and message.from_user.id == 1466731329:
        #        time.sleep(0.3)
        #        await app.send_message(-1001753741231, "/raid") 
            if 'Міжчатова битва русаків завершена!' in message.text:
                time.sleep(0.3)
                await app.send_message(message.chat.id, "/war") 
                await app.send_message(message.chat.id, "тегніть мене кого додати в список для тегів")
            if '/hill' in message.text:
                await app.send_message(-783660629, "/rusak")
            if message.chat.id == -783660629:
                await app.send_message("@Random_UA3bot", "/shop")
                await client.request_callback_answer(
                chat_id=message.chat.id,
                message_id=message.id,
                callback_data = "aid_kit"
                )
            if 'tagraid1' in message.text:
                time.sleep(0.3)
                await app.send_message(message.chat.id, "тегніть і додам щоб вас тегало") 
          
        except: pass
        try:
            a = time.ctime()
            a = a.split(' ')
            #print(a)
            a = a[3]
                 
            b = a[0] + a[1]
            b = int(b)
            c = a[6] + a[7]
            c = int(c)
            a = a[3] + a[4]
            a = int(a)
            if a >= timme and b >= timhe:
                await app.send_message(-625349388, " @Bogdanboss220 через 3хв рейд, приготуйтесь")
                await app.send_message(-625349388, "через 3хв рейд, приготуйтесь")
                    
            timr = timme + 4
            timhr = timhe
                
            if timr > 59:
                timr = timr - 60
                timhr = timhr + 1
            print(str(timhr) + ':' + str(timr))
            if a >= timr and b >= timhr:
                await app.send_message(-625349388, "/raid")
                timme = 99
                timhe = 99
        except: pass
        if 'лікар' in message.text:
                        await message.reply("/swap")
        if 'Лікар' in message.text:
                        await message.reply("/swap")
        if 'Хакер' in message.text:
                        await message.reply("/swap")
        if 'хакер' in message.text:
                        await message.reply("/swap")


app.run()

if __name__ == "__main__":
	asyncio.run(main())