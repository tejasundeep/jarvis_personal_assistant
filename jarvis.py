import random
import json
import torch
from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt  # Date and time library
import webbrowser
import pyautogui
import wikipedia
import os
from pathlib import Path
from playsound import playsound
import pywhatkit as kit
import smtplib
import pyjokes
import clipboard

from brain import NeuralNet
from neural_network import bag_of_words, tokenize
from listner import *
from speaker import *
from neuron_writer import *

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

FILE = "trained_data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Jarvis - Just A Rather Very Intelligent System
bot_name = "Jarvis"

# Greetings
greet_timing = int(dt.now().hour)

if greet_timing >= 0 and greet_timing < 12:
    greet_timing_response = "Good Morning sir"
elif greet_timing >= 12 and greet_timing < 18:
    greet_timing_response = "Good Afternoon sir"
else:
    greet_timing_response = "Good Evening sir"

# Jarvis intros
jarvis_intros = [
    f"{greet_timing_response}, {bot_name} at your service. All systems will be ready in few seconds, mean while grab a cup of coffee and have a good day",
    f"{bot_name} service system activated",
    f"Welcome back sir",
]

print("AI Started! (Say 'quit' to exit)")
speak(random.choice(jarvis_intros))

# Send email
def sendEmail(email_to, email_content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("tsreddykarri94@gmail.com", "SHreyansh2019/*")
    server.sendmail("tsreddykarri94@gmail.com", email_to, email_content)
    server.close()


# Wakeup jarvis
while True:
    # Listen wakeup word
    wakeword = listen()
    if bot_name.lower() in wakeword:
        speak("Yes sir how can i assit you?")

        while True:
            sentence = listen()
            if sentence == "quit":
                break

            tokenized_sentence = tokenize(sentence)
            X = bag_of_words(tokenized_sentence, all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(device)

            output = model(X)
            _, predicted = torch.max(output, dim=1)

            tag = tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]

            if prob.item() > 0.75:
                for neuron in neurons["neurons"]:
                    if tag == neuron["tag"]:
                        reply = str(random.choice(neuron["responses"]))
                        words_serv = [
                            "ok sir",
                            "yes sir",
                            "on your words",
                            "on it sir",
                            f"{bot_name} always at your service",
                            "sure sir",
                        ]

                        # Implement Manual Tasks
                        # Distance
                        if "distance" in reply:
                            distance_url = "https://www.google.com/search?q=" + sentence
                            distance_page = requests.get(distance_url)
                            distance_data = BeautifulSoup(
                                distance_page.content, "html.parser"
                            )
                            distance = distance_data.find(
                                "div", class_="BNeawe deIvCb AP7Wnd"
                            ).text
                            speak(distance)
                        # Time
                        elif "timenow" in reply:
                            speak(dt.now().strftime("%I:%M %p"))
                        # Volume up
                        elif "volumeup" in reply:
                            speak(
                                f"{random.choice(words_serv)} The volume has been increased"
                            )
                            pyautogui.press("volumeup")
                        # Volume down
                        elif "volumedown" in reply:
                            speak(
                                f"{random.choice(words_serv)} The volume has been decreased"
                            )
                            pyautogui.press("volumedown")

                        # Volume mute
                        elif "volumemute" in reply:
                            pyautogui.press("volumemute")
                        # Screenshot
                        elif "screenshot" in reply:
                            pyautogui.hotkey("win", "printscreen")
                            speak("Screenshot has been saved successfully")
                        # Cut
                        elif "cut" in reply:
                            pyautogui.hotkey("ctrl", "x")
                            speak("You have successfull cut")
                        # Copy
                        elif "copy" in reply:
                            pyautogui.hotkey("ctrl", "c")
                            speak("You have successfull copied")
                        # Paste
                        elif "paste" in reply:
                            pyautogui.hotkey("ctrl", "v")
                            speak("You have successfull pasted")
                        # Delete
                        elif "delete" in reply:
                            pyautogui.press("delete")
                            speak("You have successfull deleted")
                        # Pageup
                        elif "pageup" in reply:
                            pyautogui.press("pageup")
                        # Pagedown
                        elif "pagedown" in reply:
                            pyautogui.press("pagedown")
                        # Open folder
                        elif "openfolder" in reply:
                            folder_name = sentence.replace("open folder ", "")
                            open_folder = str(Path.home() / folder_name)
                            folder_path = os.path.realpath(open_folder)
                            speak(f"Opening the folder {folder_path}")
                            os.startfile(folder_path)
                        # Open website
                        elif "website" in reply:
                            sentence = sentence.replace("open the website ", "")
                            sentence = sentence.replace("open the url ", "")
                            sentence = sentence.replace("go to url ", "")
                            sentence = sentence.replace("go to website ", "")
                            speak(
                                f"{random.choice(words_serv)} Opening the website {sentence}"
                            )
                            webbrowser.open(f"{sentence}")
                        # Search google
                        elif "google" in reply:
                            sentence = sentence.replace("search google for ", "")
                            sentence = sentence.replace("search on google for ", "")
                            speak(
                                f"{random.choice(words_serv)} Searching your query {sentence} on google.com"
                            )
                            webbrowser.open(
                                f"https://www.google.com/search?q={sentence}"
                            )
                        # Search youtube
                        elif "youtube" in reply:
                            sentence = sentence.replace("search youtube for ", "")
                            sentence = sentence.replace("search on youtube for ", "")
                            speak(
                                f"{random.choice(words_serv)} Searching your query {sentence} on youtube.com"
                            )
                            kit.playonyt(f"{sentence}")
                        # Wikipedia
                        elif "wikipedia" in reply:
                            speak("{random.choice(words_serv)} Searching wikipedia...")
                            sentence = sentence.replace("search on wikipedia for", "")
                            sentence = sentence.replace("search wikipedia for ", "")
                            sentence = sentence.replace("search wikipedia for ", "")
                            result = wikipedia.summary(sentence, sentences=2)
                            speak(f"According to wikipedia {result}")
                        # Open antivirus
                        elif "programwindowsantivirus" in reply:
                            speak(f"{random.choice(words_serv)} Opening antivirus")
                            os.system("start windowsdefender:")
                        # Open windows networks
                        elif "programwindowsnetworks" in reply:
                            speak(f"{random.choice(words_serv)} Showing wifi networks")
                            os.system("start ms-availablenetworks:")
                        # Open browser
                        elif "programwindowsbrowser" in reply:
                            speak(f"{random.choice(words_serv)} Opening browser")
                            os.system("start msedge")
                        # Open calculator
                        elif "programwindowscalculator" in reply:
                            speak(f"{random.choice(words_serv)} Opening calculator")
                            os.system("start calc")
                        # Open camera
                        elif "programwindowscamera" in reply:
                            speak(f"{random.choice(words_serv)} Opening camera")
                            os.system("start microsoft.windows.camera:")
                        # Open clock
                        elif "programwindowsclock" in reply:
                            speak(
                                f"{random.choice(words_serv)} Opening alarams and clocks"
                            )
                            os.system("start ms-clock:")
                        # Open terminal
                        elif "programwindowscmd" in reply:
                            speak(f"{random.choice(words_serv)} Opening command prompt")
                            os.system("start cmd")
                        # Open control panel
                        elif "programwindowscontrolpanel" in reply:
                            speak(f"{random.choice(words_serv)} Opening control panel")
                            os.system("start control panel")
                        # Open notepad
                        elif "programwindowsnotepad" in reply:
                            speak(f"{random.choice(words_serv)} Opening notepad")
                            os.system("start notepad")
                        # Open paint
                        elif "programwindowspaint" in reply:
                            speak(f"{random.choice(words_serv)} Opening paint")
                            os.system("start mspaint")
                        # Open photos
                        elif "programwindowsphotos" in reply:
                            speak(f"{random.choice(words_serv)} Opening gallery")
                            os.system("start ms-photos:")
                        # Open windows player
                        elif "programwindowsplayer" in reply:
                            speak(f"{random.choice(words_serv)} Opening media player")
                            os.system("start mswindowsmusic:")
                        # Open windows settings
                        elif "programwindowssettings" in reply:
                            speak(
                                f"{random.choice(words_serv)} Opening windows settings"
                            )
                            os.system("start ms-settings:")
                        # Open task manager
                        elif "programwindowstaskmanager" in reply:
                            speak(f"{random.choice(words_serv)} Opening task manager")
                            os.system("start taskmgr")
                        # Open mail
                        elif "programwindowsmail" in reply:
                            speak(f"{random.choice(words_serv)} Opening windows mail")
                            os.system("start outlookmail:")
                        # Open notifications
                        elif "programwindowsnotifications" in reply:
                            speak(
                                f"{random.choice(words_serv)} Opening windows notifications"
                            )
                            os.system("start ms-actioncenter:")
                        # Shutdown pc
                        elif "shutdownpc" in reply:
                            os.system("shutdown /s /t 1")
                        # Restart pc
                        elif "restartpc" in reply:
                            os.system("shutdown /r /t 1")
                        # Logout pc
                        elif "logoutpc" in reply:
                            os.system("shutdown -l")
                        # Play music
                        elif "playmusic" in reply:
                            music_dir = "music"
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir, random.choice(songs)))
                        # Stop music
                        elif "stopmusic" in reply:
                            os.system("taskkill /f /im vlc.exe")
                        # Send email
                        elif "sendemail" in reply:
                            speak("What should i send sir ?")
                            email_content = listen().lower()
                            speak("Whom to send the email?")
                            email_to = listen().lower()
                            sendEmail(email_to, email_content)
                            speak("Email successfully sent")
                        # Tell Jokes
                        elif "jokes" in reply:
                            speak(pyjokes.get_joke())
                        # Remember data
                        elif "remember" in reply:
                            speak("What should i remember?")
                            remember_data = listen().lower()
                            speak("you told me to remember that " + str(remember_data))
                            remember = open("remembered_data.txt", "w")
                            remember.write(remember_data)
                            remember.close()
                        # Remember data
                        elif "recalldata" in reply:
                            remembered_data = open("remembered_data.txt", "r")
                            speak(
                                "You told me to remeber that " + remembered_data.read()
                            )
                        # Read the text
                        elif "readtext" in reply:
                            text = clipboard.paste()
                            speak(text)
                        # Tell jarvi to wait
                        elif "waitjarvis" in reply:
                            playsound("sounds/mm-hmm.wav")
                        else:
                            speak(reply)
