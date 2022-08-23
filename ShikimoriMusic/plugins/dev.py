import os
import asyncio
import math

import heroku3
import requests

from ShikimoriMusic import pbot
from ShikimoriMusic.vars import SUDO_USERS
from pyrogram import Client, filters
from ShikimoriMusic.vars import HEROKU_APP_NAME, HEROKU_API_KEY
from ShikimoriMusic.setup.filters import command
from pyrogram.types import Message

heroku_api = "https://api.heroku.com"
Heroku = heroku3.from_key(HEROKU_API_KEY)

@Client.on_message(command("leave") & SUDO_USERS)
async def leave(message: Message):

    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/leave [CHAT ID]")
    query = message.text.strip().split(None, 1)[1]
    if query:
        chat_id = str(query[0])
        try:
            await pbot.leave_chat(int(chat_id))
        except:
            await message.reply_text(
                "Beep boop, I could not leave that group(dunno why tho).",
            )
            return
    else:
        await message.reply_text("Send a valid chat ID")

@Client.on_message(command("usage") & filters.user(SUDO_USERS))
async def dyno_usage(message: Message):
    """
    Get your account Dyno Usage
    """
    die = await message.reply_text("`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await die.edit_text("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    day = math.floor(hours / 24)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)

    return await die.edit_text(
        "❂ **Dyno Usage **:\n\n"
        f" » Dyno usage for **{HEROKU_APP_NAME}**:\n"
        f"      •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        "  » Dyno hours quota remaining this month:\n"
        f"      •  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
        f"\n\n  » Dynos heroku {day} days left"
    )