from fastapi import APIRouter, Depends
from model import User
from schema import UserResponse
from security import get_actual_user


router = APIRouter(prefix="/user", tags=["Utilisateur"])

@router.get("/me", response_model=UserResponse)
def read_profil(
    Current_user: User=Depends(get_actual_user)):
    
    return Current_user