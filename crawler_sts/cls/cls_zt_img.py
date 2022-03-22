import json
import re
import time
from typing import Optional

import requests
from bs4 import BeautifulSoup
from crawler_sts.cls.cls import cls_headers, cls_payload, cls_url
from loguru import logger
from pages.utils.date_utils import DateUtils


class ClsZtImg():

    def __init__(self):
        pass

    def get_data(self):
        schema_id = self.get_schema_id()
        html = self.request_detail(schema_id)

    def get_schema_id(self) -> Optional[str]:     
        input_date,today_is_trade_date = DateUtils().trade_date()
        self.date = input_date
        year, month, day = input_date.split("-")
        self.today_cn = "%s月%s日" % (int(month), int(day))
        schema_payload = cls_payload % (self.today_cn + "涨停分析")
        logger.info(schema_payload)
        response = requests.request("POST", cls_url, headers=cls_headers, data=schema_payload.encode("utf-8"))
        js = json.loads(response.text)
        data = js["data"]["telegram"]["data"]
        if len(data) > 0:
            schema = (data[0]["schema"])
            img_time_stamp = (data[0]["time"])
            schema_id = re.search("\d+", schema).group(0)
            if schema_id:
                if self.time_compare(img_time_stamp):
                    return schema_id
                else:
                    logger.warning("获取的时间戳过期")
            else:
                logger.warning("schema_id is None")
        else:
            logger.warning("获取data为空")

    def request_detail(self, schema_id):
        url = "http://www.cls.cn/detail/%s" % schema_id
        response = requests.request("GET", url, headers=cls_headers)
        page = response.text
        pagesoup = BeautifulSoup(page, 'lxml')
        links = [link for link in pagesoup.find_all(name='img', attrs={"src": re.compile(r'^https://img')})]
        if len(links) == 1:
            src_link = links[0].get("src")
            url = src_link.split("?")[0]
            html = requests.get(url)
            return html
        else:
            logger.info("获取的数据为空")

    def save(self, html):
        with open(f'./data/cls_img/{self.date}.png', 'wb') as file:
            file.write(html.content)
        logger.info("保存文件完成")

    def time_compare(self, img_time_stamp: float):
        timestamp: float = time.mktime(self.date.timetuple())
        if img_time_stamp > timestamp:
            return True
        else:
            return False

if __name__ == "__main__":
    cls_zt_img = ClsZtImg()
    cls_zt_img.get_data()