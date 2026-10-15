import pandas as pd

CAMINHO_CSV = "dados_csv.csv"

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype={"zona":str, "secao":str})
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())