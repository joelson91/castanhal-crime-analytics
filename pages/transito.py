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
st.set_page_config(page_title="Morte no Trânsito", page_icon="🚨", layout="centered")

# Título da página
st.title("Casos de Morte no Trânsito")

# Carrega dados
df = load_data()
df_transito = get_crime_df(df, "MORTE NO TRANSITO")

# Bairros com maior ocorrência
st.subheader("Bairros com maior ocorrência")

transito_bairro = casos_bairro(df_transito)
st.bar_chart(transito_bairro, horizontal=True, x="Bairro", sort="-Quantidade")


# Frequência anual
st.subheader("Frequência anual")

transito_tempo = casos_anual(df_transito)
st.line_chart(transito_tempo, x="Data", y="Quantidade")


# Frequência mensal
st.subheader("Frequência mensal")

transito_mes = casos_mensal(df_transito)
st.bar_chart(transito_mes, x="Mês", y="Quantidade", horizontal=True, sort="-Quantidade")


# Frequência semanal
st.subheader("Frequência semanal")
transito_semana = casos_semanal(df_transito)

st.bar_chart(
    transito_semana,
    x="Dia da semana",
    y="Quantidade",
    horizontal=True,
    sort="-Quantidade",
)


# Horários mais frequentes
st.subheader("Horários mais frequentes")
contagem_horarios = casos_hora(df_transito)

st.bar_chart(
    contagem_horarios, x="Horário", y="Quantidade", horizontal=True, sort="-Quantidade"
)


# Principais vítimas
st.subheader("Principais vítimas")
st.write("Distribuição de idade por sexo das vítimas:")

vitimas_idade_sexo = casos_vitima(df_transito)

st.bar_chart(
    vitimas_idade_sexo,
    horizontal=True,
    stack=False,
)

# Mostrar tabela com os valores
st.write("Detalhamento por faixa etária e sexo:")
st.dataframe(vitimas_idade_sexo)
