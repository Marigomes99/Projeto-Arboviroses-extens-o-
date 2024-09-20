# relatorios.py
def gerar_relatorio(dengue_data, zika_data, chikungunya_data):
    """Gera um relatório sumarizando os dados de incidência de arboviroses."""
    
    report = []
    
    def adicionar_sumario(df, disease_name):
        total_incidencias = df['incidencias'].sum()
        anos = df['ano'].unique()
        anos.sort()
        report.append(f"{disease_name} - Total de Incidências: {total_incidencias}")
        report.append(f"Período de Dados: {anos[0]} a {anos[-1]}")
    
    adicionar_sumario(dengue_data, 'Dengue')
    adicionar_sumario(zika_data, 'Zika')
    adicionar_sumario(chikungunya_data, 'Chikungunya')
    
    with open('relatorio_arboviroses.txt', 'w') as f:
        for line in report:
            f.write(f"{line}\n")
    
    print("Relatório gerado com sucesso.")
