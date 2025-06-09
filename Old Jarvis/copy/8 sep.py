import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak('say that again please')
        return "none"
    return query

def wish():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('Good Evening')
    speak("system rebooted, I am Jarvis. Sir, how can I help you?")

if __name__ == "__main__":
    wish()
    a = 1
    while True:
        if a == 0:
            start = input("to wake me up enter: anything")
            a = 1


        if a == 1:
            query = takecommand().lower()

        if "open minecraft" in query:
            npath = "C:\\Users\\dhruv\\AppData\\Roaming\\.minecraft\\Tlauncher.exe"
            os.startfile(npath)
        
        if "open notepad" in query:
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2407.8.0_x64__8wekyb3d8bbwe\\Notepad\\notepad.exe"
            os.startfile(npath)

        if "open browser" in query:
            npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(npath)
        
        if "open command prompt" in query:
            os.system("start cmd")
        
        if "open whatsapp" in query:
            os.startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2435.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")

        if "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.inshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
                cap.release()
                cv2.destroyAllWindows()
        
        if "play music" in query:
            music_dir = "C:\\Users\\dhruv\\Music"
            songs = os.listdir(music_dir)
            songs.remove("desktop.ini")
            random_music = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_music))
        
        if "set system to sleep" in query:
            speak("system is set to sleep mode")
            a = 0