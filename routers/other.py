from typing import Any, List, Optional
from fastapi import APIRouter, Form, UploadFile, Request
from sqlalchemy import select

from database import DB_SESSION
from models import posts as posts_models
from schemas import other



router = APIRouter(tags=["Other"], prefix="/other")


@router.get("/categories", response_model=List[other.IDNameSchema])
async def categories_list(db: DB_SESSION):
    categories = await db.execute(select(posts_models.Category))
    return categories.scalars().all()

@router.get("/subcategories", response_model=List[other.IDNameSchema])
async def subcategories_list(category_id: int, db: DB_SESSION):
    subcategories = await db.execute(select(posts_models.SubCategory).filter(posts_models.SubCategory.category_id==category_id))
    return subcategories.scalars().all()

@router.get("/regions", response_model=List[other.IDNameSchema])
async def regions_list(db: DB_SESSION):
    regions = await db.execute(select(posts_models.Region))
    return regions.scalars().all()

@router.get("/districts", response_model=List[other.IDNameSchema])
async def districts_list(region_id: int, db: DB_SESSION):
    districts = await db.execute(select(posts_models.District).filter(posts_models.District.region_id==region_id))
    return districts.scalars().all()