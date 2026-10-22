"""ETAPA DE LIMPAR DADOS (NULOS E DUPLICADOS)"""

import pandas as pd
from carrega_dados import carregar_dados

def converter_votos(df):
    df = df.copy()
    df["votos"] = pd.to_numeric(df['votos'], errors='coerce')
    return df

def remover_nulos(df, colunas=None):
    return df.dropna(subset=colunas)

def preencher_nulos(df, colunas=None, valor=0):
    return df.fillna(valeu=valores)

def remover_duplicados(df):
    return df.drop_duplicates()

if __name__ == "__main__":
    df  = carregar_dados()
    df = converter_votos(df)
    print(f" Linhas Originais: {len(df)}")
    print(f" Valores Nulos por Coluna:")
    print(df.isnull().sum())
    print(df.head())

    df = remover_nulos(df, colunas=["votos"])

    salvar_csv(df, "votos_tratados.csv")