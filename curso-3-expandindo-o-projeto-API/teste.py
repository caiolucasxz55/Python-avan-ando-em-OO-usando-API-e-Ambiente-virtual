
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
            
        dados_restaurante[nome_do_restaurante].append({
        "item":item["Item"], 
        "price":item["price"],
        "descricao":item["description"]
        })
    
    
    
else:
    print(f' o erro foi {response.status_code}')
    
print(dados_restaurante['Pizza Hut'])