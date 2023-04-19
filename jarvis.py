# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
# from jarvis import if_elif_else
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('everydayknowledgebro@gmail.com', 'arsal@1234')
    server.sendmail('everydayknowledgebro@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")


            elif 'open chat GPT' in query:
                webbrowser.open("https://chat.openai.com/")

            elif 'open AI' in query:
                webbrowser.open("openai.com")

            elif 'play music' in query:
                music_dir = 'D:/SONGS'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\ARSAL\\Desktop\\Visual Studio Code.lnk"
                os.startfile(codePath)

            elif 'email to harry' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "harryyourEmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Arvaj bhai. I am not able to send this email")

            elif 'you are fucking rascal' in query:
                speak("Thank you sir, i am not able to do that work")

            elif 'open chrome' in query:
                codePath = "C:\Program Files\Google\Chrome\Application\chrome"
                os.startfile(codePath)

            elif 'thank you jarvis' in query:
                speak("Thank you sir, it's my pleasure that i have done for you something")

            elif 'shutdown' or 'shut down' in query:
                speak("Shutting down , sir")
                os.system('shutdown /s /t 0')

            # elif 'shut down computer' in query:
            #     codePath = "C:\Users\ARSAL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt"
            #     os.startfile(codePath)

            else:
                print("No query matched")