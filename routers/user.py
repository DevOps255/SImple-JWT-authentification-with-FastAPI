from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from data import livres_db, auteurs_db


router = APIRouter(
    prefix="/livre",
    tags=["Livres"]
)

class Livrecreation(BaseModel):
    titre:  str
    auteur: str
    genre: str
    année: int
    
    
class LivreResponse(BaseModel):
    
    id: int
    titre: str
    auteur: str
    genre: str
    nationalité: str
    
@router.get("")
def  get_books(genre: Optional[str] = None):
    
    if genre is not None:
        return [l for l in livres_db if l["genre"]== genre.lower()]
    return livres_db
    
@router.get("/{livre_id}")
def get_single_book(livre_id: int):
    
    for book in livres_db:
        if book["livre_id "] == livre_id:
            return book
            
    raise HTTPException  (status_code=404, detail="tache introuvable ")
        
@router.get("/{livre_id}/auteur")
def get_single_author(livre_id:int):
    for book in livres_db:
        if book["livre_id "] == livre_id:
            auteur_id = livre_id
            
            for author in livres_db:
                if author["id"] == auteur_id:
                    return {
                        "livre": book["titre"],
                        "auteur": author["nom"],
                        "nationalité": author["nationalité"]
                        
                    }
            
    raise HTTPException  (status_code=404, detail="tache introuvable ")
        


