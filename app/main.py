
from fastapi import FastAPI
from .routers import post, user, auth, vote
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .config import settings
from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["[https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#class Post(BaseModel):
#    title: str
#    content: str
#   published: bool = True

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "hello world"}

