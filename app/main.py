from fastapi import FastAPI
from app.database import Base, engine
from app.routers import admin_auth
from app.routers import admin_apartment
from app.routers import admin_module


app = FastAPI()
app.include_router(admin_apartment.router)
app.include_router(admin_auth.router)
app.include_router(admin_module.router)

# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "MakeOver Backend Running"}
