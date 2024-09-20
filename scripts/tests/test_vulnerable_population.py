import pytest
import pandas as pd
from scripts.vulnerable_population import analisar_populacao_vulneravel


@pytest.fixture
def sample_data():
    data = {
        'Doença': ['dengue', 'chikungunya', 'zika'],
        'Grupo de risco': ['crianças menores de 2 anos', 'idosos', 'gestantes'],
        'Fatores de risco': ['sistema imunologico', 'idade avançada', 'complicacoes']
    }
    return pd.DataFrame(data)

def test_analisar_populacao_vulneravel(sample_data):
    
    result = analisar_populacao_vulneravel(sample_data)
    
    
    assert 'Risco' in result.columns
    
    
    assert result.loc[result['Grupo de risco'] == 'crianças menores de 2 anos', 'Risco'].iloc[0] == 'Alto'
    assert result.loc[result['Grupo de risco'] == 'idosos', 'Risco'].iloc[0] == 'Baixo'
    assert result.loc[result['Grupo de risco'] == 'gestantes', 'Risco'].iloc[0] == 'Baixo'
    
    
