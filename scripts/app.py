from flask import Flask, render_template, flash
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'chave arboviroses'  # Chave secreta

def list_template_files():
    """Listar arquivos na pasta 'templates' ao iniciar o servidor."""
    try:
        print("Arquivos na pasta 'templates':", os.listdir('templates'))
    except FileNotFoundError:
        print("Pasta 'templates' não encontrada.")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

# Usar o contexto do aplicativo manualmente para listar arquivos
with app.app_context():
    list_template_files()

def load_data(file_name):
    """Carrega dados de um arquivo CSV e retorna um DataFrame."""
    data_dir = 'data'
    try:
        return pd.read_csv(f"{data_dir}/{file_name}")
    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado na pasta {data_dir}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Arquivo {file_name} está vazio.")
        return None
    except Exception as e:
        print(f"Erro ao carregar {file_name}: {e}")
        return None

@app.route('/')
def index():
    """Página inicial que exibe um resumo dos dados e gráficos."""
    
    flash('Bem-vindo!')  # Mensagem de boas-vindas

    # Carregar dados
    casos_suspeitos = load_data('casos_suspeitos.csv')
    dengue_csv = load_data('dengue.csv')
    chikungunya_csv = load_data('chikungunya.csv')
    zika_csv = load_data('zika.csv')
    mortalidade = load_data('mortalidade.csv')

    # Verificar se os dados foram carregados corretamente
    if (casos_suspeitos is None or casos_suspeitos.empty or 
        dengue_csv is None or dengue_csv.empty or 
        chikungunya_csv is None or chikungunya_csv.empty or 
        zika_csv is None or zika_csv.empty or 
        mortalidade is None or mortalidade.empty):
        return "Erro ao carregar dados", 500
    
    try:
        # Extrair dados necessários de 'casos_suspeitos'
        casos_suspeitos_dengue = casos_suspeitos[casos_suspeitos['doença'] == 'dengue']['casos_suspeitos'].values[0]
        casos_suspeitos_chikungunya = casos_suspeitos[casos_suspeitos['doença'] == 'chikungunya']['casos_suspeitos'].values[0]
        casos_suspeitos_zika = casos_suspeitos[casos_suspeitos['doença'] == 'zika']['casos_suspeitos'].values[0]
        
        # Extrair dados necessários de 'dengue_csv', 'chikungunya_csv', 'zika_csv' e 'mortalidade'
        incidencia_dengue = dengue_csv['incidencias'].values[0]
        casos_confirmados_dengue = dengue_csv['casos_confirmados'].values[0]
        incidencia_chikungunya = chikungunya_csv['incidencias'].values[0]
        casos_confirmados_chikungunya = chikungunya_csv['casos_confirmados'].values[0]
        incidencia_zika = zika_csv['incidencias'].values[0]
        casos_confirmados_zika = zika_csv['casos_confirmados'].values[0]
        
        mortalidade_dengue = mortalidade[mortalidade['doença'] == 'dengue']['casos_mortalidade'].values[0]
        mortalidade_chikungunya = mortalidade[mortalidade['doença'] == 'chikungunya']['casos_mortalidade'].values[0]
        mortalidade_zika = mortalidade[mortalidade['doença'] == 'zika']['casos_mortalidade'].values[0]
    except Exception as e:
        print(f"Erro ao processar dados: {e}")
        return "Erro interno no servidor", 500

    # Imprimir o caminho completo do template
    template_path = os.path.join(app.template_folder, 'index.html')
    print(f"Caminho do template sendo procurado: {template_path}")

    # Renderizar template com dados
    return render_template('index.html',
                           casos_suspeitos_dengue=casos_suspeitos_dengue,
                           casos_suspeitos_chikungunya=casos_suspeitos_chikungunya,
                           casos_suspeitos_zika=casos_suspeitos_zika,
                           incidencia_dengue=incidencia_dengue,
                           casos_confirmados_dengue=casos_confirmados_dengue,
                           incidencia_chikungunya=incidencia_chikungunya,
                           casos_confirmados_chikungunya=casos_confirmados_chikungunya,
                           incidencia_zika=incidencia_zika,
                           casos_confirmados_zika=casos_confirmados_zika,
                           mortalidade_dengue=mortalidade_dengue,
                           mortalidade_chikungunya=mortalidade_chikungunya,
                           mortalidade_zika=mortalidade_zika)

if __name__ == "__main__":
    app.run(debug=True)
