def mostrar_menu(sabores):
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

def adicionar_ao_carrinho(carrinho, sabor, tamanho, cobertura):
    item = {"sabor": sabor, "tamanho": tamanho, "cobertura": cobertura}
    carrinho.append(item)

def mostrar_carrinho(carrinho):
    print("\nSeu Carrinho:")
    if not carrinho:
        print("Carrinho vazio.")
    else:
        for i, item in enumerate(carrinho, 1):
            print(f"{i}. {item['sabor']} - {item['tamanho']} com cobertura de {item['cobertura']}")

def main():
    sabores = ["Chocolate", "Morango", "Pistache", "Coco", "Limão"]
    tamanhos = ["Pequeno", "Médio", "Grande"]
    coberturas = ["Nenhuma", "Granulado", "Calda de Chocolate", "Frutas", "Chantilly"]
    
    carrinho = []

    while True:
        mostrar_menu(sabores)
        sabor_escolhido = escolher_sabor(sabores)
        
        mostrar_tamanhos(tamanhos)
        tamanho_escolhido = escolher_tamanho(tamanhos)
        
        mostrar_coberturas(coberturas)
        cobertura_escolhida = escolher_cobertura(coberturas)

        adicionar_ao_carrinho(carrinho, sabor_escolhido, tamanho_escolhido, cobertura_escolhida)
        
        continuar = input("Deseja adicionar mais itens ao carrinho? (s/n): ").lower()
        if continuar != 's':
            break

    mostrar_carrinho(carrinho)

if __name__ == "__main__":
    main()
