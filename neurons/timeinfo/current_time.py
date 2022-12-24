from datetime import datetime as dt

timenow = dt.now().strftime("%I:%M %p")

time = {
  "tag": "time",
  "patterns": [
    "What is the time now",
    "Could you please tell me the time",
    "Let me know the time",
    "How about the time",
    "Get me the current time",
    "Time please"
  ],
  "responses": [
    "timenow"
  ]
}
