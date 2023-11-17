import telebot
import whisper

model = whisper.load_model("small")


def recognize():

    result = model.transcribe("new_voice.ogg")
    print(result)
    return result['text']


bot = telebot.TeleBot("", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте, пришлите ваше голосовое!")


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("new_voice.ogg", 'wb') as file:
        file.write(downloaded_file)
    bot.reply_to(message, recognize())


bot.infinity_polling()
