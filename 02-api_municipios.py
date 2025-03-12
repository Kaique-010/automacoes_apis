from pprint import pprint
import requests



url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"  # Corrigido espaço extra

params = {"view": 'nivelado'}

try:
    response = requests.get(url, params=params)
    response.raise_for_status() 
    
    resultado = response.json() 
    
    if resultado:  # Verifica se tem dados na resposta
        pprint(resultado)
    else:
        print("Nenhum resultado encontrado.")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")

except ValueError:
    print("Erro ao converter a resposta para JSON.")
