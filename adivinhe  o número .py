import random 
tentativas = 0
max_tentativas = 5
numSecreto = random.randint(0,10)

while tentativas <  max_tentativas:
    palpite =int(input('Digite seu palpite'))
    tentativas += 1
    
    if palpite == numSecreto:
        print(f'Parabens,você acertou em {tentativas} tentativas')
        break
    elif palpite < numSecreto:
        print('Quase la, tente um numero maior!')
    else:
        print('Quase la, tente um numero menor!')
        
    if  tentativas == max_tentativas:
        print('Você esgotou o numero de tentativas!')
        break
    else:
        print(f'Você possui {max_tentativas - tentativas} tentativas')
print('Fim de jogo')
        
        # TODO: write code...