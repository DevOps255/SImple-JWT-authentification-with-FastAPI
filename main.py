from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from router.auth import router as AuthRouter
from router.user import router as UserRouter


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Auth JWT")

app.include_router(AuthRouter)
app.inlcude_router(UserRouter)

@app.get("/")
def Welcome():
    return {
        "message": "API avec Auth"
    }