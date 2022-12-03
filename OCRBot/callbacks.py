from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery

from Data import Data


# Callbacks
@Client.on_callback_query(group=2)
async def _callbacks(bot, callback_query: CallbackQuery) -> None:
    mention = bot.me.mention
    if callback_query.data.lower() == "home":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.START.format(callback_query.from_user.mention, mention),
            reply_markup=InlineKeyboardMarkup(Data.buttons),
        )
    elif callback_query.data.lower() == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif callback_query.data.lower() == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**Here's How to use me**\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
