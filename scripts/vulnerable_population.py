import pandas as pd

def carregar_populacao_vulneravel():
    """
    Função para carregar dados da população vulnerável.
    """
    try:
        populacao_vulneravel = pd.read_csv('data/populacao_vulneravel.csv')
        return populacao_vulneravel
    except FileNotFoundError:
        raise FileNotFoundError("O arquivo 'populacao_vulneravel.csv' não foi encontrado no diretório 'data'.")
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar o arquivo 'populacao_vulneravel.csv': {e}")

def visualizar_populacao_vulneravel():
    """
    Função para visualizar dados da população vulnerável.
    """
    try:
        populacao_vulneravel = carregar_populacao_vulneravel()
        print("População Vulnerável:")
        print(populacao_vulneravel.describe())
    except FileNotFoundError as e:
        print(e)
