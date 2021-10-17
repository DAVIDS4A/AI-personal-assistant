# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:17:03 2021

@author: DAVID SHYAKA
"""


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os 
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

print('Loading your AI personal assistant- David')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', 'voices[1].id')

def speak (text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, good morning")
        print("Hello, good morning")
        
    elif hour>=12 and hour<18:
        speak("Hello,Good afternoon")
        print("Hello,Good afternoon")
    else:
        speak("Hello,Good evening")
        print("Hello, Good evening")
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio,language = 'en-in')
            print(f"user said:{statement}\n")
            
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
    
speak("Loading your AI Personal Assistant DAVID")
wishMe()

if __name__=='__main__':
    
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement :
            speak('your personal assistant Becky is shutting down,Good bye')
            break
        
        if 'wikipedia' in statement:
            speak('Searching wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https:/www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
            
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google mail is open now")
            time.sleep(5)
            
        elif 'weather' in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidty = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidty) +
                      "\n description  " +
                      str(weather_description))
                    print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidty) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Mirthula")
            print("I was built by Mirthula")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/1"])
            
time.sleep(3)
