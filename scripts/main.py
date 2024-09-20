import logging
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_all_data
from preprocessing import preprocess_all_data

def plot_line_chart(df, x_column, y_column, title, xlabel, ylabel):
    """Plota um gráfico de linha simples."""
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column], marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_bar_chart(df, x_column, y_column, title, xlabel, ylabel):
    """Plota um gráfico de barras simples."""
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_column], df[y_column], color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """Função principal para carregar, pré-processar dados e gerar análises de incidência e tendências."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        logging.info("Iniciando o carregamento dos dados...")
        dengue_csv, chikungunya_csv, casos_suspeitos, grupo_risco, mortalidade = load_all_data()
        logging.info("Dados carregados com sucesso.")
        
        # Verifique e registre as colunas disponíveis em cada DataFrame
        logging.info("Colunas disponíveis em Dengue Data CSV: %s", dengue_csv.columns)
        logging.info("Colunas disponíveis em Chikungunya Data CSV: %s", chikungunya_csv.columns)
        logging.info("Colunas disponíveis em Casos Suspeitos: %s", casos_suspeitos.columns)
        logging.info("Colunas disponíveis em Grupo Risco: %s", grupo_risco.columns)
        logging.info("Colunas disponíveis em Mortalidade: %s", mortalidade.columns)

        # Verifique se algum DataFrame está vazio
        if any(df.empty for df in [dengue_csv, chikungunya_csv, casos_suspeitos, grupo_risco, mortalidade]):
            logging.error("Um ou mais conjuntos de dados estão vazios.")
            return
        
        logging.info("Dengue CSV (primeiras linhas):\n%s", dengue_csv.head())
        logging.info("Chikungunya CSV (primeiras linhas):\n%s", chikungunya_csv.head())
        logging.info("Casos Suspeitos (primeiras linhas):\n%s", casos_suspeitos.head())
        logging.info("Grupo Risco (primeiras linhas):\n%s", grupo_risco.head())
        logging.info("Mortalidade (primeiras linhas):\n%s", mortalidade.head())
        
        logging.info("Iniciando o pré-processamento dos dados...")
        dengue_csv, chikungunya_csv, casos_suspeitos, grupo_risco, mortalidade = preprocess_all_data(
            dengue_csv, chikungunya_csv, casos_suspeitos, grupo_risco, mortalidade
        )
        
        logging.info("Dados pré-processados com sucesso.")
        
        logging.info("Dengue CSV após pré-processamento (primeiras linhas):\n%s", dengue_csv.head())
        logging.info("Chikungunya CSV após pré-processamento (primeiras linhas):\n%s", chikungunya_csv.head())
        logging.info("Casos Suspeitos após pré-processamento (primeiras linhas):\n%s", casos_suspeitos.head())
        logging.info("Grupo Risco após pré-processamento (primeiras linhas):\n%s", grupo_risco.head())
        logging.info("Mortalidade após pré-processamento (primeiras linhas):\n%s", mortalidade.head())
        
        logging.info("Iniciando a análise e visualização dos dados...")
        
        # Exemplo de gráficos de linha para tendências ao longo dos anos
        if 'ano' in dengue_csv.columns and 'incidencias' in dengue_csv.columns:
            plot_line_chart(
                dengue_csv,
                'ano',
                'incidencias',
                'Incidências de Dengue ao Longo dos Anos',
                'Ano',
                'Incidências'
            )
        
        if 'ano' in chikungunya_csv.columns and 'incidencias' in chikungunya_csv.columns:
            plot_line_chart(
                chikungunya_csv,
                'ano',
                'incidencias',
                'Incidências de Chikungunya ao Longo dos Anos',
                'Ano',
                'Incidências'
            )
        
        # Exemplo de gráfico de barras para distribuição por grupo de risco
        if 'grupo' in grupo_risco.columns and 'casos' in grupo_risco.columns:
            plot_bar_chart(
                grupo_risco,
                'grupo',
                'casos',
                'Distribuição de Casos por Grupo de Risco',
                'Grupo de Risco',
                'Número de Casos'
            )
        
        logging.info("Análise e visualização concluídas com sucesso.")
        
    except FileNotFoundError as e:
        logging.error(f"Arquivo não encontrado: {e}")
    except pd.errors.EmptyDataError as e:
        logging.error(f"Erro ao ler o arquivo de dados: {e}")
    except Exception as e:
        logging.error(f"Erro na execução do script: {e}")

if __name__ == "__main__":
    main()
