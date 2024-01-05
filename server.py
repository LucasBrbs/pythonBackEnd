# uvicorn server:app --reload 
from fastapi import FastAPI


app = FastAPI()

@app.get('/')


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

@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}'
    return {"mensagem": texto}

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    texto = f' O quadrado de {numero} é {resultado}'

    return {'mensagem': texto}

@app.post('/produtos')
def produtos():
    return {'mensaem':'Produto (Espetinho) cadastrado com sucesso'}

