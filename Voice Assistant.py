
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pywhatkit
import time
import cv2
import random
import psutil
import pyautogui

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning! I am Jarvis, please tell me how can I help you?")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon! I am Jarvis, please tell me how can I help you?")
    else:
        speak("Good evening! I am Jarvis, please tell me how can I help you?")


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query

if __name__== "__main__":
    wishMe()
    while True:
         query=takeCommand().lower()

         if query=="none":
             continue

         elif any(word in query for word in["stop","exit","quit"]):
             print("Goodbye! Have a nice day")
             speak("Goodbye! Have a nice day!")   
             time.sleep(2)  
             os.exit(0)    
         
         elif "how are you" in query:
          speak("I'm doing great, thank you! What about you?")

         elif "who are you" in query:
          speak("I am Jarvis, your personal assistant, built by you to make life easier.")


         elif "search" in query:
             query=query.replace("search","")
             speak(f"Searching for {query}")
             pywhatkit.search(query)
         
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")

         elif 'open google' in query:
             webbrowser.open("google.com")
        
         elif any(word in query for word in ["time", "current time", "what's the time"]):
          curr_time = datetime.datetime.now().strftime("%I:%M %p")
          print(curr_time)
          speak(f"The time is {curr_time}")
       

         elif any(word in query for word in ["date", "today's date", "what's the date"]):
          today = datetime.date.today().strftime("%B %d, %Y")
          print(today)
          speak(f"Today's date is {today}")
        
         elif "play" in query:
             song=query.replace("play", "")
             speak(f"Playing {song} on YouTube")
             pywhatkit.playonyt(song)

         elif "open code" in query:
           codePath="C:\\Users\\Ansh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)   

         elif "open notepad" in query:
           speak("Opening Notepad")
           os.startfile("C:\\Windows\\System32\\notepad.exe")

         elif "open calculator" in query:
           speak("Opening Calculator")
           os.startfile("C:\\Windows\\System32\\calc.exe")

         elif "shutdown" in query:
           speak("Shutting down your system. Goodbye.")
           os.system("shutdown /s /t 5")

         elif "restart" in query:
           speak("Restarting your system now.")
           os.system("shutdown /r /t 5")

         elif "lock" in query:
           speak("Locking your computer.")
           os.system("rundll32.exe user32.dll,LockWorkStation")

         elif 'wikipedia' in query:
            speak('Searching Wikipedia...')                         
            query=query.replace("wikipedia",'')
            try:
               results=wikipedia.summary(query,sentences=2)
               speak("According to Wikipedia")                          
               print(results)
               speak(results)

            except Exception as e:
                 speak("sorry i could not find any results")

         elif "open chrome" in query:
             speak("Opening Google Chrome")
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

         elif "open downloads" in query:
           speak("Opening your Downloads folder")
           os.startfile("C:\\Users\\Ansh\\Downloads")

         elif "open documents" in query:
           speak("Opening your Documents folder")
           os.startfile("C:\\Users\\Ansh\\Documents")

         elif "battery" in query:
           battery = psutil.sensors_battery()
           percent = battery.percent
           plugged = "charging" if battery.power_plugged else "not charging"
           speak(f"Battery is {percent} percent and {plugged}")

         elif "calculate" in query:
             speak("Please tell me the operation.")
             expression = takeCommand().lower()

    # Replace spoken words with mathematical symbols
             expression = expression.replace("plus", "+")
             expression = expression.replace("minus", "-")
             expression = expression.replace("multiply", "*")
             expression = expression.replace("into", "*")
             expression = expression.replace("divide", "/")
             expression = expression.replace("by", "/")
             expression = expression.replace("x", "*")
             expression = expression.replace("mod", "%")
             expression = expression.replace("remainder", "%")
             expression = expression.replace("power", "**")

             allowed="0123456789+-*/.%()"
             expression=''.join([c for c in expression if c in allowed])

             try:
                  result = eval(expression)
                  speak(f"The result is {result}")
                  print(f"Result: {result}")
             except Exception as e:
                  print(e)
                  speak("Sorry, I couldn't calculate that.")


         elif "open image" in query or "show image" in query or "photo" in query:
           image_folder = "C:\\Users\\Ansh\\OneDrive\\Pictures\\Screenshots"  
           images = [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png", ".jpeg"))]

           if images:
             img_name = random.choice(images)
             img_path = os.path.join(image_folder, img_name)
             speak(f"Opening {img_name}")
             print(f"Opening {img_path}")
        
             img = cv2.imread(img_path)
             cv2.imshow("JARVIS Image Viewer", img)
             cv2.waitKey(0)
             cv2.destroyAllWindows()

           else:
               speak("No images found in your picture folder.")

         elif "screenshot" in query:
            file = "C:\\Users\\Ansh\\OneDrive\\Pictures\\screenshot_by_jarvis.png"
            pyautogui.screenshot(file)
            speak("Screenshot taken and saved.")

            img = cv2.imread(file)
            cv2.imshow("Screenshot by Jarvis", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


         elif "close" in query:
           app = query.replace("close", "").strip()
           speak(f"Closing {app}")
           os.system(f"taskkill /IM {app}.exe /F")

         elif "status" in query or "performance" in query:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            speak(f"CPU usage is {cpu} percent and RAM usage is {ram} percent")

         




     

                  


         



