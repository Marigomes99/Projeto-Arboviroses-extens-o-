import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings

def plot_incidence(data, disease_name):
    """Plota a incidência de doenças ao longo dos anos com linha de tendência linear."""

    if 'ano' not in data.columns or 'incidencias' not in data.columns:
        raise ValueError("O DataFrame deve conter as colunas 'ano' e 'incidencias'.")

    data = data.sort_values('ano')

    plt.figure(figsize=(12, 6))
    plt.plot(data['ano'], data['incidencias'], marker='o', linestyle='-', color='b', label='Incidências')

    x = data['ano'].values
    y = data['incidencias'].values

    if len(x) > 1:  # Verifica se há mais de um ponto de dados
        print("Dados para ajuste linear:")
        print(f"x: {x}")
        print(f"y: {y}")

        try:
            coef = np.polyfit(x, y, 1)
            plt.plot(x, np.polyval(coef, x), color='r', linestyle='--', label='Tendência Linear')
        except np.linalg.LinAlgError as e:
            print(f"Erro no ajuste linear: {e}")
            warnings.warn(f"Erro no ajuste linear: {e}")
    else:
        print("Não há dados suficientes para ajuste linear.")
        warnings.warn("Não há dados suficientes para ajuste linear.")

    plt.title(f'Incidência de {disease_name}')
    plt.xlabel('Ano')
    plt.ylabel('Número de Incidências')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_trends(data, disease_name):
    """Plota a tendência de incidência com ajuste polinomial de grau 2."""

    if 'ano' not in data.columns or 'incidencias' not in data.columns:
        raise ValueError("O DataFrame deve conter as colunas 'ano' e 'incidencias'.")

    data = data.sort_values('ano')

    plt.figure(figsize=(12, 6))
    x = data['ano'].values
    y = data['incidencias'].values

    if len(x) > 2:  # Verifica se há pelo menos 3 pontos de dados para ajuste polinomial de grau 2
        print("Dados para ajuste polinomial:")
        print(f"x: {x}")
        print(f"y: {y}")

        try:
            coef = np.polyfit(x, y, 2)
            trendline = np.polyval(coef, x)
            plt.plot(x, trendline, color='g', linestyle='--', label='Tendência Polinomial')
        except np.linalg.LinAlgError as e:
            print(f"Erro no ajuste polinomial: {e}")
            warnings.warn(f"Erro no ajuste polinomial: {e}")
    else:
        print("Não há dados suficientes para ajuste polinomial.")
        warnings.warn("Não há dados suficientes para ajuste polinomial.")

    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Dados')
    plt.title(f'Tendência de {disease_name}')
    plt.xlabel('Ano')
    plt.ylabel('Número de Incidências')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Adicione o código principal aqui
if __name__ == "__main__":
    # Exemplo de dados
    data = pd.DataFrame({
        'ano': [2020, 2021, 2022],
        'incidencias': [10, 20, 15]
    })

    plot_incidence(data, 'Exemplo de Doença')
    plot_trends(data, 'Exemplo de Doença')
