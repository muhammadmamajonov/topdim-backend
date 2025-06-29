from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from  admin import *
from routers import posts, other, users


app = FastAPI()
admin = Admin(app, engine)
admin.add_view(CategoryAdmin)
admin.add_view(SubCategoryAdmin)
admin.add_view(RegionAdmin)
admin.add_view(DistrictAdmin)
admin.add_view(UserAdmin)
admin.add_view(PostAdmin)

app.mount("/media", StaticFiles(directory='./media/'), name="media")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(other.router)
app.include_router(users.router)