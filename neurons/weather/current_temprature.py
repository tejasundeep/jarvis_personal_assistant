from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=temperature"
page = requests.get(url)
data = BeautifulSoup(page.content, "html.parser")
current_temperature = data.find(class_ = "BNeawe iBp4i AP7Wnd").text
current_temperature = current_temperature.replace("°C", "")
current_temperature = current_temperature + "degrees celsius"

temperature = {
  "tag": "temperature",
  "patterns": [
    "What is the temprature",
    "Could you please tell me the temprature",
    "Let me know the temprature",
    "How about the temprature",
    "Get me the current temprature",
    "Temperature please?"
  ],
  "responses": [
    current_temperature
  ]
}