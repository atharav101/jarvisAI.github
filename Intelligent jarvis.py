import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import requests
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


# text to audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# to convert user's voice to text


def send_mail(to, subject, body):
    your_email = "athravraj8@gmail.com"
    email_pswd = "12345atharav12345atharav"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("athravraj8@gmail.com", "12345atharav12345atharav")
        server.sendmail("athravraj8@gmail.com", to,
                        f"Subject: {subject}\n\n{body}")
        server.quit()

    except Exception as e:
        print(e)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said :- {query}")

    except Exception as e:
        speak(".")
        return "none"
    return query


def pdf_reader():
    book = open('read.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(book)
    pages = pdf_reader.numPages
    speak(f"total number of pages in this book are {pages}")
    speak("Enter the page number which i had to read")
    pg = int(input("enter page number :- "))
    page = pdf_reader.getPage(pg)
    text = page.extractText()
    print(text)
    speak(text)


def TaskToDone():
    wishMe()
    while True:
        query = takeCommand().lower()

        # for opening notepad

        if "open notepad" in query:
            speak("as you wish ")
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)

        if "open paint" in query:
            path = "C:\\WINDOWS\\system32\\paint.exe"
            os.startfile(path)

        # for closing notpad

        elif "close notepad" in query:
            speak("okey ,,closing notepad")
            os.system("taskkill/f /im notepad.exe")
        # for opening command promot

        elif "open command" in query:
            speak("okey , opening command promot")
            os.system("start cmd")

        # for playing music

        elif "play music" in query:
            speak("okey , playing music")
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        # for knowing your ip address

        elif "read pdf" in query:
            pdf_reader()

        # for searching Wekipedia

        elif "wekipedia" in query:
            speak("Searching WEkipedia.....")
            query = query.replace("wekipedia", "")
            result = wikipedia.summary(query)
            speak("according to wekipedia......")
            speak(result)
            # print(result)

        # for opening you tube

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif "write paragraph" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
            speak("what you  had to type ?")
            paragraph = takeCommand().lower()
            print(paragraph)
            pyautogui.write(paragraph)

        elif "search on youtube" in query or "youtube" in query:
            speak("what to search ?")
            youtube_search = takeCommand().lower()
            webbrowser.open_new_tab(
                f"https://www.youtube.com/results?search_query={youtube_search}")
            speak(f'your result of search {youtube_search} is open on youtube')
            speak("which part to open :- top , middle , lower")
            section = takeCommand().lower()
            if "top" in section:
                speak("as you wish ")
                pyautogui.click(x=995, y=301)
            elif "middle" in section:
                speak("as you wish")
                pyautogui.click(x=996, y=573)
            elif "lower" in section:
                speak("as you wish ")
                pyautogui.click(x=1080, y=933)

        # for opening facebook

        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("www.facebook.com")
        elif "open my first website" in query:
            speak("opening wld website")
            webbrowser.open(
                "https://bpfbtrljbhnm6aunph3krw-on.drv.tw/www.WLD-GUILD.tk/#")
        elif "open my second website" in query:
            speak("opening the website with animation")
            webbrowser.open(
                "https://bpfbtrljbhnm6aunph3krw-on.drv.tw/www.myhappyfamily.com/")

        # FOR Searching on google

        elif "open google" in query or "i have doubt" in query:
            speak("what you want to search")
            doubt = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={doubt}")
            speak("here is the result of your search")

        # play a sepcific song on you tube
        

        
        

            


        elif "run this code" in query:
            speak("okey running the written code")
            # speak("but , let me clear te terminal if running")
            # pyautogui.click(x=1819 , y=607 )
            speak("ruuning this code")
            pyautogui.click(x=1823 , y=53 )


        


        elif "play song on youtube" in query:
            kit.playonyt("o saki saki")

        elif "work on you" in query:
            kit.playonyt(
                "how to make Jarvis in python (part-5) |Jarvis Python ai projects |Python projects | AviUpadhyay")

        elif 'send email' in query:

            speak("Alright to whom? Type the email address")
            to = input("Email address:-   ")
            speak("What's the subject of the mail?")
            subject = takeCommand().lower()
            speak("a.speak the body of the mail?")
            body = takeCommand().lower()
            send_mail(to, subject, body)

        elif "where are we" in query or "where I am" in query:
            speak("let me find out , wait a second please")
            try:
                ipADD = requests.get("https://api.ipify.org").text
                print(ipADD)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipADD+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']

                speak(
                    f"sir i am not sure but we are in the city of {city} of  {country} country !")

            except Exception as e:
                speak("sorry due to some reason i can't get location")
                pass

        elif "activate how to do" in query or "i don't know" in query:
            speak(" please tell me what you want to know")
            how = takeCommand().lower()
            max_result = 1
            how_to = search_wikihow(how, max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "take it easy" in query or "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak("here is a joke for you ")
            print(joke)
            speak(joke)

        elif "who are you" in query or "who had created you " in query:
            speak("i am Jarvis who is created by a 14 year old child name Atharav")

        elif "you never" in query:
            speak("sorry , but you should care while programming me ")

        elif "that is my mistake" in query or "that's my mistake" in query:
            speak("no but ,,,")

        elif "take screenshot" in query or "take a screenshot" in query or "screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("hold the screen for a second, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("the screenshot is saved !")

        elif "how are you" in query:
            speak("i am fine , what about you ?")
            fine = takeCommand().lower()
            if "fine" in fine or "good" in fine:

                speak("thats great to hear")

        elif "open code" in query or "open court" in query:
            path = "C:\\Users\\Atharav raj\\AppData\\Local\\Programs\\Microsoft VS Code.exe"
            speak("opening microsoft visual studio code ")
            os.startfile(path)
        elif "close code" in query or "close court" in query:
            speak("okey ,,closing microsoft Visual Studio code")
            os.system("taskkill/f /im code.exe")

        elif "internet speed" in query:

            speak("cheaking internet speed")
            webbrowser.open("www.fast.com")

        elif "sleep now" in query or "you can sleep" in query or "thank you" in query:
            speak("as you wish i am going to sleep , you can call me anytime ..")
            break

        elif "temperature" in query or "weather" in query:
            search = "temperature in motihari"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "volume up" in query:
            pyautogui.press('volumeup')

        elif "volume down" in query:
            pyautogui.press('volumedown')

        elif "mute volume" in query:
            pyautogui.press('volumemute')

        elif "how much power is left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            persentage = battery.percent
            speak(f"we have {persentage} persent battry left in system ")

        elif "temprature around me" in query:
            hotness = psutil.sensors_temperatures()
            degree = hotness.persent
            speak(f"temprature around us is {degree} degrees")

        elif "window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

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

        elif "close camera" in query:
            pyautogui.press('esc')

        # elif "hide all file" in query or "hide our folder" in query or "visible it" in query or "visible for everyone" in query:
        #     speak("what to do , hide or make it visible for everyone ?")
        #     condition = takeCommand().lower()
        #     if "hide" in condition:
        #         os.system("attrib +h /s /d")
        #         speak("done , all folder are being hiden")
        #     elif "visible" in condition:
        #         os.system("attrib -h /s /d")
        #         speak("okey all folder are being visible !")
        #     elif "leave it" in condition or "leave for now" in query:
        #         speak("as your wish")


# to wish us the time & good moring , afternoon or evening

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(f"Good Morning! ,the time is neraly {hour} am ")

    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon! ,the time is nearly {hour} pm")

    else:
        speak(f"Good evening! ,the time is nearly {hour} pm")

    speak("I am Jarvis ..... tell me how may I help you")

def Type_automatic():
    wishMe()
    while True:
        query = takeCommand().lower()
        if "plate" in query:

            speak("okey , as your wish")
            speak("tell me the name of the code word")
            automatic_code_word = takeCommand().lower()
            pyautogui.write(f'elif "{automatic_code_word}" in query:')
            pyautogui.press('enter')
            speak("tell me the what to write inside speak command")
            speak_command = takeCommand().lower()
            pyautogui.write(f'speak = ("{speak_command}")')
            pyautogui.press('enter')
            speak("tell me which module we are going to use ?")
            module = takeCommand().lower()
            if "os" in module or "system" in module:
                speak("tell me the path of file or write it down ")

                write_down = takeCommand().lower()
                if "path" in write_down:
                    speak("okey tell me  path")
                    path_automatic = takeCommand().lower()
                    pyautogui.write(f"os.startfile({path_automatic})")
                elif "writing down" in write_down:
                    speak("Enter path Bellow")
                    speak("please take care to write double forward slash")
                    path_manuel = input("Enter path Here :- ")
                    speak("okey , i understand  !")
                    time.sleep(3)
                    pyautogui.write("new_path =")
                    pyautogui.press(" ' " )
                    pyautogui.write(path_manuel)
                    pyautogui.press('enter')
                    pyautogui.write("os.startfile(new_path)")




if __name__ == "__main__":
    while True:
        permission = takeCommand().lower()
        if "wake up" in permission or "get started" in permission or "pick up" in permission:

            TaskToDone()
        elif "goodbye" in permission or "shutdown" in permission:
            speak("okey i am leaving ")
            sys.exit()
        elif "type automatic" in permission:
            Type_automatic()

        
