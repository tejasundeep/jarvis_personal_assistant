import platform

operating_system = {
  "tag": "operatingsystem",
  "patterns": [
    "Could you please tell me my os",
    "Could you please tell me my operating system",
    "what is my os",
    "What is my operating system",
    "how about my os",
    "how about my operating system",
    "Can you get the information about my os",
    "Can you get the information about my operating system",
    "I would like to know about my os",
    "I would like to know about my operating system",
    "Can you tell me my os",
    "Can you tell me my operating system"
  ],
  "responses": [
    f"Your are using {platform.system()}  {platform.release()} operating system"
  ]
}