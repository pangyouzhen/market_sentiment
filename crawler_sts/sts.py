import time
from pathlib import Path
from typing import List

import akshare as ak
from loguru import logger

from pages.utils.date_utils import DateUtils
import schedule
# 获取数据+统计数据
from crawler_sts.cls.cls_alters_csv import ClsAltersCsv
from crawler_sts.cls.cls_zt_img import ClsZtImg

trade_date,today_is_trade_date = DateUtils().trade_date()
logger.add(f"logs/{trade_date}.log", rotation="1 day")

class CrawlerSts():
    def __init__(self):
        self.tasks = [
            # 涨停股池
            ak.stock_zt_pool_em,
            # 跌停股池
            ak.stock_zt_pool_dtgc_em,
            # 炸板股池
            ak.stock_zt_pool_zbgc_em,
            # 昨日涨停
            ak.stock_zt_pool_previous_em,
            ak.stock_zt_pool_strong_em,
            ak.stock_zt_pool_sub_new_em,
            # ak.stock_zh_a_alerts_cls,
            ClsAltersCsv().get_data,
            # 全部数据
            ak.stock_zh_a_spot,
            # 赚钱效应
            ak.stock_market_activity_legu,
        ]
        self.res = {}

    def crawler(self):
        for task in self.tasks:
            time.sleep(10)
            try:
                task_name = task.__name__
                self.res[task_name] = task()
                self.res[task_name].to_csv(f"./data/{task_name}/{trade_date}.csv",encoding="utf-8",index=False)
                logger.info(f"{trade_date}_{task_name}运行成功")
            except Exception as e:
                logger.error(e)


    def sts(self):
        ## 区分主板创业板数据

        ## 大盘情绪

        # increase_num = len(df_main[(df_main["涨跌幅"] > 0)])
        # decrease_num = len(df_main[(df_main["涨跌幅"] < 0)])

        ## 投机情绪
        ###  跌停数目
        dt_num = len(self.res["stock_zt_pool_dtgc_em"])

        ### 涨停数据
        stock_em_zt_pool_df = self.res["stock_zt_pool_em"]
        zt_num = len(stock_em_zt_pool_df)

        ### 炸板股票
        stock_em_zt_pool_zbgc = self.res["stock_zt_pool_zbgc_em"]
        zhaban_num = len(stock_em_zt_pool_zbgc)

        ### 代表股票

    def run(self):
        if today_is_trade_date:
            logger.info("开始爬取数据")
            self.crawler()
            logger.info("开始统计数据")
            self.sts()
            logger.info("统计数据结束")
        else:
            logger.info("今天不是交易日")
    

job = CrawlerSts().run
schedule.every().day.at("20:14").do(job)

while True:
    print("start")
    schedule.run_pending()
    time.sleep(10)
