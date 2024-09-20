from load_data import load_data_function

def main():
    dengue_data, zika_data, chikungunya_data, casos_suspeitos, gruporisco, mortalidade = load_data_function()
    print("Dengue Data:")
    print(dengue_data.head())
    print("Zika Data:")
    print(zika_data.head())
    print("Chikungunya Data:")
    print(chikungunya_data.head())
    print("Casos Suspeitos Data:")
    print(casos_suspeitos.head())
    print("Grupo Risco Data:")
    print(gruporisco.head())
    print("Mortalidade Data:")
    print(mortalidade.head())

if __name__ == "__main__":
    main()
