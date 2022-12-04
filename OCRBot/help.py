from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

from Data import Data


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"), group=3)
async def _help(bot, msg) -> str:
    await bot.send_message(
        msg.chat.id,
        Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
