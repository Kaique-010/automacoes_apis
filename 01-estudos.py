from pprint import pprint
import requests

nome = 'Leonardo'

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"  # Corrigido espaço extra

params = {"localidade": 41}

try:
    response = requests.get(url, params=params)
    response.raise_for_status() 
    
    resultado = response.json() 
    
    if resultado:  # Verifica se tem dados na resposta
        pprint(resultado[0]["res"])
    else:
        print("Nenhum resultado encontrado.")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")

except ValueError:
    print("Erro ao converter a resposta para JSON.")
