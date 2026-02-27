from fastapi import FastAPI
from app.database import Base, engine
from app.routers import admin_module, admin_module_item, admin_apartment, admin_auth, public, admin_design_image, moodboard
from app.models import user, apartment, module, module_item, design_image



app = FastAPI()
app.include_router(admin_apartment.router)
app.include_router(admin_design_image.router)
app.include_router(admin_auth.router)
app.include_router(admin_module.router)
app.include_router(admin_module_item.router)
app.include_router(public.router)
app.include_router(moodboard.router)
# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "MakeOver Backend Running"}
