

from fastapi import FastAPI





app = FastAPI()


@app.get('/')
def root():
    return { "Message": "This is the message from the server Home Page"}