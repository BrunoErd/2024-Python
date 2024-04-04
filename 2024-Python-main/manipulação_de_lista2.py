import os

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

def carregar_lista(lista):
    nome_arq = input("Digite o nome que você deseja carregar:")
    nome_arq += ",txt"

    try:
        with open(nome_arq, "r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("LISTA CARREGADA COM SUCESSO, tente novamente.")
    except FileNotFoundError:
        print("O arquivo não foi encontrado, tente novamente.")
    except Exception as e:
        print("Ocorreu um erro:", e)  
    
def listar_arquivo(extensao = ",py"):
    diretorios = os.getcwd()
    arquivos = os.listdir(diretorios)
    print("Os arquivos .{extensao}desse diretório são:" )    
    for lista_arquivo in arquivos:
        if lista_arquivo.endswith(extensao)
            print(lista_arquivo)


def gravar_lista(lista):
   nome_arq = input("Digite um nome do arquivo carregar:")
   nome_arq += ".txt"
    with open("lista.txt", "w") as file:
            for item in lista:
                file.write(item + "\n")
        print("Lista gravada com sucesso!")
    except IOError:
        print("Erro ao gravar a lista no arquivo.")
    except FileNotFoundError:
        print(f"Arquivo 'lista.txt' não encontrado.")
    except IOError:
        print(f"Erro ao carregar o arquivo 'lista.txt'.")

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada com sucesso!")
    mostrar_lista(lista)

def main():
    lista = []
    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir um novo item na lista")
        print("2. Excluir um item da lista")
        print("3. Listar arquivos")
        print("4. Mostrar a lista atual")
        print("5. Gravar a lista em um arquivo")
        print("6. Ordenar a lista")
        print("7. Carregar lista")
        print("8. Sair do programa")

        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            inserir_item(lista)
        elif escolha == "2":
            excluir_item(lista)
        elif escolha == "3":
            listar_arquivo()
        elif escolha == "4":
            mostrar_lista(lista)
        elif escolha == "5":
            gravar_lista(lista)
        elif escolha == "6":
            ordenar_lista(lista)
        elif escolha == "7":
            carregar_lista()
        elif escolha == "8":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, escolha uma opção válida.")

if __name__ == "__main__":
    main()
