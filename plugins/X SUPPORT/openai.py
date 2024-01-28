from pyrogram import Client, filters
from info import OPENAI_API, LOG_CHANNEL, AI
import openai
import asyncio

openai.api_key = OPENAI_API

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096  # Maximum length of a message
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i+max_length])


@Client.on_message(filters.command("openai"))
async def ask_question(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            try:
                s = await message.reply_sticker("CAACAgQAAxkBAAELHDhlmn1cxY6clm6BgZoURPY-xywq4gACbg8AAuHqsVDaMQeY6CcRojQE")
                text = message.text.split(" ", 1)[1]
                user_id = message.from_user.id
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": text}
                    ],
                    max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
                    temperature=0.6
                )          
                ai_response = response.choices[0].message.content.strip()
                await s.delete()
                await send_message_in_chunks(client, message.chat.id, f"HEY {message.from_user.mention}\n\nQuestion: {text}\n\nRᥱ́ρoᥒ⳽ᥱ👇\n\n{response.choices[0].message.content}\n\n📌 Remɑɾque : En tɑnt que IA, Je peux commettɾe des eɾɾeuɾs. Pensez ɑ̀ véɾifieɾ les infoɾmɑtions impoɾtɑntes.")
                await send_message_in_chunks(client, LOG_CHANNEL, f"#ask {message.from_user.mention} **Avec ID utilisɑteuɾ -** {user_id}.\n🔍 **M'ɑ posé cette question...**👇\n\n🔻 **Question:** `{text}`\n\n🔻 **Voici lɑ ɾéponse que j’ɑi donnée:**\n🖍️ {ai_response}\n\n\n🔻 **Identifiɑnt :-** {user_id} \n🔻 **Nom d’utilisɑteuɾ :-** {message.from_user.mention}")
                
            except Exception as error:
                print(error)
                await message.reply_text(f"**Une eɾɾeuɾ s’est pɾoduite:**\n\n**{error}**\n\n")
    else:
        return
