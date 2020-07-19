# sethook
import requests
import json

auth_token = "token"
hook = "https://chatapi.viber.com/pa/set_webhook"
headers = {"X-Viber-Auth-Token": auth_token}


sen = dict(
    url="https://custome_url_or_ngrok/webhook2020",
    event_types=["unsubscribed", "conversation_started", "message", "seen", "delivered"],
)
r = requests.post(hook, json.dumps(sen), headers=headers)
print(r.json())
