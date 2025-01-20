from fastapi import FastAPI,Query
import requests


app = FastAPI()

@app.get('/api/hello')
def helloWorld():
    '''
    Endpoint hello world
    '''
    return {'hello' : 'world'}


@app.get('/api/restaurantes/')
def getRestaurantes(restaurante: str = Query(None)):
    '''
    Endpoint dos cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        
        print(dados_json)
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:    
                dados_restaurante.append({
                "item":item["Item"], 
                "price":item["price"],
                "descricao":item["description"]
                })
    
        return {'Restaurante':restaurante,'cardapio':dados_restaurante}
    
    else:
        print(f' o erro foi {response.status_code}')