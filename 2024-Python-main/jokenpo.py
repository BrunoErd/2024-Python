import random

def jogar_jokenpo():
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    opcoes = ['pedra', 'papel', 'tesoura']
    pontuacao_jogador = 0
    pontuacao_computador = 0
    
    while True:
        print("\nPontuação atual: Jogador {}, Computador {}".format(pontuacao_jogador, pontuacao_computador))
        jogador = input("Escolha pedra, papel ou tesoura (ou digite 'sair' para sair): ").lower()
        if jogador == 'sair':
            print("Obrigado por jogar!")
            break
        elif jogador not in opcoes:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
            continue
        
        computador = random.choice(opcoes)
        print("O computador escolheu:", computador)
        
        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você ganhou!")
            pontuacao_jogador += 1
        else:
            print("Você perdeu!")
            pontuacao_computador += 1

if __name__ == "__main__":
    jogar_jokenpo()
