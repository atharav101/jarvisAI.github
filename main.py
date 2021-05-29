import pyttsx3 , speech_recognition as sr , pyautogui ,time , os , webbrowser , requests , psutil , smtplib , random , wikipedia , pywikihow , sys , pyjokes , datetime
from bs4 import BeautifulSoup 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


# text to audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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


def send_mail(to, subject, body):
    your_email = "your_email"
    email_pswd = "your_password"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("your_email", "password")
        server.sendmail("email_id", to,
                        f"Subject: {subject}\n\n{body}")
        server.quit()

    except Exception as e:
        print(e)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)

    if hour >= 0 and hour < 12:
        speak(f"Good Morning! ,the time is  {hour}hour and {minute} minutes am")

    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon! ,the time is  {hour}hour and {minute} minutes pm")

    else:
        speak(f"Good evening! ,the time is  {hour}hour and {minute} minutes pm")

    speak("I am Jarvis . tell me how may I help you")


def task_execute():
    wishMe()
    while True:
        query = takeCommand().lower()

        # to open any program

        if "open the"  in query:
            replaced = query.replace("open the" , "")
            speak(f'opening {replaced} ')
            pyautogui.hotkey('win','s')
            time.sleep(1.5)
            pyautogui.write(replaced , interval= 0.01)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            speak(f'opened {replaced} ') 

        # to close any current running program

        elif "exit" in query:
            replaced = query.replace("exit" , "")
            os.system(f"taskkill/f /im {replaced}.exe")
            speak(f'closed {replaced}')


        #  to search on the google   
        
        elif "search on google that " in query:
            replaced = query.replace("search on google that " , "")
            url = f"https://www.google.com/search?q={replaced}"
            speak(f'your result of search {replaced} is now opened on google.com')
            webbrowser.open_new_tab(url)

        # to search anything on youtube

        elif "search on youtube that " in query:
            replaced = query.replace("search on youtube that " , "")
            url = f"https://www.youtube.com/search?q={replaced}"
            speak(f'your result of search {replaced} is now opened on youtube')
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
            webbrowser.open_new_tab(url)

        #work on chrome , shortcut and lots of many things 
        
        elif "close current tab" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','w')
            speak('done')
        
        elif "open new window" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','n')
            speak('done')
        elif "go back" in query:
            speak("okey")
            pyautogui.click(x=23 ,y=57)
        
        elif "open new tab" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','t')
            speak('done')
        
        elif "move to next open tab" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','tab')
            speak('done')
        
        elif "previous open tab" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','w')
            speak('done')
        
        elif "close current window" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','w')
            speak('done')
        
        elif "minimize current window" in query:
            speak('okey ')
            pyautogui.hotkey('alt','space' , 'n')
            speak('done')
        elif "maximize current window" in query:
            speak('okey ')
            pyautogui.hotkey('alt','space' , 'x')
            speak('done')
        
        elif "close current tab" in query:
            speak('okey ')
            pyautogui.hotkey('Ctrl','w')
            speak('done')
        
        elif "open home page" in query:
            speak('okey ')
            pyautogui.hotkey('alt','home')
            speak('done')

        # to find the current location

        elif "my location" in query or "where we are" in query or "where i am " in query:
            speak("let me find out , wait a second please")
            try:
                ipADD = requests.get("https://api.ipify.org").text
                print(ipADD)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipADD+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']

                speak( f" i am not sure but we are in the city of {city} of  {country} country !")

            except Exception as e:
                speak("sorry due to some reason i can't get location")
                pass


        # to take screenshot
            
        elif "take screenshot" in query or "take a screenshot" in query or "screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("hold the screen for a second, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("the screenshot is saved !")
        
         # to find temperature around you 

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

        # to cheak how uch battry power is left

        elif "how much power is left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            persentage = battery.percent
            speak(f"we have {persentage} persent battry left in system ")

        # sending email to anyone that you wish

        elif 'send email' in query:

            speak("Alright to whom? Type the email address")
            to = input("Email address:-   ")
            speak("What's the subject of the mail?")
            subject = takeCommand().lower()
            speak("speak the body of the mail?")
            body = takeCommand().lower()
            send_mail(to, subject, body)

        # to play music

        elif "play music" in query:
            speak("okey , playing music")
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        # to search for wikipedia

        elif 'wikipedia' in query :
            speak('Searching Wikipedia...')
            speak("please give a second")
            replaced = query.replace("wikipedia", "")
            webbrowser.open_new_tab(f'https://en.wikipedia.org/wiki/{replaced}')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak(f'thats what i found for your result of {results}')

        elif "who are you" in query:
            speak("i am Jarvis , who is an bot! .. i am created by a child ")

        elif "switch the window" in query:
            speak("okey ")
            pyautogui.hotkey('alt' , 'tab')
        # to break jarvis 
        elif 'thank you' in query :
            speak("it's my work to help you , goodbye!")
            sys.exit()

        elif "sleep now" in query or "you can sleep" in query:
            speak("as you wish i am going to sleep , you can call me anytime ..")
            break

        # to tell a joke 

        elif "take it easy" in query or "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak("here is a joke for you ")
            print(joke)
            speak(joke)

        elif  "turn off" in query or "rest" in query:
            speak("good bye !")
            sys.exit()
        elif "what's the time" in query:
            current_time = int(datetime.datetime.now().hour)
            current_minute = int(datetime.datetime.now().minute)
            speak(f'the current time is {current_time} hour and {current_minute} minute')
            print(f'the current time is {current_time} hour and {current_minute} minute')


        else:
            random_int = random.randint(1,4)
            if random_int == 1:
                found_error = "didn't recongine that command"
                print(found_error)
            elif random_int == 2:
                found_error = "I can't understand this command , please try again"
                print(found_error)
            elif random_int == 3:
                found_error = "i didn't do this , sorry !"
                print(found_error)
            elif random_int == 4:
                found_error = "didn't caught , what do you say !"
                print(found_error)
            

if __name__ == '__main__':
    while True:
        permmsion = takeCommand().lower()
        if "wake up" in permmsion or "turn on" in permmsion:
            task_execute()
        else:
            print("didn't recongine that command")
    



       

        
        
        


            




    

#``