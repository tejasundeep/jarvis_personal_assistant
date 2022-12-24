from datetime import datetime as dt # Date and time library

current_weekday = dt.now().strftime('%A')

weekday = {
  "tag": "weekday",
  "patterns": [
    "What is the weekday",
    "Could you please tell me the weekday",
    "Let me know the weekday",
    "How about the weekday",
    "Get me the current weekday"
    "Week day",
    "Weekday please"
  ],
  "responses": [
    current_weekday
  ]
}
