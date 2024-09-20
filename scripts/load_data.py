import pandas as pd
import os
import logging

def load_data(file_path):
    """Carrega um arquivo CSV e retorna um DataFrame do pandas."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
    
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        else:
            raise ValueError("Formato de arquivo não suportado. Use apenas .csv")
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar o arquivo {file_path}: {e}")

def load_all_data(data_dir):
    """Carrega todos os arquivos de dados necessários para o projeto a partir do diretório especificado."""
    files = {
        'dengue_csv': os.path.join(data_dir, 'dengue.csv'),
        'chikungunya_csv': os.path.join(data_dir, 'chikungunya.csv'),
        'casos_suspeitos': os.path.join(data_dir, 'casos_suspeitos.csv'),  
        'grupo_risco': os.path.join(data_dir, 'grupo_risco.csv'),
        'mortalidade': os.path.join(data_dir, 'mortalidade.csv'),  # Adiciona o arquivo de mortalidade
    }
    
    data = {}
    for key, file_path in files.items():
        if os.path.isfile(file_path):
            data[key] = load_data(file_path)
        else:
            logging.warning(f"O arquivo {file_path} não foi encontrado.")
            data[key] = pd.DataFrame()  # Inicializa um DataFrame vazio para arquivos ausentes

    return (
        data['dengue_csv'], 
        data['chikungunya_csv'], 
        data['casos_suspeitos'], 
        data['grupo_risco'],
        data['mortalidade'],
    )
