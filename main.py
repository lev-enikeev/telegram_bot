import telebot
from random import choice
from hangman_game import HANGMAN, HangmanGame
from text_to_speech import tex_to_speech, speech_to_text
from chatGPT import talk_to_chatGPT
from credentials import telegramTOKEN
bot = telebot.TeleBot(telegramTOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"<b>Привет</b> <u>{message.from_user.first_name}</u> <u>{message.from_user.last_name}</u>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['speech'])
def text_to_speech(message):
    text = message.text[8:]
    tex_to_speech(text)
    with open('msg.mp3', 'rb') as f:
        bot.send_audio(message.chat.id, f)


@bot.message_handler(commands=['chatGPT'])
def chatGPT(message):
    text = ' '.join(message.text.split(' ')[1:])
    answer = talk_to_chatGPT(text)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('audio.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, 'обрабатывется...')
    text = speech_to_text()
    bot.send_message(message.chat.id, text)

# =========================================================================


hg = HangmanGame()
hg.game_viseltsa = False


@bot.message_handler()
def get_user_text(message):
    if hg.game_viseltsa:
        game_message = hg.game_step(message.text)
        bot.send_message(message.chat.id, game_message)
    else:
        if message.text == "виселица":
            hg.start()
            game_message = "Давай поиграем в виселицу, я загадал слово из букв, попробуй отгадать\n" + hg.info()
            bot.send_message(message.chat.id, game_message)


bot.polling(none_stop=True)
