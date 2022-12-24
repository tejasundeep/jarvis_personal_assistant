from datetime import datetime as dt # Date and time library

current_day = int(dt.now().day)

day = {
  "tag": "day",
  "patterns": [
    "What is the day",
    "Could you please tell me the day",
    "Let me know the day",
    "How about the day",
    "Get me the current day",
    "Day please"
  ],
  "responses": [
    current_day
  ]
}