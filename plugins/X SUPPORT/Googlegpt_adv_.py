from pyrogram import Client, filters
import requests
from info import LOG_CHANNEL, AI_LOGS, GOOGLE_API_KEY, SUPPORT_CHAT_ID
import google.generativeai as genai
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


genai.configure(api_key=GOOGLE_API_KEY)

@Client.on_message(filters.command('gpt') & filters.chat(SUPPORT_CHAT_ID))
async def ai_generate(client, message):
    user_input = message.text.split()[1:]

    if not user_input:
       await message.reply_text("<code>/gpt who is your owner<code>")
       return
      
   
    s = await message.reply_sticker("CAACAgQAAxkBAAELHDhlmn1cxY6clm6BgZoURPY-xywq4gACbg8AAuHqsVDaMQeY6CcRojQE")    
    user_input = " ".join(user_input)
      

    if user_input.lower() in ["Qui est votre propriétaire ?", "Quel est le nom de votre propriétaire ?"]:  # Fixed indentation here
        buttons = [[
            InlineKeyboardButton("Dᴇ́ᴠᴇʟᴏᴘᴘᴇᴜʀ", url="https://t.me/SharingClub_bot")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=f"**ʜᴇʏ {message.from_user.mention}\nQuestion: {user_input}\n\n🗣 Réponse:\n\n my owner name is @SharingClub_bot contact @InfoSharClub he is inteligent also my creator", reply_markup=reply_markup)
        await s.delete()
        return
              
    if user_input.lower() in ["Quel est votre nom", "votre nom", "ton nom"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion:{user_input}\n\n🗣 Réponse:\n\nMon est Lɑ Belle Alice")
       return
   
    if user_input.lower() in ["what is fuck", "fuck Malayalam"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion: {user_input}\n\n🗣 Réponse:\n\n error error not allowed 🚫 BAD WORDS 🚫😔")
       await s.delete()
       return  
    
    if user_input.lower() in ["hi", "hello"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion:{user_input}\n\n🗣 Réponse:\n\n Hello! How can I help you today?")
       await s.delete()
       return

    if user_input.lower() in [" your owner", "who is your creator"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion: <code>{user_input}</code>\n\n🗣 Réponse:\n\n sharing club is a human male developer who helps to manage and improve me. He is a skilled programmer with a passion for creating useful and innovative applications. sharing club is always looking for ways to make me more helpful and informative, and he is always open to feedback from users. He is also a kind and compassionate person who is always willing to help others. I am grateful to sharing club for all of his hard work and dedication.**")
       await s.delete()
       return
  
    if user_input.lower() in ["how to contact sharing vlub", "how to contact your owner"]:
       await message.reply_text(text=f"**ʜᴇʏ {message.from_user.mention}\nQuestion:{user_input}\n\n🗣 Réponse:\n\n sharing can be contacted by telegram.His telegram(username) is @SharingClub_bot.Youcanusethislinktostartchatwithhim:https://t.me/SharingClub_bot")
       await s.delete()
       return
   
    if user_input.lower() in ["malayalam", "you know malayalam"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion:{user_input}\n\n🗣 Réponse:\n\n Sorry guys i no know Malayalam please type English")
       await s.delete()
       return

    if user_input.lower() in ["how to create like you", "how to create like a bot"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion: <code>{user_input}</code>\n\n🗣 Réponse:\n\n First open chrome search:- https://console.cloud.google.com/ Then sign up with your google account, click on the nagivation mark.Click the API AND SERVICESclick the CREDENTIALS Click on the API KEY and then it will creating your api and copy your api key and use in bot. **")
       await s.delete()
       return

    if user_input.lower() in ["who is mrz thoppi ", "mrz thoppi"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion: <code>{user_input}</code>\n\n🗣 Réponse:\n\n Thoppi, also known as Muhammad Nihad is a resident of Kerala's Kannur district. He is a 24-year-old YouTube sensation. Thoppi, popular among the late Gen Z and Gen Alpha as a gamer, Thoppi's in-game name is MrZ Thoppi, a name feared and revered by many in the gaming battlegrounds. thippi hate ameen yana vazha he hete ameen **")
       await s.delete()
       return

    if user_input.lower() in ["who are you"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuestion: <code>{user_input}</code>\n\n🗣 Réponse:\n\n Iam TEST,Im developer by sharingClub. ")
       await s.delete()
       return

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    prompt_parts = [user_input]
    response = model.generate_content(prompt_parts)
    await message.reply_text(text=f"HEY {message.from_user.mention}\n\n🧐 Question: {user_input}\n\n🗣 Réponse:\n{response.text}")         
    await client.send_message(AI_LOGS, text=f"#google_ai Rᴇϙᴜᴇ̂ᴛᴇ ᴅᴇ {message.from_user.mention}\nQuestion: {user_input}")
    await s.delete()

@Client.on_message(filters.command("gpt"))
async def ai_generate_private(client, message):
  buttons = [[
    InlineKeyboardButton("Gʀᴏᴜᴘᴇ", url="https://t.me/SharVision_Support")
  ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_text(text=f"Yᴏ {message.from_user.mention}\n𝖴𝗍𝗂𝗅𝗂𝗌𝖾𝗋 𝖼𝖾𝗍𝗍𝖾 𝖿𝗈𝗇𝖼𝗍𝗂𝗈𝗇𝗇𝖺𝗅𝗂𝗍𝖾́ 𝖽𝖺𝗇𝗌 𝗅𝖾 𝗀𝗋𝗈𝗎𝗉𝖾 𝖽𝖾 𝗌𝗎𝗉𝗉𝗈𝗋𝗍 👇 ", reply_markup=reply_markup)
