def mostrar_lista(lista):
    if lista:
        print("Lista atual:", lista)
    else:
        print("A lista está vazia.")

def inserir_item(lista):
    item = input("Digite o item que deseja inserir na lista: ")
    lista.append(item)
    print("Item '{}' inserido com sucesso!".format(item))
    mostrar_lista(lista)

def excluir_item(lista):
    item = input("Digite o item que deseja excluir da lista: ")
    try:
        lista.remove(item)
        print("Item '{}' removido com sucesso!".format(item))
    except ValueError:
        print("O item '{}' não está na lista.".format(item))
    mostrar_lista(lista)  

def gravar_lista(lista):
    try:
        with open("lista.txt", "w") as file:
            for item in lista:
                file.write(item + "\n")
        print("Lista gravada com sucesso!")
    except IOError:
        print("Erro ao gravar a lista no arquivo.")

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as file:
            conteudo = file.read()
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso!")
        return conteudo
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except IOError:
        print(f"Erro ao carregar o arquivo '{nome_arquivo}'.")
        return None

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada com sucesso!")
    mostrar_lista(lista)

def main():
    lista = carregar_arquivo
    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir um novo item na lista")
        print("2. Excluir um item da lista")
        print("3. Mostrar a lista atual")
        print("4. Gravar a lista em um arquivo")
        print("5. Ordenar a lista")
        print("6. Sair do programa")

        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            inserir_item(lista)
        elif escolha == "2":
            excluir_item(lista)
        elif escolha == "3":
            mostrar_lista(lista)
        elif escolha == "4":
            gravar_lista(lista)
        elif escolha == "5":
            ordenar_lista(lista)
        elif escolha == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, escolha uma opção válida.")

if __name__ == "__main__":
    main()
