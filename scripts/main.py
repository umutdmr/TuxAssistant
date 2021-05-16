import speech_recognition as sr
from time import ctime
import wikipedia
import playsound as ps
from gtts import gTTS
import os
import random as rn


def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("How can I help you?")
        audio = recognizer.listen(source)
        voice_data = ""
        try:
            voice_data = recognizer.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            speak("Sorry, I cannot understand")
        except sr.RequestError:
            speak("There is a voice problem")

        return  voice_data


def respond(voice_data):
    if "what is your name" in voice_data or "what's your name" in voice_data:
        speak("My name is Tux.")
    elif "goodbye" in voice_data or "enough" in voice_data:
         speak("Goodbye")
         exit()
    elif "how are you" in voice_data:
        speak("Thanks! You?")
    elif "what time is it" in voice_data or "time" in voice_data:
        time = ctime().split(' ')[3].split(':')[0:2]
        current_time = f"{time[0]}:{time[1]}"
        speak("The time is " + current_time)
    elif "date" in voice_data or "what is the day today" in voice_data:
        date = ctime().split(' ')[0:3]
        date.append(ctime().split(' ')[-1])
        speak("Today is " + date[1] + " " + date[2] + " " + date[-1] + " " + date[0])
    elif "what is" in voice_data or "who is" in voice_data:
        thing = voice_data.split()[2:]
        try:
            speak("Hold on for a second...")
            sub = wikipedia.search(thing)[1]
            speak(wikipedia.summary(sub))
        except:
            speak("Couldn't find anything")
    else:
        speak("Nothing to find")


def speak(audio_string):
    text_to_speech = gTTS(text=audio_string, lang="en")
    num = rn.randint(10, 100)
    audio_file = "audio-" + str(num) + ".mp3"
    text_to_speech.save(audio_file)
    print(audio_string)
    ps.playsound(audio_file)
    os.remove(audio_file)




while True:
    voice_data = record_audio()
    respond(voice_data)
