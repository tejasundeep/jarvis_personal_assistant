from bs4 import BeautifulSoup
import requests

search_url = "https://www.google.com/search?q=" + "how+to+start+beauty+parlour"
search_page = requests.get(search_url)
search_data = BeautifulSoup(search_page.content, "html.parser")
search_google = search_data.find("div", class_ = "egMi0 kCrYT").a['href']
search_google = search_google[:search_google.rfind('sa=')]
search_google = search_google.replace("/url?q=", "")
search_google = search_google.replace("&", "")

google_result_page = requests.get(search_google)
google_result_search_data = BeautifulSoup(google_result_page.content, "html.parser")
print(google_result_search_data)