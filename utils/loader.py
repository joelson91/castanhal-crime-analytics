import pandas as pd
import streamlit as st


@st.cache_data
def load_data(path="base_de_dados.csv") -> pd.DataFrame:
    """Carrega e prepara os dados do CSV."""
    colunas = {
        "categoria": "category",
        "especificacao": "category",
        "meio_acao": "category",
        "bairro": "category",
        "latitude": float,
        "longitude": float,
        "local_ocorrencia": "category",
        "sexo_vitima": "category",
        "tipo_vitima": "category",
        "cor_vitima": "category",
        "escolaridade_vitima": "category",
        "estado_civil_vitima": "category",
        "sexo_autor": "category",
        "cor_autor": "category",
        "grau_relacionamento": "category",
    }

    df = pd.read_csv(
        path, sep=";", low_memory=False, dtype=colunas, parse_dates=["data_hora"]
    )
    df["data_hora"] = pd.to_datetime(df["data_hora"], errors="coerce")
    return df
