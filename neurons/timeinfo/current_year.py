from datetime import datetime as dt # Date and time library

current_year = int(dt.now().year)

year = {
  "tag": "year",
  "patterns": [
    "What is the year",
    "Could you please tell me the year",
    "Let me know the year",
    "How about the year",
    "Get me the current year",
    "Year please"
  ],
  "responses": [
    current_year
  ]
}
