from datetime import datetime as dt # Date and time library

current_month = int(dt.now().month)

month = {
  "tag": "month",
  "patterns": [
    "What is the month",
    "Could you please tell me the month",
    "Let me know the month",
    "How about the month",
    "Get me the current month",
    "Month please"
  ],
  "responses": [
    current_month
  ]
}
