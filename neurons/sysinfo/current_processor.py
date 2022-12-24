import platform

processor = {
  "tag": "processor",
  "patterns": [
    "What is my pc processor",
    "Tell me my pc processor",
    "What is my computer processor",
    "Tell me my computer processor",
    "What is my system processor",
    "Tell me my system processor",
    "How about my system processor",
    "Get me the system processor",
    "Let me know my system processor"
  ],
  "responses": [
    f"Your are using {platform.processor()} processor"
  ]
}