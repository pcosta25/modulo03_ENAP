#Passo01: Instalando o streamlit
!pip install streamlit

#Passo02: Importando o streamlit e o pandas
import streamlit as st
import pandas as pd

#Passo03: Executando a atividade 01

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
st.write(df)
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

st.write('Você selecionou: ', opcao)

dadosFiltrados = df[df['nomeServidor'] == opcao]
st.write(dadosFiltrados)
