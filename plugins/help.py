from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Youtube Music və yaxud vide yükləmək isdəyirsinizsə mənə yükləmək isdədiyiniz videonun youtube linkini yollayın 😍 Məs : https://youtu.be/BaiBFQh4m1s . Əlavə sualınız olsa @SeyidliAdem profilinə yazın "
    await message.reply_text(helptxt)
