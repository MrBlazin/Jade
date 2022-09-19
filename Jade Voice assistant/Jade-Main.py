import random
import pyautogui
import subprocess
import wolframalpha
import pyttsx3
from pathlib import Path
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import ctypes
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

jadelocalresponse = "CUSTOMIZE THIS.txt"
file = open(jadelocalresponse, 'r')
delimeter = '='


def findValue(fullstring):
    fullstring = fullstring.rstrip('\n')
    value = fullstring[fullstring.index(delimeter)+1:]
    return value
for line in file:
    if line.startswith('sirmaamtitle'):
        sirmaamtitle = findValue(line)
    if line.startswith('username'):
        username = findValue(line)
    if line.startswith('descriptionofyourself'):
        descriptionofyourself = findValue(line)

def yw():
    data_folder = Path("Jade-local/Jade-responses/")
    file_to_open = data_folder / "yw.txt"
    f = open(file_to_open)
    tyyw = f.readlines()
    length = len(tyyw)
    r1 = random.randint(0,length-1)
    speak(tyyw[r1] + sirmaamtitle)
    print(tyyw[r1] + sirmaamtitle) 


def Hmsg():
    data_folder = Path("Jade-local/Jade-responses/")
    file_to_open = data_folder / "hmsg.txt"
    f = open(file_to_open)
    helpmsg = f.readlines()
    length = len(helpmsg)
    r1 = random.randint(0,length-1)
    speak(helpmsg[r1] + sirmaamtitle)
    print(helpmsg[r1] + sirmaamtitle)

def Jokerrr():
    data_folder = Path("Jade-local/Jade-jokes/")
    file_to_open = data_folder / "jokes.txt"
    f = open(file_to_open)
    jokerrr = f.readlines()
    length = len(jokerrr)
    r1 = random.randint(0,length-1)
    speak(jokerrr[r1])
    print(jokerrr[r1])

def Wb():
    data_folder = Path("Jade-local/Jade-responses/")
    file_to_open = data_folder / "wb.txt"
    f = open(file_to_open)
    wbmsg = f.readlines()
    length = len(wbmsg)
    r1 = random.randint(0,length-1)
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak(username + wbmsg[r1] + "Good Morning!")
        print(username + wbmsg[r1] + "Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak(username + wbmsg[r1] + "Good Afternoon!")
        print(username + wbmsg[r1] + "Good Afternoon!")
  
    else:
        speak(username + wbmsg[r1] + "Good Evening!")
        print(username + wbmsg[r1] + "Good Evening!")

def weather():
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/weather_icon.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        pyautogui.click()

def spotifyopen():
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_logo.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        pyautogui.click()

def spotifypause():
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_logo.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_gui_pause.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        pyautogui.click()
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_logo.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)

def spotifyplay():
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_logo.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_gui_play.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        pyautogui.click()
        res = pyautogui.locateCenterOnScreen("Jade-local/Jade-pyautogui-pics/spotify_logo.png", confidence = 0.9)
        print(res)
        pyautogui.moveTo(res)


def cord():
        os.chdir("Jade-local/Jade-tools/")
        os.startfile("mousecord.py") 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print(f"Good Morning! {sirmaamtitle}.")
        speak(f"Good Morning! {sirmaamtitle}.")
  
    elif hour>= 12 and hour<18:
        print(f"Good Afternoon! {sirmaamtitle}.") 
        speak(f"Good Afternoon! {sirmaamtitle}.")  
  
    else:
        print(f"Good Evening! {sirmaamtitle}.") 
        speak(f"Good Evening! {sirmaamtitle}.") 
        Hmsg()


def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)      
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"{username} said: {query}\n")
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return ""
    return query
  

if __name__ == '__main__':
    clear = lambda: os.system('cls')
 
    clear()
    Wb()
    Hmsg()

    while True:
         
        query = takeCommand().lower()

              #Wikipedia
        if 'search for' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search for", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)  


              #Wolfram|alpha
        elif "what" in query or "how" in query or "who is" in query or "where" in query:
            client = wolframalpha.Client("T4RK2G-QVP6874EAL")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results, Try using the phrase 'search for <object>'.")

        elif "calculate" in query:
             
            app_id = "T4RK2G-QVP6874EAL"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "the time" in query or "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir, the time is {strTime}")

    # Misc


        elif 'open youtube' in query:
            speak(f"Here you go {sirmaamtitle}")
            webbrowser.open("https://www.youtube.com")
            Hmsg()

        elif 'open spotify' in query or 'open music' in query:
            spotifyopen()
 
        elif 'play spotify' in query or 'play music' in query:
            spotifyplay()

        elif 'pause spotify' in query or 'pause music' in query:
            spotifypause()

        elif 'mouse' in query:
            cord()
 
    # Questions

 
        elif 'goodbye jade' in query:
            speak(f"Terminating Session, Goodbye {sirmaamtitle}.")
            exit()
 
        elif 'who made you' in query or 'who created you' in query:
            print("I have been created by Mr Blazin, you can find me on github at https://github.com/MrBlazin.")
            speak("I have been created by Mr Blazin, you can find me on github at this link.")

        elif 'thank' in query or 'thanks' in query:
            yw()
            Hmsg()

        elif 'who am i' in query:
            print("You are:" + username + descriptionofyourself)
            speak("You are:" + username + descriptionofyourself)

        elif 'jade echo' in query:
            query = query.replace("jade echo", "")        
            speak(query)
 
        elif 'who are you' in query:
            speak("Im Jade, Your personal voice assistant created by Mr Blazin.")
 
        elif 'what is love' in query:
            print("Baby, don't hurt me Don't hurt me no more")
            speak("Baby, don't hurt me Don't hurt me no more")
              
        elif 'how are you' in query:
            print("I'm fine, How about you?")
            speak("I'm fine, How about you?")
            Hmsg()
 
        elif 'i love you' in query:
            print("How could you love a inanimate object?")
            speak("How could you love a inanimate object?")

        elif 'joke' in query:
            Jokerrr()
            
    # System Commands
             
 
        elif 'log off' in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.winshell.LockWorkStation()

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'hey jade' in query or 'jade' in query:
            time.sleep(1)
            wishMe()
        # Work in progress...
        #
        elif 'weather' in query:
            time.sleep(1)
            weather()
        #
        #elif 'jade' and 'news' in query:
            #News WIP
        #
        #elif 'im feeling lucky' in query:
            
       
              
 
                
        # elif "" in query:
            # Command go here
            # For adding more commands
            