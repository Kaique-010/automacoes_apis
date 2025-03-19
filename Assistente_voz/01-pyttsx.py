import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

"""frase = input("Insira a Frase a Ser falada: \n")
engine.say(frase)
engine.runAndWait()
"""

arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
engine.say(conteudo)
engine.runAndWait()