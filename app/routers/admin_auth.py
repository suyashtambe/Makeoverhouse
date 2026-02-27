from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import AdminRegister, AdminLogin
from app.core.security import hash_password, verify_password, create_access_token
from app.core.dependencies import get_current_admin

router = APIRouter(prefix="/api/admin", tags=["Admin Auth"])

@router.get("/me")
def get_admin_profile(current_admin = Depends(get_current_admin)): 
    return {
        "id": current_admin.id,
        "email": current_admin.email,
        "role": current_admin.role
    }
 
@router.post("/register") 
def register_admin(data: AdminRegister, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_admin = User(
        name=data.name,  
        email=data.email,
        password=hash_password(data.password),
        role="admin"
    )
    
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return {"message": "Admin registered successfully"}

@router.post("/login")
def login_admin(data: AdminLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email, "role": user.role})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
