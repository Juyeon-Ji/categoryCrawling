import logging
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from fastapi import APIRouter, Depends, HTTPException
from common.database.dbmanager import db, DatabaseManager
from common.consts import CATEGORY
from models.category import CategoryBase
from crud.category_crud import get_categories
from crawl.categorycrawl import CategoryCrawl


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}}
)


@router.get(
    "/",
    response_model=List[CategoryBase]
)
async def get_category_items():
    categories = await get_categories(db)
    return categories


@router.get(
    "/{cid}",
    response_model=CategoryBase
)
async def get_category_by_id(cid: str):
    _query = db.find_query('cid', cid)
    row = db.find_one(CATEGORY, _query)

    if row:
        return CategoryBase(**row)

