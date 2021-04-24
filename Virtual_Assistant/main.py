import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', ' ')
                print(command)
                talk(command)


    except:
        pass
    return command



def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        talk('Playing ' + song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("It is " + time + "O'clock")
    elif 'wikipedia' in command:
        wiki = command.replace('wikipedia', '')
        info = wikipedia.summary(wiki, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say the command again. ")

while True:
    run_alexa()


