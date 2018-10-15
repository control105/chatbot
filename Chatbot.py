import random
import time
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

greetings = ['hey there','hello','hi','hey!','hey']
question = ['how far','how you dey','howdy','how are you','how are you doing']
responses = ['I dey']
var1 = ['who made you', 'who created you']
var2 = ['I was created by Control right in his computer.','Control','Some random guy I no know']
var3 = ['what time is it','what is the time','time',"what's the time"]
var4 = ['who are you', "what's your name",'who you be','who goes there']
cmd1 = ['open browser','open google']
cmd2 = ['play music','play songs', 'play a song','open music player']
cmd3 = ['crack joke give me','tell me a joke','say something funny']
jokes = ['Our politicians go to US when they need to work,Dubai to buy something,Paris to rest,europe if they want to study. The only come back to Nigeria when they want to die!, So is it a cemetery?',"A man comes home late at night. Husband shouts behind a locked door: ”Let me in!” Wife: “Go back to where you`ve come from”. Husband:” Let me in, or I`ll kill myself!” Wife: “I do not care!” Husband goes to a lake and throws a stone into the lake. Wife goes out from a house wearing nothing but bra and pants. She tries to “save” her husband in the lake! Husband sneakily returns to the house and locks the door. Wife returns to the house and finds out that the door is closed. Wife: “Let me in!” Husband:” Tell me, Darling, where have you come from wearing nothing but pants and bra?”"]
cmd4 = ['open youtube','i want to watch a video']
cmd5 = ['tell me the weather','weather']
cmd6 = ['exit','close','goodbye','nothing']
cmd7 = ['what is your colour','your colour']
colrep = ["Right now it's rainbow",'Right now its transparent','right now, its nude']
cmd8 = ['what is your favorite colour']
cmd9 = ['thank you']
refr9 = ["you're welcome",'glad i could help you']

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something: ")
        audio = r.listen(source)
        #time.sleep(10)
        try:
            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("I don't understand what you're saying")
            engine.say('I no hear you. Rerun the code')
            engine.runAndWait()

    if r.recognize_google(audio) in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
    elif r.recognize_google(audio) in question:
        random_response = random.choice(responses)
        engine.say(random_response)
        engine.runAndWait()
        print(random_response)
    elif r.recognize_google(audio) in var1:
        reply = random.choice(var2)
        engine.say(reply)
        engine.runAndWait()
        print(reply)
    elif r.recognize_google(audio) in cmd9:
        engine.say(random.choice(repfr9))
        engine.runAndWait()
        print(random.choice(repfr9))
    elif r.recognize_google(audio) in cmd7:
        reply1 = random.choice(colrep)
        print(reply1)
        engine.say(reply1)
        engine.runAndWait()
        print('It keeps changing in a flash')
        engine.say('It keeps changing in a flash')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
        webbrowser.open('www,google.com')
    elif r.recognize_google(audio) in cmd3:
        jokerep = random.choice(jokes)
        engine.say(jokerep)
        engine.runAndWait()
    elif r.recognize_google(audio) in var3:
        print("Current date and time: ")
        print(now.strftime('The time is %H:%M'))
        engine.say(now.strftime('The time is %H:%M'))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd5:
        owm = pyowm.OWM('9230792fc63cdd18574db076549d3139')
        observation = owm.weather_at_place('Uyo', 'NG')
        observation_list = owm.weather_around_coords(5.0322, 7.9248)
        w = observation.get_weather()
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')
        print(w)
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        engine.say('wind')
        engine.runAndWait()
        engine.say(w.get_wind())
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(w.get_humidity())
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(w.get_temperature('celsius'))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd2:
        mixer.init()
        mixer.music.load("D:\Music\Tha Carter V\08 Mona Lisa (feat. Kendrick Lamar).m4a")
        mixer.music.play()
    elif r.recognize_google(audio) in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()
    else:
        engine.say('please wait')
        engine.runAndWait()
        print(wikipedia.summary(r.recognize_google(audio)))
        engine.say(wikipedia.summary(r.recognize_google(audio)))
        engine.runAndWait()
        userInput00 = input('Or else search in google: ')
        webbrowser.open_new('www.google.com/search?q=' + userInput00)
