import requests
import json
import time
from functools import wraps
import datetime

# webhookURLを指定
webhook_url = "https://hooks.slack.com/services/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"

"""
# 送信するテキストを定義
text = "PythonでSlackにメッセージを送る"
"""

def set_time():
    start = time.perf_counter()
    return start

def process_time(start):
    end = time.perf_counter() - start
    print(end)

    text = 'Cal time : {}'.format(end) + '\nstart day : {}'.format(str(datetime.datetime.fromtimestamp(start)))

    requests.post(webhook_url, data = json.dumps({
        "text": text
    }))

#デコードとURLのポストも入れる
