from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=weather"
page = requests.get(url)
data = BeautifulSoup(page.content, "html.parser")
current_weather = data.find("div", class_ = "BNeawe tAd8D AP7Wnd").text

weather = {
  "tag": "weather",
  "patterns": [
    "What is the weather",
    "Could you please tell me the weather",
    "Let me know the weather",
    "How about the weather",
    "Get me the current weather",
    "Weather please?"
  ],
  "responses": [
    current_weather
  ]
}