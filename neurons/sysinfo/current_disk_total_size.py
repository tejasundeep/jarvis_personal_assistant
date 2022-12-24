import psutil

diskusage = psutil.disk_usage('/')

disktotalsize = {
  "tag": "disktotalsize",
  "patterns": [
    "Could you please tell me the total disk size",
    "Could you please let me the total disk size",
    "what is the total disk size",
    "how much total disk size",
    "how about the total disk size",
    "How much the disk total size",
    "Can you get the information about my total disk size",
    "I would like to know the total disk size",
    "What is the total storage space"
  ],
  "responses": [
    f"Your toal disk size is {round(diskusage.total / (1024.0 ** 3))}"
  ]
}