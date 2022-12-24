import psutil

cpu_used = {
  "tag": "cpuused",
  "patterns": [
    "How much cpu used",
    "How much CPU was used?",
    "Could you please tell me my cpu usage",
    "What is the cpu usage",
    "Let me know the usage of cpu",
    "Central Processing Unit Used",
    "Do you know my cpu usage",
    "can you give me the information about my cpu usage"
    "I would like to know info about my cpu usage"
  ],
  "responses": [
    f"You have used {str(psutil.cpu_percent(5)*10)} percent of total cpu"
  ]
}