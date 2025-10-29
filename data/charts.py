import pandas as pd
from utils.processors import faixa_horario, faixa_etaria


def casos_bairro(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma tabela com bairro e quantidade de ocorrências"""
    casos = df["bairro"].value_counts().reset_index()
    casos.columns = ["Bairro", "Quantidade"]
    return casos


def casos_anual(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma tabela com casos por ano"""
    casos = df.set_index("data_hora").resample("YE")["categoria"].count().reset_index()
    casos.columns = ["Data", "Quantidade"]
    return casos


def casos_mensal(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma tabela com casos por mês"""
    df["mes"] = df["data_hora"].dt.month
    contagem_mensal = df["mes"].value_counts().sort_index().reset_index()
    contagem_mensal.columns = ["Mês", "Quantidade"]

    meses = {
        1: "Jan",
        2: "Fev",
        3: "Mar",
        4: "Abr",
        5: "Mai",
        6: "Jun",
        7: "Jul",
        8: "Ago",
        9: "Set",
        10: "Out",
        11: "Nov",
        12: "Dez",
    }
    contagem_mensal["Mês"] = contagem_mensal["Mês"].map(meses)
    return contagem_mensal


def casos_semanal(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma tabela com casos por dia da semana"""
    df["dia_semana"] = df["data_hora"].dt.day_of_week
    contagem_semanal = df["dia_semana"].value_counts().sort_index().reset_index()
    contagem_semanal.columns = ["Dia da semana", "Quantidade"]

    # Criar dicionário para mapear números aos nomes dos dias
    dias = {
        0: "Segunda",
        1: "Terça",
        2: "Quarta",
        3: "Quinta",
        4: "Sexta",
        5: "Sábado",
        6: "Domingo",
    }

    # Converter números para nomes dos dias
    contagem_semanal["Dia da semana"] = contagem_semanal["Dia da semana"].map(dias)
    return contagem_semanal


def casos_hora(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma tabela com casos por intervalo de tempo"""
    df["hora"] = df["data_hora"].dt.hour
    df["faixa_horario"] = df["hora"].apply(faixa_horario)

    contagem_horarios = df["faixa_horario"].value_counts().reset_index()
    contagem_horarios.columns = ["Horário", "Quantidade"]
    return contagem_horarios


def casos_vitima(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma tabela com casos por faixa etária e sexo"""
    df["idade_vitima"] = pd.to_numeric(df["idade_vitima"], errors="coerce")
    df["faixa_etaria"] = df["idade_vitima"].apply(faixa_etaria)

    vitimas_idade_sexo = (
        df.groupby(["faixa_etaria", "sexo_vitima"], observed=True)
        .size()
        .reset_index(name="Quantidade")
        .pivot(index="faixa_etaria", columns="sexo_vitima", values="Quantidade")
        .fillna(0)
    )
    return vitimas_idade_sexo
