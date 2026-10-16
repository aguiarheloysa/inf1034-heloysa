import random

def jogo_usuario_adivinha():
    print("\n" + "=" * 50)
    print("      MODO: VOCÊ ADIVINHA O NÚMERO DO COMPUTADOR")
    print("=" * 50)
    
    numero_secreto = random.randint(1, 1023)
    tentativas = 0
    
    print("Tente adivinhar o número gerado entre 1 e 1023.")
    
    while True:
        try:
            chute = int(input("\nDigite seu palpite: "))
        except ValueError:
            print("Digite apenas números inteiros válidos!")
            continue
            
        tentativas += 1
        
        if numero_secreto < chute:
            print("-1 (O número gerado é MENOR que o seu palpite)")
        elif numero_secreto > chute:
            print("1 (O número gerado é MAIOR que o seu palpite)")
        else:
            print(f"0 (ACERTOU!)")
            print(f"Parabéns! Você descobriu o número {numero_secreto} em {tentativas} tentativa(s).")
            break

def jogo_computador_adivinha():
    print("\n" + "=" * 50)
    print("      MODO: O COMPUTADOR ADIVINHA O SEU NÚMERO")
    print("=" * 50)
    print("Pense em um número entre 1 e 1023 e não conte para ninguém.")
    print("Para cada palpite do computador, responda com as regras:")
    print("  -> Digite -1 se o seu número for MENOR que o palpite dele.")
    print("  -> Digite 1 se o seu número for MAIOR que o palpite dele.")
    print("  -> Digite 0 se o computador ACERTOU o seu número.\n")
    
    input("Pressione ENTER quando já estiver pensando no número...")
    
    limite_inferior = 1
    limite_superior = 1023
    tentativas = 0
    
    while limite_inferior <= limite_superior:
        
        palpite_computador = (limite_inferior + limite_superior) // 2
        tentativas += 1
        
        print(f"\nTentativa {tentativas}: O computador chuta {palpite_computador}.")
        
        try:
            resposta = int(input("Sua resposta (-1, 1 ou 0): "))
        except ValueError:
            print("Resposta inválida! Digite apenas -1, 1 ou 0.")
            tentativas -= 1 
            continue
            
        if resposta == -1:
            
            limite_superior = palpite_computador - 1
        elif resposta == 1:
            
            limite_inferior = palpite_computador + 1
        elif resposta == 0:
            print(f"0 (O computador acertou!)")
            print(f"O computador descobriu o seu número ({palpite_computador}) em {tentativas} tentativa(s)!")
            break
        else:
            print("Opção inválida! Use apenas -1, 1 ou 0.")
            tentativas -= 1

def principal():
    while True:
        print("\n" + "=" * 40)
        print("          JOGO DE ADIVINHAÇÃO")
        print("=" * 40)
        print("Quem vai tentar adivinhar?")
        print("[1] Você (Usuário)")
        print("[2] O Computador")
        print("[3] Sair")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if escolha == '1':
            jogo_usuario_adivinha()
        elif escolha == '2':
            jogo_computador_adivinha()
        elif escolha == '3':
            print("Obrigado por jogar! Até mais.")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    principal()