from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BrandrdXMusic import app

BOT_USERNAME = "heer_chatbot"

start_txt = """**
✪ 𝐉𝐀𝐊𝐄 ➻❥⏤͟͟͞͞𝐏𝐑𝐎𝐅𝐄𝐒𝐒𝐎𝐑💸⎯ꨄ 𝐊𝐎 𝐏𝐀𝐏𝐀 𝐁𝐎𝐋 ✪
 
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/TG_PROFESS0R"),
             InlineKeyboardButton("sɪᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url="https://t.me/MUSIC_BOT_UPDATE"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/OG_FRAINDS"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://envs.sh/ozv.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
