import os
from openai import OpenAI
from dotenv import load_dotenv
import pyttsx3 as ts
import speech_recognition as sr
engine=ts.init()

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)
print("Hi! I am your Assistant how can i help you Master!")
engine.say("HI! I am your Assistant how can i help you Master!")
engine.runAndWait()
print("Choose: \n 1 : text input \n other : voice input \n To exit : 0")
n=int(input())
if(n==0):
    print("Exited")
else:
    if(n==1):
        message=input("YOU : ")
    else:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            audio=r.listen(source)
            try:
                message=r.recognize_google(audio)
                print("You said :",message)
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError:
                print("Speech recognition service error.")
    message=message
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":message}]
    )
    reply=response.choices[0].message.content
    print(reply)
    engine.say(reply)
    engine.runAndWait()