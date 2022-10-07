

from fastapi import APIRouter, FastAPI

from .routers import post, user, auth
from . import models
from .database import engine

models.Base.metadata.create_all(bind= engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get('/')
def root():
    return { "Message": "This is the message from the server Home Page"}