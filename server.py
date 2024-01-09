# uvicorn server:app --reload 
# http://localhost:8000/docs#/default/produtos_produtos_post
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

description = """
TrainingApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="ChimichangApp",
    description=description,
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "https://www.linkedin.com/feed/",
        "email": "lucasbarbosa2807@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

# async def root():
#     return {"mensagem":"hello"}

# @app.get('/profile')
# def profile():
#     return{"nome": "teste"}

# @app.put('/profile')
# def atualizar():
#     return{"mensagem": "Perfil Criado com sucesso!"}

# @app.post('/profile')
# def signup():
#     return{"mensagem": "Perfil Criado com sucesso!"}

# @app.delete('/profile')
# def remover():
#     return{"mensagem": "Perfil Criado com sucesso!"}

@app.get('/saudacao/{nome}',tags=["test"])
def saudacao(nome: str):
    texto = f'Olá {nome}'
    return {"mensagem": texto}

@app.get('/quadrado/{numero}',tags=["test"])
def quadrado(numero: int):
    resultado = numero * numero
    texto = f' O quadrado de {numero} é {resultado}'

    return {'mensagem': texto}

class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos',tags=["test"])
def produtos(produto: Produto):
    return {'mensaem':f'Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso'}

#animal API
class Animal(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get('/animais',tags=["APIAnimal"])
def listarAnimais():
    return banco

@app.post('/animais',tags=["APIAnimal"])
def criarAnimais(animal: Animal):
    banco.append(animal)

    return None


