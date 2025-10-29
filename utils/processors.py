import pandas as pd


def get_crime_df(df: pd.DataFrame, categoria: str|list[str]) -> pd.DataFrame:
    """Filtra dados por categoria de crime."""
    categorias_desejadas = categoria
    return df.query('categoria in @categorias_desejadas').copy()


def faixa_horario(hora) -> str:
    """Define faixa horária."""
    if pd.isna(hora):
        return "Não informado"
    elif hora < 3:
        return "00h - 02h"
    elif hora < 6:
        return "03h - 05h"
    elif hora < 9:
        return "06h - 08h"
    elif hora < 12:
        return "09h - 11h"
    elif hora < 15:
        return "12h - 14h"
    elif hora < 18:
        return "15h - 17h"
    elif hora < 21:
        return "18h - 20h"
    else:
        return "21h - 23h"


def faixa_etaria(idade) -> str:
    """Define faixa etária."""
    if pd.isna(idade):
        return "Não informado"
    elif idade < 18:
        return "Menor de 18"
    elif idade < 25:
        return "18-24"
    elif idade < 35:
        return "25-34"
    elif idade < 45:
        return "35-44"
    elif idade < 60:
        return "45-59"
    else:
        return "60 ou mais"
