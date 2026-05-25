from sqlachemy import Column, Integer, String, Boolean
from database import Base

class Contact(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key= True, index=True)
    
    nom = Column(String, billable=False)
    
    tel = Column(String, nullable=True)
    
    email = Column(String, nullable=True);
    
    favori = Column(Boolean, default=False)
    
    