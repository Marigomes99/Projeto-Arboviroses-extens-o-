import matplotlib.pyplot as plt
import numpy as np
import logging

def plot_incidence(data, disease):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data['ano'], data['incidencias'], marker='o', linestyle='-', color='b')
        plt.title(f'Incidência de {disease}')
        plt.xlabel('Ano')
        plt.ylabel('Incidências')
        plt.grid(True)
        plt.savefig(f'static/{disease.lower()}_incidencia.png')  # Salva na pasta static
        plt.close()
    except Exception as e:
        logging.error(f"Erro ao plotar incidências para {disease}: {e}")

def plot_trends(data, disease):
    try:
        plt.figure(figsize=(10, 6))
        x = data['ano']
        y = data['incidencias']
        if len(x) > 1:  # Verifica se há mais de um ponto para ajuste
            p = np.polyfit(x, y, 2)  # Ajuste polinomial de grau 2
            plt.plot(x, np.polyval(p, x), color='r', linestyle='--')
        plt.scatter(x, y, color='b')
        plt.title(f'Tendências de {disease}')
        plt.xlabel('Ano')
        plt.ylabel('Incidências')
        plt.grid(True)
        plt.savefig(f'static/{disease.lower()}_tendencias.png')  # Salva na pasta static
        plt.close()
    except Exception as e:
        logging.error(f"Erro ao plotar tendências para {disease}: {e}")
