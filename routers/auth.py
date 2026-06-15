from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from database import SessionLocal

from models import User
from schema import RegistrerSchema, TokenResponse, LoginSchema, UserResponse
from security import hash_pwd, TokenMakeUp, get_actual_user, get_db, pwd_status


router = APIRouter(prefix="/auth", tags=["Authentification"])

@router.post("/inscription", reseponse_model=UserResponse, status_code=201)
def Registrer(data: RegistrerSchema, db:Session=Depends(get_db)):
    
    
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
         

@router.post("/connexion", TokenResponse)
def Login(data: LoginSchema, db: Depends(get_db)):
    
    user = db.query(User).filter(User.email == data.email).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou Mot de passe incorrect"
        )
        
    Valid_pwd =     pwd_status(
        data.pwd,
        data.hache
    )
    
    if not Valid_pwd:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou Mot de passe incorrect"
        )
        
    if not User.IsActive:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="compte désactivé"
        )
        
     token =    TokenMakeUp(
         {
             "sub": str(User.id)
         }
     )
     
     return {
         "access_token": token,
         "token_type": "bearer"
     }





