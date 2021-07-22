from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Burada Reklamınız ola bilərdi ✓", url="https://t.me/MusiqiAzerbaycanYoutube")],
        [InlineKeyboardButton(
            "Əlaqə 😊", url="https://t.me/SeyidliAdem")]
    ])
    welcomed = f"Salam <b>{message.from_user.first_name}</b>\n/Help - Ətraflı məlumat almaq , ( Yükləmək isdədiyiniz musiqinin Yalnız Youtube linkini bota göndərin) "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
