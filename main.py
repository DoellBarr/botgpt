from clients import bot
from pyrogram import filters, types, idle
import openai
from configs import configs

openai.api_key = configs.openai_apikey


@bot.on_message(filters.command("start"))
async def start_handler(_, m: types.Message):
    user = m.from_user
    return await m.reply(
        f"Hello {user.first_name}! Saya adalah bot chatgpt, silakan gunakan saya dengan mengetikkan /tanya [pertanyaan]"
    )


@bot.on_message(filters.command("tanya"))
async def tanya_handler(_, m: types.Message):
    commands = m.command
    if len(commands) < 2:
        return await m.reply("Kamu harus sertakan pertanyaan. Misalnya /tanya resep nasi rendang")
    x = await m.reply("`tunggu bentar bro...`")
    prompt = m.text.replace("/tanya ", "")
    max_tokens = 2000 - len(prompt.split(" "))
    result = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0,
        # suffix=">>> Jawaban:\n"
    )
    jawaban = result.choices[0].text
    return await x.edit(jawaban)


async def main():
    print("Bot dijalankan")
    await bot.start()
    nama_bot = bot.me.first_name
    username = bot.me.username
    print(f"Nama Bot: {nama_bot}")
    print(f"Username Bot: @{username}")
    print("Bot berjalan, silakan digunakan")
    await idle()


if __name__ == "__main__":
    bot.run(main())
