def mostrar_menu(sabores):
    print("Bem-vindo à Sorveteria Sensação")
    print("Escolha um sabor:")
    for i, sabor in enumerate(sabores, 1):
        print(f"{i}. {sabor}")

def escolher_sabor(sabores):
    while True:
        try:
            escolha = int(input("Digite o número do sabor que você deseja: "))
            if 1 <= escolha <= len(sabores):
                return sabores[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número.")

def mostrar_tamanhos(tamanhos):
    print("Escolha um tamanho:")
    for i, tamanho in enumerate(tamanhos, 1):
        print(f"{i}. {tamanho}")

def escolher_tamanho(tamanhos):
    while True:
        try:
            escolha = int(input("Digite o número do tamanho que você deseja: "))
            if 1 <= escolha <= len(tamanhos):
                return tamanhos[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número.")

def mostrar_coberturas(coberturas):
    print("Escolha uma cobertura:")
    for i, cobertura in enumerate(coberturas, 1):
        print(f"{i}. {cobertura}")

def escolher_cobertura(coberturas):
    while True:
        try:
            escolha = int(input("Digite o número da cobertura que você deseja: "))
            if 1 <= escolha <= len(coberturas):
                return coberturas[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número.")

def main():
    sabores = ["Chocolate", "Morango", "Pistache", "Coco", "Limão"]
    tamanhos = ["Pequeno", "Médio", "Grande"]
    coberturas = ["Nenhuma", "Granulado", "Calda de Chocolate", "Frutas", "Chantilly"]

    mostrar_menu(sabores)
    sabor_escolhido = escolher_sabor(sabores)
    
    mostrar_tamanhos(tamanhos)
    tamanho_escolhido = escolher_tamanho(tamanhos)
    
    mostrar_coberturas(coberturas)
    cobertura_escolhida = escolher_cobertura(coberturas)

    print(f"\nVocê escolheu: {sabor_escolhido} - {tamanho_escolhido} com cobertura de {cobertura_escolhida}")

if __name__ == "__main__":
    main()
