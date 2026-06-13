from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from database import SessionLocal

from models import User
from schema import RegistrerSchema, TokenResponse, LoginSchema, UserResponse
from security import hash_pwd, TokenMakeUp, get_actual_user, get_db


router = APIRouter(prefix="/auth", tags=["Authentification"])

@router.post("/inscription", reseponse_model=UserResponse, status_code=201)
def 
    
    FormHash = hash_pwd(data.pwd)
    
    new_user = User(
        email = data.email,
        nom = data.nom,
        PassWord = data.PassWord
    )
    
    try:
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
    except IntegrityError:
        db.rollback()   
        raise HTTPException(
             status_code=400, 
             detail="cet email est deja utilisé!", detail="cet email est deja utilisé!"
         )
    return new_user   
         







