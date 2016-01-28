#MÓDULOS
import sys

#MENU PRINCIPAL
def main():
    print("Bem vindo ao jogo!\n")
    user_choice = input("O que deseja fazer? (Escolha uma letra e pressione Enter)\n\na)Jogar \nb)Ler Intruções \nc)Sair do jogo\n\n")

    if user_choice == "a":
        
        #DEFINE A FUNÇÃO GAMEPLAY
        def gameplay():
            first_key = input("O teu objetivo é encontrares o tesouro escondido nesta casa\
            \nAtravés de puzzles e enigmas. Achas que consegues? Então vamos lá.\
            \nEstás no hall da casa. Tens uma porta à esquerda e outra porta à direita.\nÀ tua frente está um armário velho. O que pretendes fazer?\n\na)Abrir a porta à esquerda\nb)Abrir a porta à direita\nc)Vasculhar o armário\n\n")
        #ENTRADA NA PORTA DA ESQUERDA (DORMITÓRIO)
            if first_key == "a":
                print("Entraste no dormitório. O roupeiro está meio aberto, vamos investigar? \na)Sim \nb)Não")
                
        
        gameplay()
                 
    elif user_choice == "b":
        
        #DEFINE A FUNÇÃO MANUAL
        def manual():
            print("Este jogo é baseado em texto, pelo que irás seguir uma historia que terás de ser tu próprio a completá-la,\selecionando as letras correspondentes às ações que te serão propostas,\que poderás selecionar utilizando as letras correspondentes e \pressionando a tecla Enter para as realizares. Diverte-te e bom jogo!")
            
        manual()

    elif user_choice == "c":
        sys.exit()

main()


          
          
    
    
    
