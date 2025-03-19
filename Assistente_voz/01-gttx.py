from gtts import gTTS
from playsound import playsound
import os


def criar_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save("dados/mensagem.mp3")
    playsound("dados/mensagem.mp3")
    os.remove("dados/mensagem.mp3")


frase = input("Insira a Frase a ser falada: \n")
criar_audio(frase)

arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
criar_audio(conteudo)