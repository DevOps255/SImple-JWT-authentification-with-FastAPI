from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi.security import  OAuth2PasswordBearer

from sqlalchemy.orm import Session
from database import SessionLocal
from models import User






secret_key= "Changer en production"

algo = "HS256"

Expirations = 30

pwd_context = CryptContext(schemes=["bcrypte"], deprecated="auto")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
def hash_pwd(pwd: str) -> str:
    
    return pwd_context.hash(pwd)
    
def pwd_status(pwd: str, hache) -> str:
    
    return pwd_context.verify(pwd, hache)
    
    
    
def TokenMakeUp(data:dict) -> str:
    
    Container = data.copy()
    expiration= datetime.utcnow() + timedelta(minutes=Expirations)
    
    Container.update({"exp": expiration})
    
    token= jwt.encode(Container, secret_key, algorithm=algo )
    
    return token
    
    
    
def get_actual_user(
    token:str= Depends(oauth2_schema),
    db: Session=Depends(get_db)):
    
    
    credential_error= HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalide ou expiré",
        headers={"WWW-Authenticate": "Bearer"},
         
     )
		
     try:
         payload= jwt.decode(token,secret_key, algorithms=[algo] )
         
         
         user_id_str: str= payload.get("sub")
         
         if user_id_str is None:
             raise credential_error
             
          user _id = int(user_id_str)
          utilisateur = db.get(User, user_id)
          
          if utilisateur is  None:
              raise credential_error
              
          if not utilisateur.IsActive:
              
              raise HTTPException(
                  status_code=status.HTTP_403_FORBIDDEN, detail="compte desactivé"
                  
			  )
		return utilisateur
          
          
          
			             



    
    
    










