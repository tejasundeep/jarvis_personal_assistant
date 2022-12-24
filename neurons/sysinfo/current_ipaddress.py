import requests

ip = requests.get('http://api.ipify.org').text

ipaddress = {
  "tag": "ipadress",
  "patterns": [
    "Could you please tell me my ip address",
    "what is my ip address",
    "how about my ip address",
    "Can you get the information about my ip address",
    "I would like to know my ip address"
  ],
  "responses": [
    f"Your IP Adress is: {ip}"
  ]
}
print(ip)