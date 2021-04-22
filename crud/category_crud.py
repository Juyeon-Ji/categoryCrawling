from typing import List, Optional
from common.database.dbmanager import DatabaseManager
from models.category import CategoryBase
from common.consts import CATEGORY


async def get_categories(db: DatabaseManager) -> List[CategoryBase]:
    categories: List[CategoryBase] = []
    rows = db.find(CATEGORY, {})

    if rows:
        for row in rows:
            categories.append(CategoryBase(**row))

    return categories
