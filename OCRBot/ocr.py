import os
import pytesseract

from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty


# pytesseract.pytesseract.tesseract_cmd = r""

@Client.on_message(filters.private & filters.incoming & filters.photo)
async def _ocr(_, msg: Message):
    user_id = msg.from_user.id
    message_id = msg.id
    name_format = f"StarkBots_{user_id}_{message_id}"
    message = await msg.reply("Downloading and Extracting...", quote=True, disable_web_page_preview=True)
    image = await msg.download(file_name=f"{name_format}.jpg")
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    text = text[:-1]
    try:
        await message.edit_text(text)
    except MessageEmpty:
        await message.edit_text("Either the image has no text or the text is not recognizable.")
    os.remove(image)
