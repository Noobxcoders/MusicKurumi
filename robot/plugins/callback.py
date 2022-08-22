#
# Copyright (C) by M8N@Github, < https://github.com/UnknownMortal >.
#
# This file is part of < https://github.com/UnknownMortal/Music-Bot-v2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UnknownMortal/Music-Bot-v2/blob/main/LICENSE >
#
# All rights reserved !!


from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from robot.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴡᴇʟᴄᴏᴍᴇ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ɪ ᴀᴍ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

ᴜsᴇ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ !!""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗂 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cmds"),
                    InlineKeyboardButton(
                        "🆘 ʜᴇʟᴘ", url=f"https://t.me/{SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "✚ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "📡 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATE}"),
                    InlineKeyboardButton(
                        "☁️ ᴏᴛʜᴇʀs", callback_data="others")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ ʜᴇʀᴏᴋᴜ", url=f"https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.heroku.com/&ved=2ahUKEwj05-Kp0rL4AhVFT2wGHXu5BRYQFnoECAwQAQ&usg=AOvVaw1V4lhSv6mb_lZj6UUCUXpS"),
                    InlineKeyboardButton(
                        "🌐 ɢɪᴛʜᴜʙ", url=f"https://github.com/UnknownMortal/Music-Bot-v2")
                ],
                [
                    InlineKeyboardButton(
                        "🍭 ᴄʀᴇᴅɪᴛs", callback_data="credit"),
                    InlineKeyboardButton(
                        "🍀 ʀᴇᴘᴏ ɪɴғᴏ", callback_data="repoinfo")
                ],
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="home")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("credit"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴄʀᴇᴅɪᴛs ғᴏʀ ᴛʜɪs ʙᴏᴛ 🍀

• @Its_romeoo 
- ʀᴇᴘᴏ ᴅᴇᴠᴇʟᴏᴘᴇʀ !! 

• @Cool_Mortal
- sᴜᴘᴘᴏʀᴛ & ᴜᴘᴅᴀᴛᴇs ᴍᴀɪɴᴛᴀɪɴᴇʀ

• @{OWNER_USERNAME}
- ʙᴏᴛ ᴏᴡɴᴇʀ


ᴛʜᴀɴᴋs ᴀ ʟᴏᴛ ғᴏʀ ᴄᴏɴᴛʀɪʙᴜᴛɪɴɢ ʏᴏᴜʀ ᴛɪᴍᴇ ᴀɴᴅ sᴋɪʟʟs !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
    )



@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 

ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

ғᴏɴᴛ ᴜsᴇᴅ : sᴍᴀʟʟ ᴄᴀᴘs

🔗 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : https://github.com/UnknownMortal/Music-Bot-v2""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
