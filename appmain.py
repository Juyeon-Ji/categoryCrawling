"""
use module
import os
"""
import logging
from fastapi import FastAPI
from crawl.categorycrawl import CategoryCrawl  # pylint: disable
from common.database.dbmanager import DatabaseManager
from common.config.configmanager import ConfigManager
from common.log import make_logger

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def main():

    logger = make_logger()

    logger.info('Crawl Test')

    # driver = Selenium().driver

    ConfigManager()
    DatabaseManager()

    # pickle.dumps(DatabaseManager())
    # 카테고리 파싱 주석
    # CategoryCrawl().run()
    CategoryCrawl().parse()

    # ProductCrawl()

    logger.info('Crawl Test End')

    # driver.quit()


if __name__ == '__main__':
    main()
