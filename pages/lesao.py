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
st.set_page_config(page_title="Lesão Corporal", page_icon="🚨", layout="centered")

# Título da página
st.title("Casos de Lesão Corporal")

# Carrega dados
df = load_data()
df_lesao = get_crime_df(df, "LESAO CORPORAL")

# Bairros com maior ocorrência
st.subheader("Bairros com maior ocorrência")

lesao_bairro = casos_bairro(df_lesao)
st.bar_chart(lesao_bairro, horizontal=True, x="Bairro", sort="-Quantidade")


# Frequência anual
st.subheader("Frequência anual")

lesao_tempo = casos_anual(df_lesao)
st.line_chart(lesao_tempo, x="Data", y="Quantidade")


# Frequência mensal
st.subheader("Frequência mensal")

lesao_mes = casos_mensal(df_lesao)
st.bar_chart(lesao_mes, x="Mês", y="Quantidade", horizontal=True, sort="-Quantidade")


# Frequência semanal
st.subheader("Frequência semanal")
lesao_semana = casos_semanal(df_lesao)

st.bar_chart(
    lesao_semana,
    x="Dia da semana",
    y="Quantidade",
    horizontal=True,
    sort="-Quantidade",
)


# Horários mais frequentes
st.subheader("Horários mais frequentes")
contagem_horarios = casos_hora(df_lesao)

st.bar_chart(
    contagem_horarios, x="Horário", y="Quantidade", horizontal=True, sort="-Quantidade"
)


# Principais vítimas
st.subheader("Principais vítimas")
st.write("Distribuição de idade por sexo das vítimas:")

vitimas_idade_sexo = casos_vitima(df_lesao)

st.bar_chart(
    vitimas_idade_sexo,
    horizontal=True,
    stack=False,
)

# Mostrar tabela com os valores
st.write("Detalhamento por faixa etária e sexo:")
st.dataframe(vitimas_idade_sexo)
