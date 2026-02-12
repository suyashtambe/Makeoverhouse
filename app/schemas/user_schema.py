from pydantic import BaseModel

class AdminRegister(BaseModel):
    name: str
    email: str
    password: str

class AdminLogin(BaseModel):
    email: str
    password: str
