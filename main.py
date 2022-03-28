import datetime
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
listener=sr.Recognizer()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
n=0

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice=listener.listen(source)
            com=listener.recognize_google(voice,language='en-in')
            com=com.lower()
            if 'kitty' in com:
                com=com.replace('kitty','')
                print('user said\n',com)
    except:
        pass
    return com
def run_apple():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        hour=datetime.datetime.now().strftime('%H:%M %p')
        talk('its'+hour+'now')
        print(hour)
    elif ('wikipedia of') in command:
            talk('Searching wikipedia.....')
            data=command.replace('wikipedia of','')
            info=wikipedia.summary(data,1)
            print(info)
            talk(info)
    elif 'are you single' in command:
        talk('no,i am in relationship with wifi')
    elif 'your age' in command:
        talk('I was made at 16 december 2021')
    elif 'how can you help me' in command:
        talk('i can make things easy for you')
        print('i can make things easy for you')
    elif ('tell something about yourself' or 'tell me something about yourself') in command:
        engine.say('I am robot, your virtual assistant\t.I was created by Asra')
        print('I am robot, your virtual assistant\t.I was created by Asra')
        engine.runAndWait()
    elif ('covid' or 'corona') in command:
        talk('ah! it\'s a big headache')
        print('ah! it\'s a big headache')
    elif 'shut up' in command:
        talk('okay    I am there if you need anything')
        print('okay    I am there if you need anything')
        n= 1
    elif 'are you human' in command:
        talk('No,I am a virtual assistant made by Artificial Intelligence')
        print('No,I am a virtual assistant made by Artificial Intelligence')
    elif 'open youtube' in command:
        talk(' here we go.... ')
        print(' here we go.... ')
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        talk('here we go....')
        print('here we go....')
        webbrowser.open("google.com")
    elif 'open whatsapp' in command:
        talk('here we go....')
        print('here we go....')
        webbrowser.open("web.whatsapp.com")
    elif'what' in command:
        talk('here we go....')
        webbrowser.open("google.com")
    else:
        talk('sorry, would you repeat again')
        print('sorry, would you repeat again')

while n==0:
    run_apple()
    engine.runAndWait()

