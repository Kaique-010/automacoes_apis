import speech_recognition as sr

reco = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga alguma coisa: \n")
    
    audio = reco.listen(source)

print(reco.recognize_google(audio, language="pt"))