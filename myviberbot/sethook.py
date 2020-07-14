# sethook
import requests
import json

auth_token = "4bd371ba60e7dc6f-bd2b285c3eb35da7-c73e528a718675ea"
hook = "https://chatapi.viber.com/pa/set_webhook"
headers = {"X-Viber-Auth-Token": auth_token}


sen = dict(
    url="https://2a0d5b265b63.ngrok.io/webhook2020",
    event_types=["unsubscribed", "conversation_started", "message", "seen", "delivered"],
)
r = requests.post(hook, json.dumps(sen), headers=headers)
print(r.json())
