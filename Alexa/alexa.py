import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text) :
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try :
        with sr.Microphone() as source:
            print("Say something!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

    except :
        pass
    return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me a about' in command:
        look_for = command.replace('tell me a about', '')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'date' in command:
        talk('Sorry Bro, I am in a relation with Jarvis')
    else:
        talk('I did not get it but I am going to  search it for you')
        pywhatkit.search(command)

run_alexa()
