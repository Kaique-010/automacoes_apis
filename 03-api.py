import requests
from pprint import pprint
import pandas as pd
import streamlit as st




def obter_request(url, params=None):
    """Faz uma requisição em GET e retorna a resposta em Json"""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None


def freq_nome(name):
    """Obtém um Dicionário de frequencia de um nome por Década  no formato  de {decada:quantidades}"""
    
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
 
    dados_nome = obter_request(url) or []
    
    #return {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    dados_dict = {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df

def main():
    st.title("Web App -Nomes Por Décadas-")
    st.header("Dados API: IBGE")
    in_name = st.text_input("Digite um nome: ")
    if not in_name:
        st.stop()
    df = freq_nome(in_name)
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        st.write("Frequencia por década")
        st.dataframe(df)
    with col2:
        st.write("Serie Temporal")
        st.line_chart(df)
    #print(freq_nome(in_name))

if __name__ == "__main__":
    main()
    