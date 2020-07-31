#!/usr/bin/python3
import requests
import datetime
 
today = datetime.date.today()
 
def send_attachments():
    return requests.post(
        "https://api.mailgun.net/v3/mg.hjalti.me/messages",
        auth=("api", "My-Private-API-KEY"),
 
        files = [("attachment", ("/home/hjalti/my-logs/"+str(today)+"_rclone_home_sync.log",
                  open("/home/hjalti/my-logs/"+str(today)+"_rclone_home_sync.log", "rb").read()))],
        data = {
            "from": "hjalti@mg.hjalti.me",
            "to":"hjalti@hjalti.me",
            "subject":"Hello Hjalti - Your daily rclone log is here!!",
            "text": "Hey, your daily Rclone log  is here!!"
            })
# Run the function
send_attachments()
