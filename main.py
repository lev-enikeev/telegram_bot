import telebot
import os
from random import choice
from game import HANGMAN

bot = telebot.TeleBot('6191246167:AAExRk5YkSN8w1JUhrWheop9Ndra8C9f5F8')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"<b>Привет</b> <u>{message.from_user.first_name}</u> <u>{message.from_user.last_name}</u>"
    bot.send_message(message.chat.id,mess, parse_mode='html')

game_viseltsa = False

max_wrong = len(HANGMAN) - 1
WORDS = ("python", "игра", "программирование")  # Слова для угадывания

word = choice(WORDS)  # Слово, которое нужно угадать
so_far = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
wrong = 0  # Количество неверных предположений, сделанных игроком
used = []  # Буквы уже угаданы

type_otv = 1

def vopros1():
    global so_far
    global used
    c = HANGMAN[wrong]  # Вывод висельника по индексу
    c += "\nВы использовали следующие буквы:\n"
    c += str(used)
    c += "\nНа данный момент слово выглядит так:\n"
    c += so_far

    c += "\n\nВведите свое предположение: "  # Пользователь вводит предполагаемую букву
    return c


@bot.message_handler()
def get_user_text(message):
    global game_viseltsa
    global type_otv

    global max_wrong 
    global WORDS

    global word
    global so_far
    global wrong
    global used

    if game_viseltsa:
        guess = message.text
        if type_otv == 1:

            if guess in used:
                c = "Вы уже вводили букву"
                c += guess  # Если буква уже вводилась ранее, то выводим соответствующее сообщение
                c += "Введите свое предположение: "  # Пользователь вводит предполагаемую букву
                bot.send_message(message.chat.id, c)
            else:
                used.append(guess)  # В список использованных букв добавляется введённая буква

                if guess in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
                    c = "\nДа! \""
                    c += guess
                    c += "\" есть в слове!"

                    new = ""
                    for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                        if guess == word[i]:
                            new += guess
                        else:
                            new += so_far[i]
                    so_far = new
                    if so_far == word:
                        c += "\nВы угадали слово!"
                        game_viseltsa = False
                    else:
                        c += vopros1()
                    bot.send_message(message.chat.id, c)
                else:
                    c = "\nИзвините, буквы \"" 
                    c += guess 
                    c += "\" нет в слове."  # Если буквы нет, то выводим соответствующее сообщение
                    wrong += 1

                    if wrong >= max_wrong:
                        c += HANGMAN[wrong]
                        c += "\nТебя повесили!"
                        game_viseltsa = False
                    else:
                        c += vopros1()

                    bot.send_message(message.chat.id, c)

    else:
        if message.text == "виселица":
            wrong = 0
            type_otv = 1
            game_viseltsa = True
            used = []
            word = choice(WORDS)  # Слово, которое нужно угадать
            so_far = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
            bot.send_message(message.chat.id, "Давай поиграем в виселицу, я загадал слово из букв, попробуй отгадать\n" + vopros1())
            
    
bot.polling(none_stop=True)