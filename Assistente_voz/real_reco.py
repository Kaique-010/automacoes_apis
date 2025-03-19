from random import randint
import speech_recognition as sr
from gtts import gTTS
import os 
from playsound import playsound


def criar_audio(audio, mensagem):
    os.makedirs(os.path.dirname(audio), exist_ok=True)
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


criar_audio("dados/welcome.mp3", "Escolha um numero entre um a 10")


reco = sr.Recognizer()#instancia o recognizer 
with sr.Microphone() as source:#pega o audio do microfone e reconhece como source
    print("Diga alguma coisa")
    
    try:
        audio = reco.listen(source) #reconhece o source que o audio do microfone
        numero_texto = reco.recognize_google(audio, language="pt-br") #Reconhece e passa 
        print(f"Você disse {numero_texto}")   #Retorna com o audio     
   
    except sr.UnknownValueError:
        criar_audio("dados/error.mp3", "Não entendi o que você falou, repita por favor")
        exit()
    except sr.RequestError:
        criar_audio("dados/erro.mp3", "Erro ao acessar o reconhecimento")
        exit()
    

numero_texto = reco.recognize_google(audio, language="pt-br")
print(numero_texto)

word_to_digit = {
    "um": 1, 
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove":9,
    "dez": 10
         
}

numero_digito = word_to_digit.get(numero_texto)

if numero_digito is not None:
    criar_audio("dados/erro.mp3", "Numero Invalido Tente novamente")

resultado = randint(1,10)
print(f"Número sorteado: {resultado}")

if numero_texto == resultado:
    criar_audio("dados/venceu.mp3", "Parabéns você acertou o número")
else:
    criar_audio("dados/perdeu.mp3", f"Infelizmente vocÊ errou, Tente novamente,  o numero sorteado era {resultado}")