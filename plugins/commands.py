from Script import script
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, enums
from info import PICS, LOG_CHANNEL, MSG_ALRT
import os, random, asyncio
import time

CMD = ["/", "."]

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")

TEXT_TXT = """<b> Hᴇʟʟᴏ {}.

Mʏ Nᴀᴍᴇ Is {}.

I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇ Fᴏʀ Yᴏᴜ Jᴜsᴛ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Oʀ Jᴏɪɴ Oᴜʀ Gʀᴏᴜᴘ 🫶🏻🤍</b>"""

TEXT = """**Hai {},
I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).**
For Know More /help"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🥤 Channel", url = "https://t.me/LEXUSOTP"),
            InlineKeyboardButton("Support Group 🥤", url = "https://t.me/NibrasHacked")
        ],
        [
            InlineKeyboardButton("🧃 Repo", url = "https://t.me/herokuaccountBot"),
            InlineKeyboardButton("Deploy 🧃", url = "https://t.me/ajzalup")
        ],
        [
            InlineKeyboardButton("📍 Developer 📍", url = "https://t.me/xax_ha_ha_l")
        ]
    ]
)

HELP = """Hai {},
**There Is Nothing To Know More.**
- Send Me The Limit Of Your Password and Keys (optional)
  Like :-
    `10 abcd1234`
    `10`
- I Will Give The Password Of That Limit.
**Note :-**
• Only Digits Are Allowed
• Maximum Allowed Digits Till 100 (I Can't Generate Passwords Above The Length 84)"""

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),
            InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Password-Generator-Bot")
        ]
    ]
)

ABOUT = """--**About Me**--
**🤖 Bot :** Password Generator Bot
**🧑‍💻 Developer :** [M-fazin](https://github.com/M-fazin)
**💻 Channel :** @EKBOTZ_UPDATE
**☎️ Support :** @ekbotz_support
**🗂️ Source Code :** [Password Generator Bot](https://github.com/M-fazin/Password-Generator-Bot)
**⚙️ Language :** Python 3
**🛡️ Framework :** Pyrogram"""


@Client.on_message(filters.command("start", CMD))
async def start(_, message):
        buttons = [[
                    InlineKeyboardButton('⛦ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ⛦', url=f'http://t.me/oggyRbot?startgroup=true')
                ],[
                    InlineKeyboardButton('⚙️ ꜰᴜɴᴛɪᴏɴ ⚙️', callback_data="helpp"),
                    InlineKeyboardButton('🧭 ᴀʙᴏᴜᴛ 🧭', callback_data="stick")
                ],[
                    InlineKeyboardButton('🕸️ Hᴇʟᴩ', callback_data="file")
                  ]]
        m = await message.reply_sticker("CAACAgIAAxkBAAIve2XgRl5w5qGTeAjktaUi00daPTyLAAIGMAACER1xSFRMh-rQSCkpNAQ") 
        await asyncio.sleep(2)
        await message.reply_photo(photo=random.choice(PICS), caption=script.ABOUT_TXT, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
        return await m.delete()
        await query.answer(MSG_ALRT)

@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    await message.reply_text(
         text="<b>ʜᴇʏ ᴅᴜᴅᴇ 👋🏻 ,\n\nʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ any other messages ꜰʀᴏᴍ ʜᴇʀᴇ. ʀᴇǫᴜᴇsᴛ ᴏɴ ᴏᴜʀ <a href=https://t.me/xax_ha_ha_l>ʙᴏᴛ_ᴄʀᴇᴀᴛᴏʀ</a></b>",   
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ ", url=f"t.me/xax_ha_ha_l")]]),disable_web_page_preview=True)
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#𝐏𝐌_𝐌𝐒𝐆\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "file":
         buttons = [[
            InlineKeyboardButton(text="👇🏻", callback_data="rmbgwhite"),
            InlineKeyboardButton(text="👋🏻", callback_data="rmbgplain"),
            ],[
            InlineKeyboardButton(text="❗️", callback_data="rmbgsticker"),
            ],[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
            ]]
         await query.message.edit_text("**Select Required Mode**", reply_markup=InlineKeyboardMarkup(buttons))
           
    elif query.data == "stick":
           buttons = [[
            InlineKeyboardButton(text="👨🏼‍🦯", callback_data="stkr"),
            InlineKeyboardButton(text="😳", callback_data="cur_ved"),
            ],[                    
            InlineKeyboardButton(text="👀", callback_data="help")
            ],[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
            ]]              
           await query.message.edit("**Select A Type**", reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "start":
         buttons = [[
                    InlineKeyboardButton('⛦ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ⛦', url=f'http://t.me/oggyRbot?startgroup=true')
                ],[
                    InlineKeyboardButton('⚙️ ꜰᴜɴᴛɪᴏɴ ⚙️', callback_data="helpp"),
                    InlineKeyboardButton('🧭 ᴀʙᴏᴜᴛ 🧭', callback_data="stick")
                ],[
                    InlineKeyboardButton('🕸️ Hᴇʟᴩ', callback_data="file")
                  ]]
         await query.message.edit_text("**Select Required Mode**", reply_markup=InlineKeyboardMarkup(buttons))
         await query.answer(MSG_ALRT)
    elif query.data == "helpp":
           buttons = [[
            InlineKeyboardButton(text="🫂", callback_data="stkr"),
            InlineKeyboardButton(text="😅", callback_data="cur_ved"),
            ],[                    
            InlineKeyboardButton(text="😌", callback_data="help")
            ],[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
            ]]              
           await query.message.edit("**Select A Type**", reply_markup=InlineKeyboardMarkup(buttons))
           await query.answer(MSG_ALRT) 

