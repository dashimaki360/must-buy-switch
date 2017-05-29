# -*- coding: utf-8 -*-

import requests
import os

def ifttt_urlreq():
    event_name = os.getenv("IFTTT_EVENT_NAME_YODOBASHI", "hogehoge")
    key = os.getenv("IFTTT_KEY", "foo")
    requests.post("https://maker.ifttt.com/trigger/" + event_name "/with/key/" + key)

