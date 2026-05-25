from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from apicontact.database import Base, engine, SessionLocal
from apicontact.models import Contact
from apicontact.schema import ContactCreation, ContactResponse, ContactModification
from typing import list


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API contact")

app.add_middleware(
    CORSMiddleware,
    allow_origin=["http://localhost:5173"],
    
    allow_credential=True,
    allow_method=["*"],
    allow_methode=["*"]
    
    
def get_db:
    db=SessionLocal() 	  
     try:
    
    




