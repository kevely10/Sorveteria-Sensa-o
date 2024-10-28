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

def main():
    sabores = ["Chocolate", "Morango", "Pistache", "Coco", "Limão"]
    mostrar_menu(sabores)
    sabor_escolhido = escolher_sabor(sabores)
    print(f"Você escolheu: {sabor_escolhido}")

if __name__ == "__main__":
    main()
