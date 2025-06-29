from sqlalchemy import select
from typing import Any, List, Optional
from fastapi import APIRouter, Form, UploadFile, Request

import schemas
from models import *
from database import DB_SESSION

router = APIRouter(tags=["User"], prefix="/user")

@router.get("/profile", response_model=schemas.ProfileSchemas)
async def get_profile(tg_id: int, db: DB_SESSION):
    profile = await db.execute(select(User).where(User.tg_id==tg_id))
    return profile.scalars().first()