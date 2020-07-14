import json

import requests
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

auth_token = "4bd371ba60e7dc6f-bd2b285c3eb35da7-c73e528a718675ea"
hook = "https://chatapi.viber.com/pa/set_webhook"
headers = {"X-Viber-Auth-Token": auth_token}
url = "https://chatapi.viber.com/pa/send_message"


def sending(func):
    def wrapped(*args):
        return requests.post(url, json.dumps(func(*args)), headers=headers)

    return wrapped


@sending
def send_text(agent, text, track=None):
    print(agent)
    m = dict(receiver=agent, min_api_version=2, tracking_data=track, type="text", text=text)
    return m


@csrf_exempt
def trx_bot(request):
    if request.method == "POST":
        viber = json.loads(request.body.decode("utf-8"))
        if viber["event"] in ["webhook", "message"]:
            if viber["event"] == "message":
                conversation(viber)
            return HttpResponse(status=200)
        # else:
        #     return HttpResponse(status=500)
    return HttpResponse(status=200)


def conversation(viber):
    id = viber["sender"]["id"]
    send_text(id, viber["message"]["text"])
