from pyrogram import Client, filters
import requests
from info import LOG_CHANNEL, GOOGLE_API_KEY, SUPPORT_CHAT_ID
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
      

    if user_input.lower() in ["who is your owner", "what is your owner name"]:  # Fixed indentation here
        buttons = [[
            InlineKeyboardButton("developer", url="https://t.me/SharingClub_bot")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(text=f"**ʜᴇʏ {message.from_user.mention}\nQuery: {user_input}\n\nResults:\n\n my owner name is @SharingClub_bot contact @InfoSharClub he is inteligent also my creator", reply_markup=reply_markup)
        await s.delete()
        return
              
    if user_input.lower() in ["what is your name", "your name"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery:{user_input}\n\nResults:\n\nMY NAME IS TEST BOT")
       return
   
    if user_input.lower() in ["what is fuck", "fuck Malayalam"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery: {user_input}\n\nResults:\n\n error error not allowed 🚫 BAD WORDS 🚫😔")
       await s.delete()
       return  
    
    if user_input.lower() in ["hi", "hello"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery:{user_input}\n\nResults:\n\n Hello! How can I help you today?")
       await s.delete()
       return

    if user_input.lower() in ["how to contact your owner", "who is your creator"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery: <code>{user_input}</code>\n\nResults:\n\n Mr Tech is a human male developer who helps to manage and improve me. He is a skilled programmer with a passion for creating useful and innovative applications. Mrtech is always looking for ways to make me more helpful and informative, and he is always open to feedback from users. He is also a kind and compassionate person who is always willing to help others. I am grateful to Bisal for all of his hard work and dedication.**")
       await s.delete()
       return
  
    if user_input.lower() in ["how to contact mr tech", "how to contact my owner"]:
       await message.reply_text(text=f"**ʜᴇʏ {message.from_user.mention}\nQuery:{user_input}\n\nResults:\n\n sharing can be contacted by telegram.His telegram(username) is @SharingClub_bot.Youcanusethislinktostartchatwithhim:https://t.me/SharingClub_bot")
       await s.delete()
       return
   
    if user_input.lower() in ["malayalam", "you know malayalam"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery:{user_input}\n\nResults:\n\n Sorry guys i no know Malayalam please type English")
       await s.delete()
       return

    if user_input.lower() in ["how to create like you", "how to create like a bot"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery: <code>{user_input}</code>\n\nResults:\n\n First open chrome search:- https://console.cloud.google.com/ Then sign up with your google account, click on the nagivation mark.Click the API AND SERVICESclick the CREDENTIALS Click on the API KEY and then it will creating your api and copy your api key and use in bot. **")
       await s.delete()
       return

    if user_input.lower() in ["who is mrz thoppi ", "mrz thoppi"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery: <code>{user_input}</code>\n\nResults:\n\n Thoppi, also known as Muhammad Nihad is a resident of Kerala's Kannur district. He is a 24-year-old YouTube sensation. Thoppi, popular among the late Gen Z and Gen Alpha as a gamer, Thoppi's in-game name is MrZ Thoppi, a name feared and revered by many in the gaming battlegrounds. thippi hate ameen yana vazha he hete ameen **")
       await s.delete()
       return

    if user_input.lower() in ["who are you"]:
       await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nQuery: <code>{user_input}</code>\n\nResults:\n\n Iam TEST,Im developer by sharingClub. ")
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
    await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\n ǫᴜᴇʀʏ ɪs:- {user_input} {user_input}\n\nResults:\n\n{response.text}")         
    await client.send_message(LOG_CHANNEL, text=f"#google_ai ʀᴇǫᴜᴇsᴛ ғʀᴏᴍ {message.from_user.mention}\nǫᴜᴇʀʏ ɪs:- {user_input}")
    await s.delete()

@Client.on_message(filters.command("gpt"))
async def ai_generate_private(client, message):
  buttons = [[
    InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/SharVision_Support")
  ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ɪn 👇 ", reply_markup=reply_markup)
