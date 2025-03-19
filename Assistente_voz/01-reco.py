import speech_recognition as sr
from gtts import gTTS
import os 
from playsound import playsound


def criar_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


criar_audio("dados/welcome.mp3", "Olá Vou reconhecer a Sua Voz")

reco = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga alguma Coisa:")
    audio =reco.listen(source)


frase= reco.recognize_google(audio, language='pt-br')
criar_audio("dados/mensagem.mp3", frase)