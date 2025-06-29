from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, Text, DateTime, ForeignKey


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    districts = relationship("District", back_populates="region")
    posts = relationship("Post", back_populates="region")

    def __str__(self):
        return self.name

class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    region_id = Column(Integer, ForeignKey("regions.id"))
    region = relationship("Region", back_populates='districts')
    posts = relationship("Post", back_populates='district')

    def __str__(self):
        return self.name

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    posts = relationship("Post", back_populates="category")
    sub_categories = relationship("SubCategory", back_populates="category")

    def __str__(self):
        return self.name

class SubCategory(Base):
    __tablename__ = "sub_categories"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="sub_categories")
    posts = relationship("Post", back_populates="sub_category")

    def __str__(self):
        return self.name

    
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(100))
    description = Column(Text)
    is_top = Column(Boolean, server_default="f")
    phone_number = Column(String(17))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    sub_category_id = Column(Integer, ForeignKey("sub_categories.id"))
    region_id = Column(Integer, ForeignKey('regions.id'))
    district_id = Column(Integer, ForeignKey('districts.id'))
    user_tg_id = Column(String)

    category = relationship("Category", back_populates="posts")
    sub_category = relationship("SubCategory", back_populates="posts")
    region = relationship("Region", back_populates="posts")
    district = relationship("District", back_populates="posts")
    photos = relationship("PostPhoto", back_populates="post")

    def __str__(self):
        return self.title

class PostPhoto(Base):
    __tablename__ = "post_photos"

    id = Column(Integer, primary_key=True, unique=True)
    path = Column(String)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="photos")

