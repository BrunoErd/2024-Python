# Solicite a idade a d o usúario 
nota = int(input("Digite sua nota:"))
#categorize a idade 
if  nota > 90:
    categoria = "Nota A"
elif nota > 80:
    categoria = "Nota B"
elif nota > 70:
    categoria = "Nota C"
elif nota > 60:
    categoria = "Nota D"
else:
    categoria = "Nota F"
    #Exibe a categoria
print(f"Você está na categoria: {categoria}.")
