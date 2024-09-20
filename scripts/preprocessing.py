def preprocess_all_data(dengue_data, chikungunya_data, casos_suspeitos, grupo_risco, mortalidade):
    """Função para pré-processar todos os dados."""
    
    def preprocess_dataframe(df):
        if 'ano' in df.columns:
            df['ano'] = df['ano'].astype(int)  # Converte a coluna 'ano' para inteiros
        if 'doenca' in df.columns:
            df['doenca'] = df['doenca'].str.strip()  # Remove espaços extras
        return df
    
    dengue_data = preprocess_dataframe(dengue_data)
    chikungunya_data = preprocess_dataframe(chikungunya_data)
    casos_suspeitos = preprocess_dataframe(casos_suspeitos)
    grupo_risco = preprocess_dataframe(grupo_risco)
    mortalidade = preprocess_dataframe(mortalidade)

    # Validação para casos onde 'ano' pode estar ausente
    if 'ano' not in dengue_data.columns or 'ano' not in chikungunya_data.columns:
        raise ValueError("A coluna 'ano' está ausente em um ou mais DataFrames.")
    
    return dengue_data, chikungunya_data, casos_suspeitos, grupo_risco, mortalidade
