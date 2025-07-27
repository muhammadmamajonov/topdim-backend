from typing import List, Optional
from pydantic import BaseModel


class AddPostSchema(BaseModel):
    title: str
    description: str
    phone_number: str
    category_id: int
    sub_category_id: Optional[int] = None
    region_id: int
    district_id: int


class PostListSchema(BaseModel):
    id: int
    title: str
    phone_number: str
    region: str
    district: str
    photos: List[str]

class PostDetailSchema(PostListSchema):
    description: str


class PhotoSchema(BaseModel):
    id: int
    url: str

class PostDetailForUpdateSchema(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    phone_number: Optional[str] = None
    category_id: Optional[int] = None
    sub_category_id: Optional[int] = None
    region_id: Optional[int] = None
    district_id: Optional[int] = None
    photos: List[PhotoSchema] = []
