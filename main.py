nome = input("Escreva seu Nome!")
try:
    idade =int (input("Escreva sua Idade!") )
except ValueError:
    print("vocẽ não digitou um número")
print(f"Olá, {nome},vocẽ tem {idade} anos")         