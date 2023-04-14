import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import datetime
import os
import subprocess as sp
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[1].id)

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

paths = {
    'notepad': "C:\\Program Files\\Notepad\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_calculator():
    sp.Popen(paths['calculator'])

def open_notepad():
    sp.Popen(paths['notepad'])

def open_cmd():
    os.system('start cmd')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=4 and hour< 12:
        speak("Good Morning sir")
    elif hour>= 12 and hour< 18:
        speak("Good Afternoon sir")
    elif hour>= 18 and hour< 20:
        speak("Good Evening sir")    
    else:
    
        speak("Good Night sir")
        
    speak(f"I am Sophie. How may I assist you ?")
  
if __name__ == "__main__":
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.1
            audio = r.listen(source)
        
        try: 
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in') 
            print(f"You said: {query}\n")
            query=query.lower()
        
            if 'stop now' in query or 'stop it' in query:
                speak("Okay sir")
                break
        
            elif 'tell me something about' in query:
                speak("Okay sir, I'm working on it.")
                speak("Showing results.........")
                query = query.replace("tell me something about", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'what is the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"The time is {strTime}")
            
            elif 'open youtube' in query:
                speak("Opening youtube")
                webbrowser.open('https://www.youtube.com/') 
               
            elif 'open google' in query:
                speak("cool, opening google")
                webbrowser.open('https://www.google.com/')
            
            elif 'open chat' in query:
                speak("opening ChatGPT")
                webbrowser.open('https://chat.openai.com/chat')  

            elif 'lock windows' in query or "lock my pc" in query or "lock the device" in query:
                speak("locking the device master")
                ctypes.windll.user32.LockWorkStation()  

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                sp.call("shutdown / h")

            elif "restart" in query or "restart the device" in query:
                speak("Your device will be restarting within a minute!")
                sp.call(["shutdown", "/r"])
            
            elif 'open Matlab' in query:
                speak("Opening matlab")
                codePath = "C:\\Program Files\\MATLAB\\R2022b\\bin\\matlab.exe"   
                os.startfile(codePath) 

            elif 'search' in query or 'play' in query:
             
                query = query.replace("search", "")
        
                query = query.replace("play", "")         
                webbrowser.open(webbrowser.open("https://www.google.com/search?q=" + query + ""))
        
            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
                speak("Background changed successfully")
           
            elif "what's your name" in query or "What is your name" in query:
                speak("My sir call me")
                speak("Sophie")
                print("My master call me Sophie")

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Sanyam.")

            elif 'open aio' in query:
                speak("Opening A I O")
                codePath = "C:\demo\AIO.py"
                os.startfile(codePath)

            elif 'make a folder with name' in query or 'create a folder with name' in query:
        
                query = query.replace("make a folder with name", "")
                query = query.replace("create a folder with name", "")
                speak("creating a folder named" + query + "")
                os.mkdir(query)
                speak("folder created")

            elif "write a note" in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('master.txt', 'w')
                speak("master, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
         
            elif "show notes" in query:
                speak("Showing Notes")
                file = open("master.txt", "r")
                print(file.read())
                t=file.read()
                speak(t)
        
            elif 'open camera' in query:
                speak("Cool, opening camera.")
                open_camera()

            elif 'open calculator' in query:
                speak("Cool, I'm opening calculator.")
                open_calculator() 

            elif "who i am" in query:
                speak("If you talk then definitely your human.")
 
            elif "why you came to world" in query:
                speak("Thanks to my master. further It's a secret")

            elif 'open cmd' in query:
                speak("opening command center.")
                open_cmd()
        
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("locating" + query)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            elif 'open my linkedin profile' in query:
                speak("cool,Opening your linkedin profile")
                webbrowser.open('https://www.linkedin.com/in/sanyam-gupta-7b7624258/')

            elif 'open my github profile' in query:
                speak("Just a second sir.")
                speak("Opening github")
                webbrowser.open('https://github.com/mehisanyam/codeit')

        
            elif 'speak what i write' in query:
                speak("Okay, go on")
                while True:
                    inp=input("SAY: ")
                    speak(inp)
                    if (inp=="stop now"):
                        speak("Okay sir")
                        break

            else:
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()
        
        except Exception as e:
            print("Sorry, I could not understand. Could you please say that again?")  
            engine.runAndWait()
            
        