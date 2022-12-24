from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=temperature"
page = requests.get(url)
data = BeautifulSoup(page.content, "html.parser")
current_location = data.find(class_ = "BNeawe tAd8D AP7Wnd").text

location = {
  "tag": "location",
  "patterns": [
    "What is the location",
    "Could you please tell me the location",
    "Let me know the location",
    "How about the location",
    "Get me the current location",
    "Location please?"
  ],
  "responses": [
    current_location
  ]
}