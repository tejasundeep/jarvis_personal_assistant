import psutil

diskusage = psutil.disk_usage('/')

diskused = {
  "tag": "diskused",
  "patterns": [
    "Could you please tell me the total disk used",
    "Could you please let me the total disk used",
    "what is the total disk used",
    "how much total disk used",
    "how about the total disk used",
    "How much the disk total used",
    "Can you get the information about my total disk used",
    "I would like to know the total disk used"
    "What is the storage space used"
  ],
  "responses": [
    f"You used {round(diskusage.used / (1024.0 ** 3))} GB"
  ]
}