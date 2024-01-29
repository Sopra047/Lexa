from pyrogram import Client, filters , enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import random
import time
from info import *
import asyncio


@Client.on_message(filters.command("gpt"))
async def ai_res(message ,query):
    try:
        userMention = message.from_user.mention()
        url = f'https://bisal-nothing-org.koyeb.app/biisal?query={query}&bot_name={BOT_NAME}&bot_admin={ADMIN_NAME}' #dont try to change anything here ⚠️
        res = requests.get(url)
        if res.status_code == 200:
            response_json = res.json()  
            api_response = response_json.get('response')  
            if len(query) <= 280:
                await message.reply_text(text=f"<b>hey {userMention}\nʏᴏᴜʀ ǫᴜᴇʀʏ : <code>{cut_query_str}</code>\n\n{BOT_NAME} :\n{api_response}</b>")
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "MOVIE", url=f"https://t.me/fndnfmfkrk"
                                )
                            ]
                        ]
                    ),
                    disable_web_page_preview=True,                                       

                    )
            else:
                cut_query_str = query[:77]
                await message.reply_text(text=f"<b>hey {userMention}\nʏᴏᴜʀ ǫᴜᴇʀʏ : <code>{cut_query_str}</code>\n\n{BOT_NAME} :\n{api_response}</b>")
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "MOVIE", url=f"https://t.me/fndnfmfkrk"
                                )
                            ]
                        ]
                    ),
                    disable_web_page_preview=True,                                       
