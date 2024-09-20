import pytest
import pandas as pd
from scripts.analises import carregar_dados, analisar_dados


@pytest.fixture
def mock_load_data(monkeypatch):
    def mock_read_csv(file_path):
        
        if "casos_suspeitos" in file_path:
            return pd.DataFrame({
                'data_inicio': ['2024-01-01'],
                'data_fim': ['2024-08-24'],
                'doença': ['dengue'],
                'casos_suspeitos': [29247]
            })
        elif "chikungunya" in file_path:
            return pd.DataFrame({
                'Doença': ['Chikungunya'],
                'Período': ['01 de janeiro a 24 de agosto de 2024'],
                'Casos prováveis': [4617],
                'Incidência': [51.0],
                'Variação': ['Aumento de 142,2%'],
                'Casos confirmados': [1315]
            })
       
        return pd.DataFrame()
    
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_carregar_dados(mock_load_data):
    casos_suspeitos, chikungunya, dengue, grupo_risco, mortalidade, zika = carregar_dados()
    
    
    assert not casos_suspeitos.empty
    assert 'data_inicio' in casos_suspeitos.columns
    assert casos_suspeitos['doença'].iloc[0] == 'dengue'
    
    assert not chikungunya.empty
    assert chikungunya['Doença'].iloc[0] == 'Chikungunya'
    
    
def test_analisar_dados(mock_load_data):
    
    analisar_dados()
    
   