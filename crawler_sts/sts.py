import time
from pathlib import Path
from typing import List

import akshare as ak
from loguru import logger

from pages.utils.date_utils import trade_date,today_is_trade_date
import schedule
# 获取数据+统计数据

class CrawlerSts():
    def __init__(self):
        self.tasks = [
            # 涨停股池
            ak.stock_em_zt_pool,
            ak.stock_em_zt_pool_dtgc,
            ak.stock_em_zt_pool_zbgc,
            ak.stock_em_zt_pool_previous,
            ak.stock_em_zt_pool_strong,
            ak.stock_em_zt_pool_sub_new,
            ak.stock_zh_a_alerts_cls,
            ak.stock_zh_a_spot,
        ]
        self.res = {}

    def crawler(self):
        for task in self.tasks:
            time.sleep(10)
            try:
                task_name = task.__name__
                self.res[task_name] = task()
                self.res[task_name].to_csv(f"./data/{task_name}/{today_str}.csv",encoding="utf-8",index=False)
                logger.info(f"{today_str}_{task_name}运行成功")
            except Exception as e:
                logger.error(e)


    def sts(self):
        ## 区分主板创业板数据

        ## 大盘情绪

        # increase_num = len(df_main[(df_main["涨跌幅"] > 0)])
        # decrease_num = len(df_main[(df_main["涨跌幅"] < 0)])

        ## 投机情绪
        ###  跌停数目
        dt_num = len(self.res["stock_em_zt_pool_dtgc"])

        ### 涨停数据
        stock_em_zt_pool_df = self.res["stock_em_zt_pool"]
        zt_num = len(stock_em_zt_pool_df)

        ### 炸板股票
        stock_em_zt_pool_zbgc = self.res["stock_em_zt_pool_zbgc"]
        zhaban_num = len(stock_em_zt_pool_zbgc)

        ### 代表股票

    def run(self):
        if today_is_trade_date:
            self.crawler()
            self.sts()
    

job = CrawlerSts().run()
schedule.every().day.at("18:00").do(job)