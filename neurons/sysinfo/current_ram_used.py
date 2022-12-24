import psutil

ram_used = {
  "tag": "ramused",
  "patterns": [
    "What is my ram usage",
    "Tell me my ram usage",
    "What is my ram used",
    "Tell me my ram used",
    "How about my ram used",
    "Get me the ram used",
    "Let me know my ram used"
  ],
  "responses": [
    f"You have used {str(psutil.virtual_memory()[2])} percent of total ram"
  ]
}