import pyttsx3
import datetime
import os
import  speech_recognition
engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
#print(voice[1].id)
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hey Good Morning Ashish, I am jarvis how can help you")
    elif hour >= 12 and hour < 18:
        speak("Hey Good Afternoon Ashish, I am jarvis how can help you")
    else:
        speak("Hey Good Evening  Ashish, I am jarvis how can help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please speak again")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:
        command = takeCommand().lower()
        if 'open google' in command:
            webbrowser.open('google.com')
        elif 'open youtube' in command:
            webbrowser.open('youtube.com')
        elif 'play music' in command:
            musicPath = "C:\\Users\\1022784\\Desktop\\music"
            songs = os.listdir(musicPath)
            os.startfile(os.path.join(musicPath,songs[0]))
        elif 'quit' in command:
            exit()