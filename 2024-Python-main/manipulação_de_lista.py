def mostrar_lista(lista):
    if lista:
        print("Lista atual:", lista)
    else:
        print("A lista está vazia.")

def inserir_item(lista):
    item = input("Digite o item que deseja inserir na lista: ")
    lista.append(item)
    print("Item inserido com sucesso!")
    mostrar_lista(lista)

def excluir_item(lista):
    item = input("Digite o item que deseja excluir da lista: ")
    if item in lista:
        lista.remove(item)
        print("Item removido com sucesso!")
    else:
        print("O item não está na lista.")
    mostrar_lista(lista)

def main():
    lista = []
    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir um novo item na lista")
        print("2. Excluir um item da lista")
        print("3. Mostrar a lista atual")
        print("4. Sair do programa")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            inserir_item(lista)
        elif escolha == "2":
            excluir_item(lista)
        elif escolha == "3":
            mostrar_lista(lista)
        elif escolha == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()