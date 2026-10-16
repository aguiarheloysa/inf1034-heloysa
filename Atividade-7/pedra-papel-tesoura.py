import random

def jogar_jokenpo():
    print("=" * 40)
    print("      BEM-VINDO AO PEDRA, PAPEL E TESOURA!")
    print("=" * 40)
    
    opcoes = ["pedra", "papel", "tesoura"]
    pontos_jogador = 0
    pontos_computador = 0
    empates = 0
    
    while True:
        print("\n--- NOVO ROUND ---")
        print(h:= f"Placar atual -> Você: {pontos_jogador} | Computador: {pontos_computador} | Empates: {empates}")
        
        jogador = input("Escolha [pedra, papel, tesoura] (ou digite 'sair' para encerrar): ").strip().lower()
        
        if jogador == 'sair':
            break
            
        if jogador not in opcoes:
            print("Opção inválida! Escolha exatamente entre: pedra, papel ou tesoura.")
            continue
            
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador.upper()}")
        
        if jogador == computador:
            print("Empate.")
            empates += 1
        elif (
            (jogador == "pedra" and computador == "tesoura") or
            (jogador == "tesoura" and computador == "papel") or
            (jogador == "papel" and computador == "pedra")
        ):
            print(f"Você venceu esta rodada! ({jogador} ganha de {computador})")
            pontos_jogador += 1
        else:
            print(f"Você perdeu esta rodada! ({computador} ganha de {jogador})")
            pontos_computador += 1
            
    print("\n" + "=" * 40)
    print("          FIM DE JOGO - PLACAR FINAL")
    print("=" * 40)
    print(f"Suas vitórias: {pontos_jogador}")
    print(f"Vitórias do computador: {pontos_computador}")
    print(f"Empates: {empates}")
    print("Obrigado por jogar.")

if __name__ == "__main__":
    jogar_jokenpo()