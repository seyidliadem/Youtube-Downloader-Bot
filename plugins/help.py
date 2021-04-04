from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Youtube Music və yaxud vide yükləmək isdəyirsinizsə mənə yükləmək isdədiyiniz videonun youtube linkini yollayın 😍"
    await message.reply_text(helptxt)
