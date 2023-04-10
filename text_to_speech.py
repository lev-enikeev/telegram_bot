import gtts
from playsound import playsound


def convert(msg):
    tts = gtts.gTTS(msg, lang="ru")
    tts.save("msg.mp3")