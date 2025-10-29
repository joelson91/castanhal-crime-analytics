import streamlit as st
from utils.loader import load_data


def home_page():
    st.title("Análise de segurança em Castanhal")
    st.markdown(
        "A seguinte análise utiliza dados de registros de boletim de ocorrência disponibilizados publicamente pela [Secretaria de Segurança Pública e Defesa Social](https://codec.segup.pa.gov.br) de 2010 a 2025."
    )

    # Carrega dados
    df = load_data()

    # Visão Geral
    st.header("Panorama Geral")
    st.subheader("Quantidade de ocorrências por categoria")

    contagem_categorias = df["categoria"].value_counts().reset_index()
    contagem_categorias.columns = ["Categoria", "Quantidade"]

    st.bar_chart(
        contagem_categorias,
        horizontal=True,
        x="Categoria",
        y="Quantidade",
        sort="-Quantidade",
    )


# 2. Configurações e Execução do App
st.set_page_config(
    page_title="Análise de Segurança - Castanhal", page_icon="🚨", layout="centered"
)

pages = [
    st.Page(home_page, title="Home", icon="🏠"),
    st.Page("pages/roubos.py", title="Roubos"),
    st.Page("pages/furtos.py", title="Furtos"),
    st.Page("pages/latrocinio.py", title="Latrocínio"),
    st.Page("pages/homicidio.py", title="Homicídio"),
    st.Page("pages/lesao.py", title="Lesão Corporal"),
    st.Page("pages/transito.py", title="Mortes no Trânsito"),
    st.Page("pages/trafico.py", title="Tráfico de Drogas"),
    st.Page("pages/estupros.py", title="Estupros"),
]

pg = st.navigation(pages)
# st.sidebar.header("Menu de Navegação")
pg.run()
