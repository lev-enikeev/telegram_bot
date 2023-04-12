from random import choice

with open("hangman.txt", "r", encoding='utf-8') as f:
    WORDS = [line.strip().lower() for line in f.readlines()]


class HangmanGame():
    def __init__(self):
        self.game_viseltsa = False

    def start(self):
        self.game_viseltsa = True
        self.word = choice(WORDS)
        self.wrong = 0
        self.used = []
        self.max_wrong = len(HANGMAN) - 1
        self.so_far = ["_"] * len(self.word)

    def info(self):
        c = HANGMAN[self.wrong]
        c += "\nВы использовали следующие буквы:\n"
        c += str(self.used)
        c += "\nНа данный момент слово выглядит так:\n"
        c += ' '.join(self.so_far)
        c += "\n\nВведите свое предположение: "
        return c

    def game_step(self, guess):
        if guess in self.used:
            return f'Вы уже вводили букву {guess}. Введите свое предположение:'
        else:
            self.used.append(guess)
            if guess in self.word:
                g_msg = f"\nДа! \" {guess} \" есть в слове!"
                indxs = [i for i in range(
                    len(self.word)) if self.word[i] == guess]
                for indx in indxs:
                    self.so_far[indx] = guess
                if self.so_far.count('_') == 0:
                    g_msg += f"\nВы угадали слово! {self.word}"
                    self.game_viseltsa = False
                else:
                    g_msg += self.info()
                return g_msg
            else:
                g_msg = f"\nИзвините, буквы \" {guess} \" нет в слове."
                self.wrong += 1
                if self.wrong >= self.max_wrong:
                    g_msg += HANGMAN[self.wrong]
                    g_msg += "\nТебя повесили!"
                    g_msg += f"\nПравильный ответ **{self.word}**"
                    self.game_viseltsa = False
                else:
                    g_msg += self.info()
                return g_msg


HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |    
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |      
     |   
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |     
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |    
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
    ---------
    """
)
