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

    
class GetPostSchema(AddPostSchema):
    id: int
    photos: List[str]

class PostListSchema(BaseModel):
    id: int
    title: str
    phone_number: str
    region: str
    district: str
    photos: List[str]