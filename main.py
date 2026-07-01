from datetime import datetime

import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound
import tempfile
import os
import time

recognizer = sr.Recognizer()
# site dictionary
from sites import sites
# music dictionary
from musiclibrary import music
# api key
from api_key import weather_api_key

import requests

def get_weather(city):
    api_key = weather_api_key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    print(f"Temperature is {temp} degree Celsius")
    speak(f"Today's weather in {city}: {desc}. Temperature is {temp} degree Celsius")

def processCommand(c):
        # Sites
    if c.lower().startswith("open"):
        for name, link in sites.items():
            if( f"open {name}" in c.lower()):
                webbrowser.open(link)
                speak(f"Opening {name}")
                return
      # Music
    elif c.lower().startswith("play"):
        for song, link in music.items():
            if f"play {song}" in c.lower():
                webbrowser.open(link)
                speak(f"Playing {song}")
                return
     # today's update
    elif c.lower().startswith("today's"):
        if "weather" in c.lower():
            city = "Delhi"  # Default city
            get_weather(city)
            return
        if "date" in c.lower():
            today = datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {today}")
            return
    #calculator
    elif c.lower().startswith("calculate"):
            expr = c.lower().replace("calculate", "").strip()
            expr = expr.replace("plus", "+")
            expr = expr.replace("minus", "-")
            expr = expr.replace("into", "*")
            expr = expr.replace("multiply by", "*")
            expr = expr.replace("divided by", "/")
            result = eval(expr)
            speak(f"The answer is {result}")
            return
    #time
    elif c.lower().startswith("what time is it"):
            now = datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")
            return

# def ask_yes_no(prompt):
#     speak(prompt)
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.5)
#         audio = r.listen(source, timeout=5, phrase_time_limit=5)
#     try:
#         answer = r.recognize_google(audio)
#         print("Confirmation heard:", answer)
#         return answer.lower().strip() == "yes"
#     except Exception as e:
#         #if you will not say any thing it will stop

#         print(f"Sorry, could not understand confirmation: {e}")
#         return False


def speak(text):
    print(f"[Friday] {text}")
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
        tmp_path = tmp.name
    tts.save(tmp_path)
    try:
        playsound(tmp_path)
    except Exception as e:
        print(f"[speak] playback error: {e}")
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
    time.sleep(0.2)


if __name__ == "__main__":
    print("Initializing Friday....")
    speak("Initializing ")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            # speak("say Friday")
            with sr.Microphone() as source:
                #to reduce ambiant noise
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print("Heard:", word)
            if "friday" in word.lower():
                speak("Yes sir, I am listening")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("Friday Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio)
                print("Command:", command)
                processCommand(command)
                # if ask_yes_no("Do you want me to continue?Do you want me do anything else for you sir? Say yes to continue."):
                #     speak("Continuing")
                #     continue
                # else:
                #     speak("Stopping now")
                #     break
            else:
                print("Wake word not detected.")
        except sr.WaitTimeoutError:
            print("Microphone timed out waiting for phrase; retrying...")
        except Exception as e:
            print(f"Sorry, could not understand: {e}")