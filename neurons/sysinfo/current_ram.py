import psutil

ram = {
  "tag": "ram",
  "patterns": [
    "How much ram do i have?",
    "Tell me my ram info",
    "My ram details",
    "Get my ram info?"
  ],
  "responses": [
    f"You have {str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB ram in your machine sir"
  ]
}