import requests
from pprint import pprint


def obter_request(url, params=None):
    """Faz uma requisição em GET e retorna a resposta em Json"""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None
    

def buscar_id_estado():
    """Obtem um dicionario de estados  na  forma de id_estado nome_estado"""
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    dados_estados = obter_request(url, params={"view":"nivelado"}) or []
    return {estado["UF-id"]:estado["UF-nome"]for estado in dados_estados}



def freq_nome(name):
    url = url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
 
    dados_frq = obter_request(url, params={"groupBy": "UF"}) or []
    return {int(dado["localidade"]): dado["res"][0]["proporcao"] for dado in dados_frq}

def main(name):
    dict_estados = buscar_id_estado()
    dict_frq = freq_nome(name)
    print(f"=== Frequencia do nome {name} no Estados por 100.000 habitantes===")
    for id_estado, frequencia in sorted(dict_frq.items(),
                                        key=lambda item:item[1],
                                        reverse=True):
        print(f" -> {dict_estados.get(id_estado, 'desconhecido')}: {frequencia}")
    
    
    

if __name__ == "__main__":
    main("Jessica")