import streamlit as st
from utils.loader import load_data
from utils.processors import get_crime_df
from data.charts import (
    casos_bairro,
    casos_anual,
    casos_mensal,
    casos_semanal,
    casos_hora,
    casos_vitima,
)

# Configuração da página
st.set_page_config(page_title="Estupros", page_icon="🚨", layout="centered")

# Título da página
st.title("Casos de Estupro")

# Carrega dados
df = load_data()
df_estupro = get_crime_df(df, ["ESTUPRO", "ESTUPRO DE VULNERAVEL", "ESTUPRO DE VULNERAVEL COM RESULTADO MORTE", "ESTUPRO COM RESULTADO MORTE"])

# Bairros com maior ocorrência
st.subheader("Bairros com maior ocorrência")

estupro_bairro = casos_bairro(df_estupro)
st.bar_chart(estupro_bairro, horizontal=True, x="Bairro", sort="-Quantidade")


# Frequência anual
st.subheader("Frequência anual")

estupro_tempo = casos_anual(df_estupro)
st.line_chart(estupro_tempo, x="Data", y="Quantidade")


# Frequência mensal
st.subheader("Frequência mensal")

estupro_mes = casos_mensal(df_estupro)
st.bar_chart(estupro_mes, x="Mês", y="Quantidade", horizontal=True, sort="-Quantidade")


# Frequência semanal
st.subheader("Frequência semanal")
estupro_semana = casos_semanal(df_estupro)

st.bar_chart(
    estupro_semana,
    x="Dia da semana",
    y="Quantidade",
    horizontal=True,
    sort="-Quantidade",
)


# Horários mais frequentes
st.subheader("Horários mais frequentes")
contagem_horarios = casos_hora(df_estupro)

st.bar_chart(
    contagem_horarios, x="Horário", y="Quantidade", horizontal=True, sort="-Quantidade"
)


# Principais vítimas
st.subheader("Principais vítimas")
st.write("Distribuição de idade por sexo das vítimas:")

vitimas_idade_sexo = casos_vitima(df_estupro)

st.bar_chart(
    vitimas_idade_sexo,
    horizontal=True,
    stack=False,
)

# Mostrar tabela com os valores
st.write("Detalhamento por faixa etária e sexo:")
st.dataframe(vitimas_idade_sexo)
