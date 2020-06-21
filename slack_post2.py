import requests
import json
import time
from functools import wraps
import datetime

# webhookURLを指定
webhook_url = "XXXX"

def set_time():
    start = time.perf_counter()
    return start

def process_time(start):
    end = time.perf_counter() - start
    print(end)

    text = 'プログラム全体の計算時間 : {}\n開始日時 :{}'.format(end,str(datetime.datetime.fromtimestamp(start)))

    requests.post(webhook_url, data = json.dumps({
        "text": text
    }))

# 関数ごとの時間を計算（関数の前に設置）
def fanc_time(func):
    @wraps(func) # fanc_time()の中に外部関数を取り込む
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args,**kargs) # 外部の関数が設定
        #print(result) # リターン確認
        elapsed_time =  time.time() - start
        text = '関数{}の計算実行時間は{}です'.format(func.__name__,elapsed_time)
        requests.post(webhook_url, data = json.dumps({
            "text": text
        }))
        return result
    return wrapper # ローカル関数を返す
