#MÓDULOS
import sys

#MENU PRINCIPAL
def main():
    print("Bem vindo ao jogo!\n")
    user_choice = input("O que deseja fazer? (Escolha uma letra e pressione Enter)\n\na)Jogar \nb)Ler Intruções \nc)Sair do jogo\n\n")

    if user_choice == "a":
        
        #DEFINE A FUNÇÃO GAMEPLAY
        def gameplay():
            first_key = input("Estás no hall da casa. Tens uma porta à esquerda e outra porta à direita.\nÀ tua frente está um armário velho. O que pretendes fazer?\n\na)Abrir a porta à esquerda\nb)Abrir a porta à direita\nc)Vasculhar o armário\n\n")

        #ENTRADA NA PORTA DA ESQUERDA (DORMITÓRIO)
            if first_key == "a":
                second_key = input("Entraste no dormitório. O roupeiro está meio aberto, vamos investigar? \n\na)Sim \nb)Não\n")
                if second_key == "a":
                    third_key = input("Encontraste uma nota! Diz 'Cheeseburguer', parece ser alguma espécie de código.\nNão há aqui mais nada, vamos voltar para o hall\n")
                    gameplay()

        #ENTRADA NA PORTA À DIREITA
                    
                
        
        gameplay()
                 
    elif user_choice == "b":
        
        #DEFINE A FUNÇÃO MANUAL
        def manual():
            print("Este jogo é baseado em texto, pelo que o teu objetivo será encontrar o tesouro escondido nesta casa,\selecionando as letras correspondentes às ações que te serão propostas,\que poderás selecionar utilizando as letras correspondentes e \pressionando a tecla Enter para as realizares. Diverte-te e bom jogo!")
            
        manual()
        
        #TERMINA O PROGRAMA
    elif user_choice == "c":
        sys.exit()

main()


          
          
    
    
    
