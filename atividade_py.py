# Inicializa uma lista vazia para a lista de compras
lista_de_compras = []

# Função para adicionar um item à lista de compras
def adicionar_item():
    item = input("Digite o item que deseja adicionar à lista de compras: ")
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")

# Função para apagar um item da lista de compras
def apagar_item():
    if not lista_de_compras:
        print("A lista de compras está vazia. Não há itens para apagar.")
        return

    print("Itens na lista de compras:")
    for i, item in enumerate(lista_de_compras):
        print(f"{i + 1}. {item}")

    indice = int(input("Digite o número do item que deseja apagar: ")) - 1

    if 0 <= indice < len(lista_de_compras):
        item_removido = lista_de_compras.pop(indice)
        print(f"{item_removido} foi removido da lista de compras.")
    else:
        print("Índice inválido. O item não foi apagado.")

# Função para editar um item na lista de compras
def editar_item():
    if not lista_de_compras:
        print("A lista de compras está vazia. Não há itens para editar.")
        return

    print("Itens na lista de compras:")
    for i, item in enumerate(lista_de_compras):
        print(f"{i + 1}. {item}")

    indice = int(input("Digite o número do item que deseja editar: ") - 1)

    if 0 <= indice < len(lista_de_compras):
        novo_item = input("Digite o novo valor para o item: ")
        lista_de_compras[indice] = novo_item
        print(f"Item editado com sucesso.")
    else:
        print("Índice inválido. O item não foi editado.")

# Função para listar os itens na lista de compras
def listar_itens():
    if not lista_de_compras:
        print("A lista de compras está vazia.")
    else:
        print("Itens na lista de compras:")
        for i, item in enumerate(lista_de_compras):
            print(f"{i + 1}. {item}")

# Loop principal para interagir com o usuário
while True:
    print("\nOpções:")
    print("1. Adicionar item à lista de compras")
    print("2. Apagar item da lista de compras")
    print("3. Editar item na lista de compras")
    print("4. Listar itens da lista de compras")
    print("5. Sair")

    escolha = input("Escolha uma opção (1/2/3/4/5): ")

    if escolha == "1":
        adicionar_item()
    elif escolha == "2":
        apagar_item()
    elif escolha == "3":
        editar_item()
    elif escolha == "4":
        listar_itens()
    elif escolha == "5":
        print("Saindo do programa. Obrigado!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
