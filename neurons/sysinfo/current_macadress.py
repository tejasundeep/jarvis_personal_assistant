import re, uuid

current_macaddress = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

macaddress = {
  "tag": "macaddress",
  "patterns": [
    "Could you please tell me my mac address",
    "what is my mac address",
    "how about my mac address",
    "Can you get the information about my mac address",
    "I would like to know my mac address"
  ],
  "responses": [
    f"Your Mac Adress is: {current_macaddress}"
  ]
}