from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="☆𝐇𝐞𝐥𝐩☆", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆𝐒𝐮𝐩𝐩𝐨𝐫𝐭☆", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="☆𝐎𝐰𝐧𝐞𝐫☆", user_id=OWNER
            )
        ],
        [
        InlineKeyboardButton(

                text="☆𝐒𝐞𝐫𝐯𝐞𝐫☆",

                url="https://t.me/royal_official_server",

            ),
     ],
        ]
    return buttons
