import psutil

diskusage = psutil.disk_usage('/')
diskused = round(diskusage.used / (1024.0 ** 3))
disktotalsize = round(diskusage.total / (1024.0 ** 3))
diskfree = round(diskusage.free / (1024.0 ** 3))

diskinfo = {
  "tag": "diskinfo",
  "patterns": [
    "Please tell me my disk information",
    "Please tell me my disk info",
    "Please tell me my disk info"
    "What is the disk information",
    "Do you know the disk information",
    "What is the disk info",
    "What is the disk details",
    "Do you know the disk info"
    "How much information do you have about the hard disk"
    "I would like to know info about my hard disk"    
    "Tell me information about my storage space"
  ],
  "responses": [
    f"{str(diskused)} GB used of total {str(disktotalsize)} GB, free space left is {str(diskfree)} GB"
  ]
}