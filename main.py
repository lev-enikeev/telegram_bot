import telebot
from random import choice
from hangman_game import HANGMAN, HangmanGame
from text_to_speech import convert
from chatGPT import talk_to_chatGPT
import creditials
bot = telebot.TeleBot(creditials.telegramTOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"<b>Привет</b> <u>{message.from_user.first_name}</u> <u>{message.from_user.last_name}</u>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['speech'])
def text_to_speech(message):
    text = message.text[8:]
    convert(text)
    with open('msg.mp3', 'rb') as f:
        bot.send_audio(message.chat.id, f)


@bot.message_handler(commands=['chatGPT'])
def chatGPT(message):
    text = ' '.join(message.text.split(' ')[1:])
    answer = talk_to_chatGPT(text)
    bot.send_message(message.chat.id, answer)


# =========================================================================



hg = HangmanGame()
hg.game_viseltsa = False


@bot.message_handler()
def get_user_text(message):
    if hg.game_viseltsa:
        guess = message.text

        if guess in hg.used:
            bot.send_message(message.chat.id,
                             f'Вы уже вводили букву {guess}. Введите свое предположение:')
        else:
            hg.used.append(guess)
            if guess in hg.word:
                c = f"\nДа! \" {guess} \" есть в слове!"
                indxs = [i for i in range(len(hg.word)) if hg.word[i] == guess]
                for indx in indxs:
                    hg.so_far[indx] = guess
                if hg.so_far.count('_') == 0:
                    c += f"\nВы угадали слово! {hg.word}"
                    hg.game_viseltsa = False
                else:
                    c += hg.info()
                bot.send_message(message.chat.id, c)
            else:
                c = f"\nИзвините, буквы \" {guess} \" нет в слове."
                hg.wrong += 1
                if hg.wrong >= hg.max_wrong:
                    c += HANGMAN[hg.wrong]
                    c += "\nТебя повесили!"
                    hg.game_viseltsa = False
                else:
                    c += hg.info()
                bot.send_message(message.chat.id, c)
    else:
        if message.text == "виселица":
            hg.game_viseltsa = True
            hg.__init__()
            bot.send_message(
                message.chat.id, "Давай поиграем в виселицу, я загадал слово из букв, попробуй отгадать\n" + hg.info())


bot.polling(none_stop=True)
