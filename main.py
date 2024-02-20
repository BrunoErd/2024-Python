# Solicite o més do ano e descubra qual é a estação  
mes = input("Digite o mes:")
#categorize o més 
if mes in ("Dezembro","Janeiro","fevererio"):
    estação = "Verão"
elif mes in ("Março","Abril","Maio"):
    estação = "Outono"
elif mes in ("Junho","Julho","Agosto"):
    estação = "Inverno"
elif mes in  ("setembro","outubro","Dezembro"):
    estação = "Primavera"

    #Exibe a categoria
print(f"Você está na categoria: {estação}.")
