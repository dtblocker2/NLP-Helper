import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
from googlesearch import search
import pywhatkit as kit
import smtplib
import sys
import time
import pyautogui
import requests
import json
import subprocess
import shutil

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
        r.pause_threshold = 5
        audio = r.listen(source, timeout=100, phrase_time_limit=5)
    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        return query
    except Exception as e:
        speak('say that again please')
        takecommand()

def waiting():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=10000, phrase_time_limit=3)
    try:
        print("recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        if "wake up to reality" in query:
            speak("alright lets get back to work")
            speak("during stand by mode you said following things")
            os.startfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\recorder.txt")
        else:
            with open("C:\\Users\\dhruv\\Desktop\\JARVIS\\recorder.txt", "a") as recorder:
                recorder.write(query)
            waiting()
    except Exception as e:
        waiting()

def wish():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('Good Evening')
    speak("system rebooted, I am Jarvis. Sir, how can I help you?")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.closed()

def alarm(h,m):
    now = datetime.datetime.now()
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour == h and minute == m:
        os.startfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\alarm.mp3")
    else:
        time.sleep(30)
        alarm(h,m)

def wait(h,m):
    now = datetime.datetime.now()
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour == h and minute == m:
        speak("my waiting time has completed, i shall now get back to work")
    else:
        time.sleep(30)
        wait(h,m)

def reminder(h,m,remind):
    now = datetime.datetime.now()
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour == h and minute == m:
        speak(remind)
    else:
        time.sleep(30)
        reminder(h,m)

def news(interest):
    speak("please wait sir, fetching the latest news")
    main_url = "https://newsapi.org/v2/everything?q="+interest+"&from=2024-09-27&sortBy=popularity&apiKey=f4d8de84de91459a91877cba29b4eff7"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
        print("------------------------------------------------")

if __name__ == "__main__":
    wish()
    p = 0
    while True:
        if p>0:
            speak("sir do you have any other work")
        query = takecommand().lower()

        if "open minecraft" in query:
            npath = "C:\\Users\\dhruv\\AppData\\Roaming\\.minecraft\\Tlauncher.exe"
            os.startfile(npath)
        
        elif "open notepad" in query:
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2407.8.0_x64__8wekyb3d8bbwe\\Notepad\\notepad.exe"
            os.startfile(npath)
        
        elif "open browser" in query:
            npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open whatsapp" in query:
            os.startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2435.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
                
        elif "play music" in query:
            music_dir = "C:\\Users\\dhruv\\Music"
            songs = os.listdir(music_dir)
            songs.remove("desktop.ini")
            random_music = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_music))
        
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")
        
        elif "wikipedia" in query:
            speak("searching wikipedia......")
            query = query.replace("wikipeadia","")
            results = wikipedia.summary(query, sentences=5)
            speak("according to wikipedia")
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            query_google = query.replace("open google and", "")
            list_searches = []
            for j in search(query_google, tld="co.in", num=5, stop=5, pause=2):
                list_searches.append(j)
            m = 0
            while True:
                speak(f"searching for {query_google}")
                webbrowser.open(list_searches[m])
                speak("are you satisfied with results?")
                query_google2 = takecommand()
                if m <= 4:
                    if "yes" in query_google2 :
                        speak("glad you like it")
                        break
                    else:
                        m += 1
                if m > 4:
                    speak("i can present only these results")
                    break
        
        elif "incomplete work" in query:
            file_dir = "C:\\Users\\dhruv\\Desktop\\leftover_work"
            files = os.listdir(file_dir)
            txt = "sir you have", len(files), "works to do"
            txt_2 = txt.__str__()
            speak(txt)
            if len(files) <= 5:
                speak("not much work, you can chill")
            if len(files) <= 10 and len(files) > 5:
                speak("sir, i think you should start studying now...")
            if len(files)>10:
                speak("sire pray pardon for my behaviour but you are not studying")
            speak("shall i open the work")
            query_leftwork = takecommand()
            if "open" in query_leftwork:
                for i in files:
                    file_name = os.path.join(file_dir,i)
                    os.startfile(file_name)
                    if i.endswith(".txt"):
                        speak("sir it is reminded that")
                        i2 = i.replace(".txt", "")
                        speak(i2)
            else:
                if len(files) <= 5:
                    speak("ok")
                if len(files) > 5:
                    speak("ok, but you must also consider your academics too")
        
        elif "can you say" in query:
            query_2 = query.replace("can you say", " ")
            speak(query_2)
        
        elif "send message" in query:
            now = datetime.datetime.now()
            ti_h = int(now.strftime("%H"))
            ti_m = int(now.strftime("%M"))
            if "anurag" in query:
                query_w1 = query.replace("send message to anurag","")
                speak("send message titled")
                speak(query_w1)
                speak("to Anurag")
                
                kit.sendwhatmsg("+919817289442", query_w1,ti_h,ti_m+2)
                speak("message has been sent to Anurag")
            elif "ishan" in query:

                query_w1 = query.replace("send message to ishan","")
                speak("send message titled")
                speak(query_w1)
                speak("to Aeshan")
                kit.sendwhatmsg("+918427312742", query_w1,ti_h,ti_m+2)
                speak("message has been sent to Aeshan")
            elif "raghav" in query:
                query_w1 = query.replace("send message to raghav","")
                speak("send message titled")
                speak(query_w1)
                speak("to Raghav")
                kit.sendwhatmsg("+917217505641", query_w1,ti_h,ti_m+2)
                speak("message has been sent to Raghav")
            elif "kaku" or "kanishk" in query:
                query_w1 = query.replace("send message to kaku","")
                speak("send message titled")
                speak(query_w1)
                speak("to Kaku")
                kit.sendwhatmsg("+919413724684", query_w1,ti_h,ti_m+2)
                speak("message has been sent to Kaku")
        
        elif "what is time" in query:
            now = datetime.datetime.now()
            speak("sir the time is")
            speak(now.strftime("%H hours and %M minutes"))
        
        elif "on youtube" in query:
            query_3 = query.replace("play","")
            query_4 = query_3.replace("on youtube","")
            kit.playonyt(query_4)
        
        elif "email to dhruv" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "dk30nov2005@gmail.com"
                sendEmail(to,content)
                speak("email has been sent to dhruv")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send it")
        
        elif "wait for" in query:
            query_2 = query.replace("wait for", "")
            query_3 = query_2.replace("seconds", "")
            query = int(query_3)
            speak(f"waiting for {query_3} seconds")
            time.sleep(query)
        
        elif "shutdown the system" in query:
            speak("shutting down PC in 30 seconds")
            time.sleep(25)
            os.system("shutdown /s /t 5")
        
        elif "restart the system" in query:
            speak("restarting PC in 30 seconds")
            time.sleep(25)
            os.system("shutdown /r /t 5")
        
        elif "sleep mode" in query:
            os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif "no thanks" in query:
            speak("i feel great to serve you my sire, thanks for using me")
            sys.exit()
        
        elif "close notepad" in query:
            speak("okay sir closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        elif "set alarm" in query:
            speak("okay so what hour will it be")
            a = takecommand()
            a2 = int(a)
            speak("and what minute")
            b = takecommand()
            b2 = int(b)
            speak(f"okay so setting alarm for {a2} hours and {b2} minutes")
            speak("while this alarm is set, i am opening a new prompt so that i can continue to help you (this session will be closed after alarm)")
            os.startfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\jarvis.py")
            alarm(a2,b2)
            sys.exit()

        elif "set timer for" in query:
            query_2 = query.replace("set timer for", "")
            if "seconds" in query:
                query_3 = query_2.replace("seconds", "")
                query = int(query_3)
                speak(f"setting timer for {query_3} seconds")
            if "minutes" in query:
                query_3 = query_2.replace("minutes", "")
                query = int(query_3)*60
                speak(f"setting timer for {query_3} minutes")
            def countdown_timer(seconds):
                while seconds:
                    mins, secs = divmod(seconds, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    seconds -= 1
                speak("Time's up!")
            speak("while this reminder is set, i am opening a new prompt so that i can continue to help you (this session will be closed after completion of task)")
            os.startfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\jarvis.py")
            countdown_timer(query)
            time.sleep()
            sys.exit()
        
        elif "test file" in query:
            x=0
            while True:
                x = str(x)
                file_path = "C:\\Users\\dhruv\\Desktop\\JARVIS\\test_" + x +  ".py"
                if not os.path.isfile(file_path):
                    with open(file_path, 'w') as file:
                        file.write("#this is new python file")
                    subprocess.call(["C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", file_path])
                    break
                else:
                    x = int(x)
                    x += 1
            x = str(x)
            speak(f"test_{x} created succesfully")
            time.sleep(5)

        elif "remind me to" in query:
            query2 = query.replace("remind me to","")
            speak("okay so what hour will it be")
            a = takecommand()
            a2 = int(a)
            speak("and what minute")
            b = takecommand()
            b2 = int(b)
            if a2 != None and b2 != None:
                speak(f"okay so reminding you for {query2} at {a} hours and {b} minutes")
                speak("while this reminder is set, i am opening a new prompt so that i can continue to help you (this session will be closed after completion of task)")
                os.startfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\jarvis.py")
                reminder(a2,b2,query2)
                time.sleep(30)
                sys.exit()
            else:
                speak("sorry i was not able to process information let's retry")
            
        elif "wait till" in query:
            #wait till 22 hours and 45 minutes
            query2 = query.split()
            a2 = int(query2[2])
            b2 = int(query2[5])
            speak(f"okay i am at stand by mode till {query2[2]} hours and {query2[5]} minutes")
            wait(a2,b2)
        
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif "tell me news" in query:
            speak("which type of news you want to hear")
            interest = takecommand()
            news(interest)

        elif "standby mode" in query:
            speak("entering standby mode")
            waiting()
        
        elif "open source code" in query:
            speak("opening source code")
            subprocess.call(["C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", "C:\\Users\\dhruv\\Desktop\\JARVIS\\jarvis.py"])
            speak("the modifications done will be applied after restart")
        
        elif "create backup" in query:
            x = 1
            try:
                shutil.copyfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\jarvis.py",f"C:\\Users\\dhruv\\Desktop\\JARVIS\\backup\\{x}.py")
                speak(f"backup file {x} successfully created")
            except FileExistsError:
                x += 1
        
        elif "close" in query:
            query_2 = query.replace("close","")
            query = query_2.lower()
            if "microsoft edge" in query:
                subprocess.call(["taskkill","/F","/IM","msedge.exe"])

        elif "create file" in query:
            speak("what type of file you want to create")
            query_2 = takecommand()
            speak("what do you want to name it")
            query_3 = takecommand()
            file_path = f"C:\\Users\\dhruv\\Desktop\\JARVIS\\"
            if "Word" in query_2:
                file_name = file_path+f"{query_3}.docx"
                with open(file_name, "w") as file:
                    pass
            elif "PowerPoint" in query_2:
                file_name = file_path+f"{query_3}.pptx"
                with open(file_name, "w") as file:
                    pass
            elif "text file" in query_2:
                file_name = file_path+f"{query_3}.txt"
                with open(file_name, "w") as file:
                    pass
            elif "Excel" in query_2:
                file_name = file_path+f"{query_3}.xlsx"
                shutil.copyfile("C:\\Users\\dhruv\\Desktop\\JARVIS\\blank.xlsx",f"C:\\Users\\dhruv\\Desktop\\JARVIS\\{query_3}.xlsx")
            speak("file successfully created")
            os.startfile(file_name)
        
        p += 1