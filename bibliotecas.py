from fastapi import FastAPI
import pandas as pd
from selenium import webdriver
import streamlit as st

app = FastAPI()

# Exemplo de endpoint FastAPI
@app.get("/dados")
def ler_dados():

    # Exemplo de análise de dados com pandas
    df = pd.DataFrame({
        "nome": ["Ana", "Clara", "João"],
        "idade": [22, 25, 30]
    })
    return df.to_dict()

# Exemplo de automação com Selenium
def buscar_google(consulta):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    caixa = driver.find_element("name", "q")
    caixa.send_keys(consulta)
    caixa.submit()
    resultados = driver.title
    driver.quit()
    return resultados

# Exemplo de site com Streamlit
def site_streamlit():
    st.title("Exemplo de Site com Streamlit")
    st.write("Este site foi criado 100% com Python!")
    dados = pd.DataFrame({
        "nome": ["Ana", "Clara", "João"],
        "idade": [22, 25, 30]
    })
    st.dataframe(dados)

