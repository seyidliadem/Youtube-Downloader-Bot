from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Musiqi Kanalımız ✓", url="https://t.me/MusiqiEuphoria")],
        [InlineKeyboardButton(
            "Əlaqə 😊", url="https://t.me/SeyidliAdem")]
    ])
    welcomed = f"Salam <b>{message.from_user.first_name}</b>\n/Help - Ətraflı məlumat almaq"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
