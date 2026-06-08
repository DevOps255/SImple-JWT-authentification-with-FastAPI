from fastapi import FastAPI
from pydantic import BaseModel,  EmailStr
from typing import Optional

class RegisterSchema(BaseModel):
    nom: str
    email: str
    PassWord: str
    
class LoginSchema(BaseModel):
    
    
     
    email: str
    PassWord: str
    

class UserResponse(BaseModel):
    
    id: int
    email: str
    nom: str
    PassWord: str
    IsActive: bool
    
class TokenResponse(BaseModel):
    access_token: str
    
    token_type: str
    
    
    
     
    class config:
        from_atrribute=True
        
        
    
    
    
    