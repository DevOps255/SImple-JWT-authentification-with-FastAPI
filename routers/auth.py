from fastapi import APIRouter, HTTPException
from pydantic import BaseModel 
from data import auteurs_db


router = APIRouter(
    prefix="/auteur",
    tags= ["Auteur"],
)

class AuteurCreation(BaseModel):
    nom: str
    nationalité : str
    

class AuteurResponse(BaseModel):
    id: int
    nom: str
    nationalité: str
    
@router.get('')    
def get_auteur():
    return auteurs_db
    
@router.get("/{auteur_id}")   
def get_single_author(auteur_id: int):
    for author in auteurs_db:
         
         if author["id"] == auteur_id:
             return author
    raise HTTPException(status_code=404, detail="Author not found")       
    
@router.post(" ")
def add_author(data: AuteurResponse):
    
    last = auteurs_db[-1]["id"] if len(auteurs_db) > 0 else 0
    
    new_author = {
        "id": last + 1,
        "nom": data.nom,
        "nationalité": data.nationalité,
        
        
    }
    
    auteurs_db.append(new_author)
    
    return new_author
   
