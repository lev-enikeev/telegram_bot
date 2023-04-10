from random import choice

with open("hangman.txt", "r", encoding='utf-8') as f:
    WORDS = [line.strip().lower() for line in f.readlines()]

class HangmanGame():
    def __init__(self):
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

