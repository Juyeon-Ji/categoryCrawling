"""
use module
import os
"""
import logging
import uvicorn
from uuid import uuid4
from fastapi import FastAPI, Depends
from crawl.categorycrawl import CategoryCrawl, crawl  # pylint: disable
from common.database.dbmanager import DatabaseManager, db
from common.config.configmanager import ConfigManager
from common.log import make_logger
from routers import category
import asyncio

logger = make_logger('uvicorn')

app = FastAPI()
app.include_router(category.router)

context = {'jobs': {}}


@app.get("/")
async def root():
    return {"message": "Hello World111"}


@app.get(
    "/start"
)
async def start():
    identifier = str(uuid4())
    logging.info("start")
    context['jobs'][identifier] = {}

    asyncio.run_coroutine_threadsafe(crawl.parse(identifier, context), loop=asyncio.get_running_loop())

    return {"identifier": identifier}


@app.get(
    "/status/{identifier}"
)
async def get_crawl_status(identifier: str):
    return {"status": context['jobs'].get(identifier, 'job with that identifier is undefined')}


if __name__ == '__main__':
    uvicorn.run("appmain:app", host="0.0.0.0", port=8000, reload=True)
