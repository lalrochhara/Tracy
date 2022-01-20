import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Tracy.events import register
from Tracy import telethn as tbot


PHOTO = "https://telegra.ph/file/7d2fab979a7f4b5dd3af5.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Tracy Robot.** \n\n"
    TEXT += "♤ **I'm Working Properly** \n\n"
    TEXT += f"♤ **My Master : [Tracy](https://t.me/Tracyuuuu)** \n\n"
    TEXT += f"♤ **Library Version :** `{telever}` \n\n"
    TEXT += f"♤ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"♤ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/TracyMusicBot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/TracySupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
