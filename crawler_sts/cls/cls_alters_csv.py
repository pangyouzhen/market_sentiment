import json
from datetime import datetime
from typing import Optional
from unittest import main

import pandas as pd
import requests

from crawler_sts.cls.cls import cls_headers,cls_url,cls_payload
from pages.utils.date_utils import DateUtils

class ClsAlterCsv():
    def __init__(self):
        pass 
        
    def get_data(self):
        payload = json.dumps(
            {
                "type": "telegram",
                "keyword": "快讯",
                "page": 0,
                "rn": 30,
                "os": "web",
                "sv": "7.2.2",
                "app": "CailianpressWeb",
            }
        )
        trade_date,today_is_trade_date = DateUtils().trade_date()
        today = datetime.today()
        today_start = today.replace(hour=0, minute=0, second=0, microsecond=0)
        response = requests.request("POST", cls_url, headers=cls_headers, data=payload)
        res = response.json()
        data = res["data"]["telegram"]["data"]
        df = pd.DataFrame(data)
        df = df[["descr", "id", "time"]]
        df["descr"] = df["descr"].astype(str).str.replace("</em>", "")
        df["descr"] = df["descr"].str.replace("<em>", "")
        df["time"] = df["time"].apply(datetime.fromtimestamp)
        df = df[df["time"] > today_start]
        df.columns = ["快讯信息", "id", "时间"]
        df.to_csv(f"./data/stock_zh_a_alerts_cls/{trade_date}.csv", encoding="utf-8")
        
if __name__ == "__main__":
    cls_alter_csv = ClsAlterCsv()
    cls_alter_csv.get_data()