from database import engine
from sqladmin import Admin, ModelView
from models import Category, SubCategory, Region, District, User, Post


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]

class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.id, SubCategory.name, SubCategory.category]

class RegionAdmin(ModelView, model=Region):
    column_list = [Region.id, Region.name]

class DistrictAdmin(ModelView, model=District):
    column_list = [District.id, District.name, District.region]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.first_name, User.last_name, User.phone_number, User.tg_id, User.is_active]
    column_searchable_list = [User.phone_number, User.tg_id]

class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.title, Post.phone_number, Post.category, Post.region]
    column_details_exclude_list = [Post.photos]
    form_excluded_columns = [Post.photos]

