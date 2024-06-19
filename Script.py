class script(object):
    START_TXT = """<blockquote>Hey 👋 {}, ᴍʏ ɴᴀᴍᴇ <a href=https://t.me/{}>{}</a></blockquote>
    
<b>🍿 Wᴇʟᴄᴏᴍᴇ Tᴏ Tʜᴇ Wᴏʀʟᴅ's Cᴏᴏʟᴇsᴛ Sᴇᴀʀᴄʜ Eɴɢɪɴᴇ!

Here You Can Request Movie's, Just Sent Movie OR WebSeries Name With Proper <a href='https://www.google.com'>Google</a> Spelling..!!</b>"""

    HELP_TXT = """<b>Hᴇʏ {} Fʀɪᴇɴᴅ Hᴇʀᴇ Yᴏᴜʀ Bᴜᴛᴛᴏɴs 👇</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code>
@ipapkorndbot</b>"""

    FCAPTION = """
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ : </b> <code>{file_name}</code>

<b>
╭──────── • ◆ • ────────╮
😎 Oᴡɴᴇʀ :  <a href="https://t.me/devbots2">DᴇᴠBᴏᴛs</a>
🎥 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ :  <a href="https://t.me/iPopkornBot_ipop_bot">IᴘᴀᴘKᴏʀɴ</a>
😒 Sᴜᴘᴘᴏʀᴛ :  <a href="https://t.me/champaklalbot">Aᴅᴍɪɴ</a>
╰──────── • ◆ • ────────╯</b>"""

    PRIVATEBOT_TXT = """<b>Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ

- ›› Mᴜsᴛ Aᴅᴅ Mᴇ Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ Oɴ Tʜɪs Gʀᴏᴜᴘ

- ›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect

- ›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ

- ›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>
"""

    MODS_TXT = """I Hᴀᴠᴇ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs"""

    PONGD_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""
    
    PONG_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""

    ABOUT_TXT = """📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 ʜᴏsᴛᴇᴅ ᴏɴ : Heroku</b>"""

    SOURCES_TXT = """📨 Sᴇɴᴅ Mᴏᴠɪᴇ Oʀ Sᴇʀɪᴇs Nᴀᴍᴇ ᴀɴᴅ Yᴇᴀʀ Aꜱ Pᴇʀ Gᴏᴏɢʟᴇ Sᴘᴇʟʟɪɴɢ..!! 👍

⚠️ Exᴀᴍᴘʟᴇ Fᴏʀ Mᴏᴠɪᴇ 👇

👉 Jailer
👉 Jailer 2023

⚠️ Exᴀᴍᴘʟᴇ Fᴏʀ WᴇʙSᴇʀɪᴇs👇

👉 Stranger Things 
👉 Stranger Things S02 E04

⚠️ ᴅᴏɴ'ᴛ ᴀᴅᴅ ᴇᴍᴏᴊɪꜱ ᴀɴᴅ ꜱʏᴍʙᴏʟꜱ ɪɴ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ, ᴜꜱᴇ ʟᴇᴛᴛᴇʀꜱ ᴏɴʟʏ..!! ❌"""

    SOURCE_TXT = """📨 Sᴇɴᴅ Mᴏᴠɪᴇ Oʀ Sᴇʀɪᴇs Nᴀᴍᴇ ᴀɴᴅ Yᴇᴀʀ Aꜱ Pᴇʀ Gᴏᴏɢʟᴇ Sᴘᴇʟʟɪɴɢ..!! 👍

⚠️ Exᴀᴍᴘʟᴇ Fᴏʀ Mᴏᴠɪᴇ 👇

👉 Jailer
👉 Jailer 2023

⚠️ Exᴀᴍᴘʟᴇ Fᴏʀ WᴇʙSᴇʀɪᴇs👇

👉 Stranger Things 
👉 Stranger Things S02 E04

⚠️ ᴅᴏɴ'ᴛ ᴀᴅᴅ ᴇᴍᴏᴊɪꜱ ᴀɴᴅ ꜱʏᴍʙᴏʟꜱ ɪɴ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ, ᴜꜱᴇ ʟᴇᴛᴛᴇʀꜱ ᴏɴʟʏ..!! ❌"""

    STATUS_TXT = """<b><b>Tᴏᴛᴀʟ Fɪʟᴇs Fʀᴏᴍ Bᴏᴛʜ DBs: <code>{}</code>
Bᴏᴛ Usᴇʀs ᴀɴᴅ Cʜᴀᴛs Cᴏᴜɴᴛ
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
Pʀɪᴍᴀʀʏ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛɪsᴛɪᴄs 
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
Sᴇᴄᴏɴᴅᴀʀʏ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛɪsᴛɪᴄs
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
</b>"""
    LOG_TEXT_G = """<b> #NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} </b>
"""
    LOG_TEXT_P = """<b> #NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} </b>
"""
