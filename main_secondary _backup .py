import speech_recognition as sr
import webbrowser
import pyttsx3
import time
#recogniser => class helps to get speech_recognition duncationality
recognition=sr.Recognizer()

#innitalizing pyttsx3
engine=pyttsx3.init()
def process_comand(c):
      pass

def speak(text):
    engine.say(text)
    engine.runAndWait()
   

if __name__=="__main__":
     speak("Initializing Jarvis......")
     while True:
     
        print("recognisizing...............")
        try:
           #listen for the wake word
            with sr.Microphone() as source:
                        print("Listening...")
                        
                        audio = recognition.listen(source,timeout=3,phrase_time_limit=2)
            text = recognition.recognize_google(audio)
            
            print("You said:", text)
            if(text.lower()=="hello"):
                time.sleep(0.5)
                speak("Yes Sir")
                print("yes sir")
                with sr.Microphone() as source:
                            print("Jarvis Active...")
                            
                            audio = recognition.listen(source,timeout=2,phrase_time_limit=1)
                command = recognition.recognize_google(audio)

        except Exception as e:
            print(f"Sorry, could not understand:{e}")
            



