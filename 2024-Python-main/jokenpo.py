import random

def jogar_jokenpo():
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    opcoes = ['pedra', 'papel', 'tesoura']
    pontuacao_jogador = 0
    pontuacao_computador = 0
    
    while pontuacao_jogador < 5 and pontuacao_computador < 5:
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

    if pontuacao_jogador == 5:
        print("Parabéns! Você venceu o jogo!")
    elif pontuacao_computador == 5:
        print("O computador venceu o jogo. Melhor sorte da próxima vez!")

if __name__ == "__main__":
    jogar_jokenpo()
