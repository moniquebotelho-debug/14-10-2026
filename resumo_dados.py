import pandas as pd
from rich.panel import Panel

from carrega_dados import carregar_dados
from formatacao import console, numero_br

def mostrar_resultado(df):
    total_registros = len(df)
    total_votos = pd.to_numeric(df["votos"], errors="coerce").sum()
    total_cidades = df["cidade"].nunique()
    total_candidatos = df["candidato"].nunique()

    texto =(

        f"[bold] Registros: [/] { numero_br(total_registros)}\n"
        f"[bold] Votos: [/] { numero_br(total_votos)}\n"
        f"[bold] Cidades: [/] { numero_br(total_cidades)}\n"
        f"[bold] Candidatos: [/] { numero_br(total_candidatos)}\n"
    )

    console.print(Panel(texto, title="Monique Painel de Eleições", expand=False))

if __name__ == "__main__":
    df  = carregar_dados()
    mostrar_resultado(df)

