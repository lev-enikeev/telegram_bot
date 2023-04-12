import gtts
import speech_recognition as sr
from pydub import AudioSegment


def tex_to_speech(msg):
    tts = gtts.gTTS(msg, lang="ru")
    tts.save("msg.mp3")


def ogg2wav(ofn):
    wfn = ofn.replace('.ogg', '.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')


def speech_to_text():
    ofn = 'audio.ogg'
    ogg2wav(ofn)
    r = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text
