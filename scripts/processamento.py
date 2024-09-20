import pandas as pd

# Carregar dados
df=pd.read_csv('data/grupo_risco.csv')

#processar dados
df_grouped=df.groupby('some_column').agg({'another_column':'sum'})

#salvar dados
df_grouped.to_csv('data/processed_data.csv')

print("Dados processados com sucesso!")