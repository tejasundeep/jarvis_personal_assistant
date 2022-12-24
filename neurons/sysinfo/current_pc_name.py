import socket

pcname = {
  "tag": "pcname",
  "patterns": [
    "What is my pc name",
    "Tell me my pc name",
    "What is my computer name",
    "Tell me my computer name",
    "What is my system name",
    "Tell me my system name",
    "How about my system name",
    "Get me the system name",
    "Let me know my system name"
  ],
  "responses": [
    f"Your PC name is: {socket.gethostname()}"
  ]
}