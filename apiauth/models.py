from sqlalchemy import Column, Integer, String, Boolean
from database import Base
class User(Base):
    __tablename__="utilisateur"
    
    id= Column(Integer, primary_key=True, index=True)
    
    email= Column(String, unique=True, index=True, nullable=False)
    
    nom= Column(String,nullable=False)
    
    HashPassword = Column(String, nullable=False)
    
    IsActive= Column(Boolean, default=True)
    
    
    
    
    