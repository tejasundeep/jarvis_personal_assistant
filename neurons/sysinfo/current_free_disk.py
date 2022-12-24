import psutil

diskusage = psutil.disk_usage('/')

freedisk = {
  "tag": "freedisk",
  "patterns": [
    "Could you please tell me the free disk size",
    "Could you please let me the free disk size",
    "what is the free disk size",
    "how much free disk size",
    "how about the free disk size",
    "How much the disk free size",
    "Can you get the information about my free disk size",
    "I would like to know the free disk size",
    "Can you tell me free disk left",
    "What is the storage space left"
  ],
  "responses": [
    f"You have {round(diskusage.free / (1024.0 ** 3))} GB of storage space left"
  ]
}