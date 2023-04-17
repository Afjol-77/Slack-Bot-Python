import requests
import sys
import json

message_text=input()

def send_slack_message(message):
    payload = {"text":message} #key must be 'text'
    payload = json.dumps(payload)
    response = requests.post(
        'Incoming Webhook URL',
        data = payload
    )
    print(response.text)

def times(message_text):
    for i in range(0,5):
        send_slack_message(message_text)


if len(message_text)>0:
    times(message_text)    
else:
    print("Please type a message")

