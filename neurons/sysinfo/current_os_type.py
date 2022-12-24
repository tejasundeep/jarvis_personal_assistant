import platform

os_type = {
  "tag": "ostype",
  "patterns": [
    "Could you please tell me the os type",
    "what is the os type",
    "how about os type",
    "Can you get the information about os type",
    "I would like to know about the os type",
    "Can you tell me the os type",
    "What type of operating system?"
  ],
  "responses": [
    f"Your os type is: {platform.machine()}"
  ]
}