import jogo_da_forca
import adivinhe_o_número

def escolha_o_jogo ():
    print("hgfdfghj")
    print("escolha o jogo")
    print("vgbhgfdsadfgh")

    print("(1)forca,(2)adivinhação")

    jogo = int input ("qual jogo ?")

    if (jogo ==1):
        print ("jogo da forca")
        jogo_da_forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhação")
        adivinhe_o_número.jogar()   
        
