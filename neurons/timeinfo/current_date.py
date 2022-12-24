from datetime import datetime as dt # Date and time library

current_year = int(dt.now().year)
current_month = int(dt.now().month)
current_day = int(dt.now().day)
current_date = f"{current_day}/{current_month}/{current_year}"

date = {
  "tag": "date",
  "patterns": [
    "What is the date today",
    "Could you please tell me the date today",
    "Let me know the date today",
    "How about the date today",
    "Get me the date",
    "How about todays date",
    "Date please"
  ],
  "responses": [
    current_date
  ]
}