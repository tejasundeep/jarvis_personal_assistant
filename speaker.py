import pyttsx3

engine = pyttsx3.init() # Call the initial function of the pyttsx3 library
engine.setProperty("rate", 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(content):
    engine.say(content)
    engine.runAndWait()