from typing import Optional
from pydantic import Basemodel


class ContactCreation(Basemodel):
    
    nom: str
    tel: Optional[str]=None
    email: Optional[str]=None
    favori: bool=False
    
class ContactModification(Base model):
    
    nom: Optional[str]=None    
    tel: Optional[str]=None
    email=Optional[str]=None
    favori: Optional[bool]=None
    
class ContactResponse(BaseModel):
    
    id:int
    nom:str
    tel:Optional[str]=None
    email:Optional[str]=None
    favori: bool
    
    class config:
        from_attributes=True