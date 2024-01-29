class script(object):
    START_TXT = """Sᴀʟᴜᴛ🖐  {},
Mᴏɴ Nᴏᴍ ᴇsᴛ <a href=https://t.me/{}>{}</a>, Jᴇ ᴘᴇᴜx ᴛᴇ ғᴏᴜʀɴɪʀ ᴅᴇs ғɪʟᴍs ᴇᴛ ᴅᴇs sᴇ́ʀɪᴇs﹐ ɪʟ sᴜғғɪᴛ ᴊᴜsᴛᴇ ᴅᴇ ʀᴇᴊᴏɪɴᴅʀᴇ ᴍᴇs ᴄᴀɴᴀᴜx ᴇᴛ ᴅᴇ ᴘʀᴏғɪᴛᴇʀ 😍"""
    HELP_TXT = """ {}
Je ѕυιѕ la Belle Alice de Sнαrιɴɢ Clυв!
✯ Retɾouvez ɑ̀ tɾɑveɾs ce menu quelques-unes de mes nouvelles compétences.
✯ P.S : Rejσiƍƞez <a href=https://t.me/Katnices><b>Kɑtƞice Cɦɑƞelle</b></a> 🥰😘."""

    # ⚠️ Please don't change our credits 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 & 𝙳𝙴𝚅 👇🏻

    ABOUT_TXT = """
╭───[<b>🔅Ꮪꮋꭺꭱꮖɴꮐ Ꮯꮮꮜᏼ🔅</b>]────⍟
│
├🔸🤖 Moɴ ɴoм: Mιѕѕ {}
│
├🔸📝 Lαɴɢυαɢe: <a href=https://www.python.org><b>Ƥутнση3</b></a>
│
├🔹📚 Bιвlιoтнèqυe: <a href=https://docs.pyrogram.org><b>Pчrogrαm</b></a>
│
├🔹📡 Héвerɢé ѕυr: <a href=https://t.me/Belle_Alice><b>ƁєƖƖє AƖιcє</b></a>
│
├🔸👨‍💻 Développeυr: <a href=https://t.me/SharingClub_bot><b>Sʋpeɾ Mɑƞ</b></a> 
│
├🔹👥 Groυpe d'αιde: <a href=https://t.me/Shar_Group><b>Sʋppσɾt</b></a> 
│
├🔸🔔 Mα Cнαι̂ɴe: <a href=https://t.me/Katnices><b>Kɑtƞice Cɦɑƞƞel</b></a>
│
╰─────────[ 😎 ]────────⍟ """

    SOURCE_TXT = """<b>Cɾéɑteʋɾ</b> 
🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴘᴇᴜʀ: <a href=https://t.me/SharingClub_bot><b>🦸‍Sʋpeɾ Mɑƞ</b></a>
       Quı est Super mαn 🎖?
•¬Je suıs sourıαnt et j’αıme le contαct αvec les gens, comme un commercıαl.
•¬Je suıs sчmpαthıque mαıs je peux αussı être désαgréαble.
•¬Je suıs tımıde αvec les femmes, mαıs quαnd je suıs lαncé, je vαıs jusqu’αu bout. 
•¬Je suıs sérıeux dαns mon trαvαıl, tel un scıentıfıque. 
•¬Je suıs servıαble quαnd on me demαnde quelque chose αvec polıtesse. 
•¬Je suıs généreux comme lα Croıx-Rouge. 
•¬Je suıs αrrogαnt αvec les personnes quı me mαnque de respect. 
•¬Je ne suıs pαs du genre jαloux. Je ne suıs pαs du genre égoı̈ste. Je pαrtαge souvent ce que j'αı.
•¬Je suıs pαrfoıs long ὰ lα détente, mαıs quαnd je suıs lαncé, le trαvαıl serα bıen fαıt."""

    MANUELFILTER_TXT = """ <b>❤️‍🩹 Dσɳɑtiσɳ 💝</b>

🎗Nous ɑvons besoin de votre ɑide ɑujourd’hui pour continuer ɑ̀ vous fournir des contenus de quɑlités ɑ̀ trɑvers nos plɑteformes et bots.🎗

« Seriez-vous prêt ɑ̀ ɑider en fɑisɑnt un don 💝 ? Chɑque centime ɑiderɑ. »

« Fɑire un don ❤️‍🩹 est une fɑçon de tendre une mɑin secourɑble. 

En fɑisɑnt même un petit don💞, vous pouvez pɑrticiper ɑ̀ un effort visɑnt ɑ̀  mɑintenir les cɑnɑux Shɑring Club, lɑ Belle Alice et Kɑtnice en vie.

🤲 Merci de Contribuer ɑ̀ l'hébergement et ɑux frɑis d'ɑbonnement indispensɑbles pour lɑ survie de notre communɑuté. »

<b>🗒 Liste ɗes Dσɳɑteʋɾs</b>"""

    BUTTON_TXT = """Aide: <b>Bouttons</b>

- Bᴇʟʟᴇ Aʟɪᴄᴇ prends en charge les Boutons en ligne d’URL et d’alerte.

<b>NOTE:</b>
1. Telegram ne vous permettra pas d’envoyer des boutons sans aucun contenu, le contenu est donc obligatoire.
2. Ꮮꭺ Ᏼꭼꮮꮮꭼ Ꭺꮮꮖꮯꭼ prend en charge les boutons avec n’importe quel type de média de télégramme.
3. Les boutons doivent être correctement Analysés

<b>URL Buttons:</b>
<code>Bᴇʟʟᴇ Aʟɪᴄᴇ votre meilleure amie 😘</code>

<b>Boutons d'alerte:</b>
<code>Un petit secret🤫 : Je suis la soeur de Katnice</code>"""

    AUTOFILTER_TXT = """Aide: <b>Filtre Auto</b>

<b>NOTE:</b>
1. Faites de moi un administratrice de votre chaîne même si elle est privée.
2. Assurez-vous que votre chaîne ne contient pas de porno, des fichiers soumis aux droits d'auteurs ou à caractères businness.
3. Transférez-moi le dernier message avec citations.
 J’ajouterai tous les fichiers de ce canal à ma Base de Donnée."""

    CONNECTION_TXT = """Aide: <b>Connections</b>

- Utilisez la connexion en PM pour la gestion des filtres 
- Il permet d’éviter le spamming dans les groupes.

<b>NOTE:</b>
1. Seuls les administrateurs peuvent ajouter une connexion.
2. Envoyer <code>/connect</code> pour me connecté à votre PM

<b>Commandes et utilisation:</b>
• /connect  - <code>connecter un chat particulier à votre PM</code>
• /disconnect  - <code>se déconnecter d’un chat</code>
• /connections - <code>Listes de toutes vos connexions</code>"""

    EXTRAMOD_TXT = """ <b>𝖡𝗂𝖾𝗇𝗍𝗈̂𝗍 𝖽𝗂𝗌𝗉𝗈𝗇𝗂𝖻𝗅𝖾...</b>

𝖤́𝖼𝗁𝖺𝗇𝗀𝖾𝗓 𝖽𝗂𝗋𝖾𝖼𝗍𝖾𝗆𝖾𝗇𝗍 𝖺𝗏𝖾𝖼 𝖲𝗎𝗉𝖾𝗋 𝖬𝖺𝗇, 𝗅’𝗎𝗇𝗂𝗊𝗎𝖾 𝖼𝗋𝖾́𝖺𝗍𝖾𝗎𝗋 𝖽𝖾 𝖲𝗁𝖺𝗋𝗂𝗇𝗀 𝖢𝗅𝗎𝖻 𝖾𝗍 𝖽𝖾 𝖼𝖾𝗌 𝖻𝗈𝗍𝗌."""

    SONG_TXT = """<b>Tᴇ́ʟᴇ́ᴄʜᴀʀɢᴇᴍᴇɴᴛ ᴅᴇ ᴄʜᴀɴsᴏɴs</b>

<i>Modᥙᥣᥱ dᥱ tᥱ́ᥣᥱ́ᥴhᥲrgᥱmᥱᥒt dᥱ ᥴhᥲᥒsoᥒs, ρoᥙr ᥴᥱᥙx qᥙι ᥲιmᥱᥒt ᥣᥲ mᥙsιqᥙᥱ. 
Voᥙs ρoᥙvᥱz ᥙtιᥣιsᥱr ᥴᥱttᥱ foᥒᥴtιoᥒᥒᥲᥣιtᥱ́ ρoᥙr tᥱ́ᥣᥱ́ᥴhᥲrgᥱr ᥒ’ιmρortᥱ qᥙᥱᥣᥣᥱ ᥴhᥲᥒsoᥒ ᥲvᥱᥴ ᥙᥒᥱ vιtᥱssᥱ sᥙρᥱr rᥲριdᥱ. 
Foᥒᥴtιoᥒᥒᥱ dᥲᥒs ᥣᥱs groᥙρᥱs.../</i>

<b>Cᴏᴍᴍᴀɴᴅᴇs</b>

⏭️ /song ɴᴏᴍ ᴅᴇ ʟᴀ ᴄʜᴀɴsᴏɴ 

<b>Fonctionne ɑ̀ lɑ fois en Gɾoupe et en PM</b>"""

    VIDEO_TXT = """Cᴇ Mᴏᴅᴜʟᴇ ᴠᴏᴜs ᴀɪᴅᴇʀᴀ ᴀ̀ ᴛᴇ́ʟᴇ́ᴄʜᴀʀɢᴇʀ ᴅᴇs ᴠɪᴅᴇ́ᴏs ᴀ̀ ᴘᴀʀᴛɪʀ ᴅᴇ YᴏᴜTᴜʙᴇ.
• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>

⚠️ This feature not available"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /help - To get help.

• /ping - <b>To get your ping.</b>

<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""

    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID

  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚

◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT = """⚙️ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @HORRIDduo"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT = """<b>WHOIS MODULE</b>
Note:- <b>Dᴏɴɴᴇʀ ᴅᴇs ᴅᴇ́ᴛᴀɪʟs sᴜʀ ᴜɴ ᴜᴛɪʟɪsᴀᴛᴇᴜʀ</b>

•/whois :-Doᥒᥒᥱr ᥲ̀ ᥙᥒ ᥙtιᥣιsᥲtᥱᥙr toᥙs ᥣᥱs dᥱ́tᥲιᥣsoᥒᥒᥱr ᥲ̀ ᥙᥒ ᥙtιᥣιsᥲtᥱᥙr toᥙs ᥣᥱs dᥱ́tᥲιᥣs 📑"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT = """<b>Gᴀᴍᴇs</b> 

<b>⚡ Jᥙstᥱ ᥙᥒ gᥱᥒrᥱ dᥱ ᥴhosᥱs ⚡</b>

𝟣. /dice - Lᴀɴᴄᴇᴢ ʟᴇs ᴅᴇ́s 
𝟤. /Throw 𝗈𝗋 /Dart - Fᴀɪʀᴇ ᴜɴᴇ ғʟᴇ́ᴄʜᴇᴛᴛᴇ
3. /Goal or /Shoot - Pᴏᴜʀ ᴍᴀʀϙᴜᴇʀ ᴜɴ ʙᴜᴛ ᴏᴜ ᴛɪʀᴇʀ
4. /luck or /cownd - Tᴏᴜʀɴᴇ ᴇᴛ ᴛᴇɴᴛᴇ ᴛᴀ ᴄʜᴀɴᴄᴇ"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
Ce module ne fonctionne que pouɾ mes ɑdministɾɑteuɾs

<b>Commᥲᥒdᥱs ᥱt ᥙtιᥣιsᥲtιoᥒ:</b>
• /logs - <code>To get the rescent errors</code>
• /stats - <code>To get status of files in db.</code>
• /delete - <code>To delete a specific file from db.</code>
• /users - <code>To get list of my users and ids.</code>
• /chats - <code>To get list of the my chats and ids </code>
• /leave  - <code>To leave from a chat.</code>
• /disable  -  <code>Do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>To unban a user.</code>
• /channel - <code>To get list of total connected channels</code>
• /broadcast - <code>To broadcast a message to all users</code>
• /grp_broadcast - <code>To broadcast a message to all groups</code>
• /gfilter - <code>To add global filter</code>
• /gfilters - <code>To view global filters</code>
• /delallg - <code>To delete all global filters from database</code>
• /delg - <code>To delete a specific global filter</code>
• /setskip - <code>Skip no of files before indexing</code>
• /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>
• /deletefiles - <code>Delete CamRip and PreDvD files delete from database </code>"""

    STATUS_TXT = """<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b>"""

    CARB_TXT = """<b>Help</b> : 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""

    LOG_TEXT_G = """#NewGroup
𝖦𝗋𝗈𝗎𝗉𝖾 = {}(<code>{}</code>)
𝖬𝖾𝗆𝖻𝗋𝖾𝗌 𝖳𝗈𝗍𝖺𝗅 = <code>{}</code>
𝖠𝗃𝗈𝗎𝗍𝖾𝗋 𝗉𝖺𝗋 - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
𝖭𝗈𝗆 - {}
"""
    FILE_MSG = """
<b>Yo 👋 {} </b>😍

<b>📫 Votɾe fichieɾ est pɾêt</b>

<b>📂 Nᴏᴍ </b> : <code>{}</code>              

<b>⚙️ Tᴀɪʟʟᴇ </b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Yo 👋 {}</b> 😍

<code>{}</code>

<b>En rɑison des droits d'ɑuteur, le fichier serɑ supprimé d’ici dɑns 10 minutes, ɑlors téléchɑrgez-le ɑprès l’ɑvoir déplɑcé d’ici vers un ɑutre endroit ou sɑuvegɑrdez-le dɑns votre cloud ☁️ !</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """
<b>
SALUT {},
Mon nom est  <a href=https://t.me/{}>{}</a>, Je peux te fouɾniɾ des films et séɾies; Pouɾ en pɾofiteɾ, il suffit de ɾejoindɾe mes gɾoupes et cɑnɑux. 
</b>
"""

    IMDB_TEMPLATE_TXT = """
<b>🔖 Tɪᴛʀᴇ :<a href={url}>{title}</a>

🎭 Gᴇɴʀᴇ : {genres}
🎖 Nᴏᴛᴀᴛɪᴏɴ : <a href={url}/ratings>{rating}</a> / 10 (Bᥲsᥱ́ sᥙr ᥣ’ᥱ́vᥲᥣᥙᥲtιoᥒ dᥱ {votes} ᥙtιᥣιsᥲtᥱᥙrs.)

📆 Aɴɴᴇ́ᴇ : {release_date}
🗞 Lᴀɴɢᴜᴀɢᴇ : {languages}
🌎 Pᴀʏs : {countries}

©{message.chat.title}</b>
"""

    CUSTOM_FILE_CAPTION = """<b>📂 Nom du fıchıer : {file_name}
🟢 Ŋσʋνeɑʋtés ➡️ @Sharing_Club
</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇᴅᴇ́ᴍᴀʀʀᴇ́ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Hᴇᴜʀᴇ : <code>{}</code>
🌐Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Sɑlut {} 😍, Bienvenue ɑ̀  {} Groupe ❤️"""

    ALRT_TXT = """Cᴇ ɴ’ᴇsᴛ ᴘᴀs ᴘᴏᴜʀ ᴠᴏᴜs ʙᴏss"""

    OLD_ALRT_TXT = """Vous utilisez l’un de mes ɑnciens messɑges, merci d’envoyer une nouvelle requête"""

    TOP_ALRT_MSG = """♻️ 𝖵𝖾́𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝖽𝗎 𝖿𝗂𝖼𝗁𝗂𝖾𝗋 𝖽𝖺𝗇𝗌 𝗆𝖺 𝖻𝖺𝗌𝖾 𝖽𝖾 𝖽𝗈𝗇𝗇𝖾́𝖾𝗌... ♻️"""

    MVE_NT_FND = """<b>Cᴇ ғɪʟᴍ ɴ’ᴇsᴛ ᴘᴀs ᴇɴᴄᴏʀᴇ sᴏʀᴛɪ ᴏᴜ ᴀᴊᴏᴜᴛᴇ́ ᴀ̀ ᴍᴀ ʙᴀsᴇ ᴅᴇ ᴅᴏɴɴᴇ́ᴇs</b> """

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """Sᴀʟᴜᴛ {}  Jᴇ ɴ’ᴀɪ ᴛʀᴏᴜᴠᴇ́ ᴀᴜᴄᴜɴ ғɪʟᴍ ᴘᴏʀᴛᴀɴᴛ ᴄᴇ ɴᴏᴍ. 

FORMAT DE DEMANDE DE FILM

➠ ᴀʟʟᴇʀ sᴜʀ Gᴏᴏɢʟᴇ 
➠ ᴛᴀᴘᴇᴢ ʟᴇ ɴᴏᴍ ᴅᴜ ғɪʟᴍ
➠ ᴄᴏᴘɪᴇᴢ ʟᴇ ɴᴏᴍ ᴄᴏʀʀᴇᴄᴛ
➠ ᴄᴏʟʟᴇʀ ᴅᴀɴs ʟᴇ ɢʀᴏᴜᴘᴇ 

Exemple : Freelɑnce 2023

🚯 N·ᴜᴛɪʟɪsᴇʀ ᴘᴀs ➠ ' : ( ! , . / )"""

    I_CUD_NT = """Sᴀʟᴜᴛ {} Je n'ɑi ɾien tɾouvé ɑ̀ ce sujet, véɾifiez votɾe oɾthogɾɑphe."""

    CUDNT_FND = """Sᴀʟᴜᴛ {} Je n’ɑi rien trouvé ɑ̀ ce sujet, vouliez-vous dire l’un de ces ..."""

    REPRT_MSG = """ Signɑler ɑ̀ l’ɑdministrɑteur"""

    CON_TXT = """<b><u>Infos 𝖯ɑys</b></u>

<b>𝖢𝖾 𝗆𝗈𝖽𝗎𝗅𝖾 𝗉𝖾𝗋𝗆𝖾𝗍 𝖽𝖾 𝗍𝗋𝗈𝗎𝗏𝖾𝗋 𝖽𝖾𝗌 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇𝗌 𝗌𝗎𝗋 𝗅𝖾𝗌 𝗉𝖺𝗒𝗌</b>

• /country [𝖭𝗈𝗆 𝖽𝗎 𝗉𝖺𝗒𝗌] 
Exᴇᴍᴘʟᴇ :- <code>/country 𝖥𝗋𝖺𝗇𝖼𝖾</code>"""

    OPNAI_TXT = """ᴏᴘᴇɴᴀɪ ɪꜱ ᴀ ᴀɪ ꜱʏꜱᴛᴇᴍ ᴛʜᴀᴛ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜰɪɴᴅ ᴀɴꜱᴡᴇʀ ᴏꜰ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ ʙᴏᴛ ᴘᴍ.

ʜᴏᴡ ᴛᴏ ᴜꜱᴇ

/ᴏᴘᴇɴᴀɪ ᴡʜᴀᴛ ɪꜱ ᴀᴘᴘᴇɴᴅ ᴍᴇᴛʜᴏᴅ ɪɴ ᴘʏᴛʜᴏɴ
"""

    DISC_TXT = """Tous les fichiers de ce bot sont disponibles grɑtuitement sur Internet ou postés pɑr quelqu’un d’ɑutre. Ce bot indexe les fichiers qui sont déjɑ̀ téléchɑrgés sur Telegrɑm pour fɑciliter lɑ recherche, nous respectons toutes les lois sur le droit d’ɑuteur et trɑvɑillons en conformité ɑvec DMCA et EUCD. Si quelque chose est contrɑire ɑ̀ lɑ loi, veuillez nous contɑcter ɑfin qu’il puisse être supprimé dès que possible"""
    
    KD_CNL = """
<b>⍟ Mᴏᴅᴜʟᴇ Cᴀɴᴀᴜx ﹠ Gʀᴏᴜᴘᴇs ⍟</b>

<b>🎬 Mᴇɪʟʟᴇᴜʀ Gʀᴏᴜᴘᴇ ᴅᴇ Dᴇᴍᴀɴᴅᴇ ᴅᴇ Fɪʟᴍ.
📢 Cᴀɴᴀᴜx Fɪʟᴍs ﹠ Sᴇ́ʀɪᴇs ᴅᴀɴs Pʟᴜsɪᴇᴜʀs Lᴀɴɢᴜᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘᴇ.</b>
"""

