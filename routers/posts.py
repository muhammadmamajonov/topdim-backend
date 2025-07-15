from typing import Any, List, Optional
from fastapi import APIRouter, Form, UploadFile, Request
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from utils import storage
from database import DB_SESSION
from models import Post, PostPhoto
from schemas import posts as posts_schemas


router = APIRouter(tags=["Posts"], prefix="/posts")


@router.post("/", response_model=posts_schemas.PostDetailSchema)
async def add_post(
    photos: List[UploadFile], db: DB_SESSION, request: Request,
    title: str = Form(), description: str = Form(), user_tg_id: str = Form(),
    phone_number: str = Form(), category_id: int = Form(),
    subcategory_id: Optional[int] = Form(default=None),
    region_id: int = Form(), district_id: int = Form(),):
   
    new_post = Post(
        title=title, description=description, 
        phone_number=phone_number, category_id=category_id, 
        sub_category_id=subcategory_id, region_id=region_id, 
        district_id=district_id, user_tg_id=user_tg_id
    )
    db.add(new_post)
    await db.flush()
    photos_paths = []
    for photo in photos:
        photo_path = storage.save_file("photos", photo)
        photos_paths.append(photo_path)
        photo_object = PostPhoto(path=photo_path, post_id=new_post.id)
        db.add(photo_object)

    await db.commit()
    data = new_post.__dict__
    data["photos"] = [f"{request.base_url}{path}" for path in photos_paths]
    return new_post


@router.get("/", response_model=List[posts_schemas.PostListSchema])
async def get_posts(
    db: DB_SESSION, request: Request,
    category_id: Optional[int]=None, 
    subcategory_id: Optional[int]=None,
    region_id: Optional[int]=None, 
    district_id: Optional[int]=None
):

    stmt = select(Post)

    if category_id is not None:
        stmt = stmt.where(Post.category_id == category_id)
    if subcategory_id is not None:
        stmt = stmt.where(Post.sub_category_id == subcategory_id)
    if region_id is not None:
        stmt = stmt.where(Post.region_id == region_id)
    if district_id is not None:
        stmt = stmt.where(Post.district_id == district_id)

    result = await db.execute(stmt.options(selectinload(Post.photos)).options(selectinload(Post.photos)).options(selectinload(Post.region)).options(selectinload(Post.district)))
    
    data = []
    for post in result.scalars().all():
        photos = post.photos
        d = post.__dict__
        d['photos'] = [f"{request.base_url}{photo.path}" for photo in photos]
        d['region'] = post.region.name
        d['district'] = post.district.name
        data.append(d)
    return data

    
@router.get("/my-posts", response_model=List[posts_schemas.PostListSchema])
async def my_posts(user_tg_id: str, db: DB_SESSION, request: Request):
    posts = await db.execute(select(Post).filter(Post.user_tg_id==user_tg_id).options(selectinload(Post.photos)).options(selectinload(Post.district)).options(selectinload(Post.region)))
    
    data = []
    for post in posts.scalars().all():
        photos = post.photos
        d = post.__dict__
        d['photos'] = [f"{request.base_url}{photo.path}" for photo in photos]
        d['region'] = post.region.name
        d['district'] = post.district.name
        data.append(d)
    return data


@router.get("/{post_id}", response_model=posts_schemas.PostDetailSchema)
async def post_detail(post_id: int, db: DB_SESSION, request: Request):
    post = await db.execute(select(Post).filter(Post.id==post_id).options(selectinload(Post.photos)).options(selectinload(Post.district)).options(selectinload(Post.region)))
    post = post.scalars().first()
    photos = post.photos
    data = post.__dict__
    data['photos'] = [f"{request.base_url}{photo.path}" for photo in photos]
    data['region'] = post.region.name
    data['district'] = post.district.name
    return data