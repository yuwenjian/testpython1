from pandas.io.json import json_normalize
import pandas as pd
import time
import requests
import json
from helper import applist_path,del_used_keyword,save_path

def crawler(page):

    baseUrl = "http://api.scs.mob.com/api/app/quick?pageSize=10&type=KA&pageNo="+str(page)
    headers = {
        "token": "0774de0c-83bc-44a3-9ad3-d62044857b99",
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.190 Safari / 537.36"
    }

    params = (
        ('pageNo', page),
        ('pageSize', 10),
        ('type', 'KA')
    )

    response = requests.get(baseUrl, headers=headers, params=params)
    json_data = response.text
    print(json_data)
    d = json.loads(json_data)
    result = []
    for num in range(0, 10):
        if d['data']['list'][num]['dayYoy'] <= -20.00 and d['data']['list'][num]['chain'] <= -10.00 and d['data']['list'][num]['weeklyAvgYoy'] <= -10.00:
            temp = {
                'appName': d['data']['list'][num]['storeName'],
                'appkey': d['data']['list'][num]['appKey']
            }
            result.append(temp)
            print(temp)

    df = json_normalize(result)
    df.to_csv(save_path, mode="a+", header=False, encoding='utf-8', index=False)

if __name__ == '__main__':

    for i in range(1, 24):
        crawler(i)
