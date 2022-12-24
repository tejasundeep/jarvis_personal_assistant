from types import NoneType
import speech_recognition as sr # Speech recognition

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.dynamic_energy_threshold = True
        recognizer.adjust_for_ambient_noise(source)
        input_audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(input_audio, language = "en-IN")
        query = query.lower()
        print(query)
        return query

    except Exception as error:
        print(error)
        return "None"