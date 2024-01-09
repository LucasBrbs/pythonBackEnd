from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/hello',tags=["APIAnimal"])
def home(nome):
    return{"msg":"a"}