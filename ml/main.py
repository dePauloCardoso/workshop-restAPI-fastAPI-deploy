import joblib
from fastapi import FastAPI, responses
from pydantic import BaseModel

class PrevisaoCasaRequest(BaseModel):
    tamanho: int
    quartos: int
    n_vagas: int

class PrevisaoCasaResponse(BaseModel):
    preco_estimado: float

app = FastAPI()

modelo = joblib.load('modelo_casas.pkl')

@app.post('/prever/', response_model=PrevisaoCasaResponse)
def prever_preco(casa: PrevisaoCasaRequest):

    dados_entrada = [[casa.tamanho, casa.quartos, casa.n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    return {
        'preco_estimado': round(preco_estimado, 2)
    }