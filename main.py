nome = input("Escreva seu Nome!")
try:
    idade =int (input("Escreva sua Idade!") )
except ValueError:
    print("vocẽ não digitou um número")
print(f"Olá, {nome},vocẽ tem {idade} anos")    

try:
    n1 = float(input("digite um número"))
    n2 = float(input("digite mais um número"))
except ValueError:
    print("Tente novamente")
    
soma = n1 + n2

print (f"O número {n1} mais o número {n2} é igual a: {soma}.")
# -*- coding: utf-8 -*-
