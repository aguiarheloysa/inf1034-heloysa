import random

def jogar_forca():
    lista_palavras = [
        "vermelho", "amarelo", "piscina", "janela", 
        "laranja", "musica", "viagem", "futebol", 
        "basquete", "praia", "roxo", "azul", "verde"
    ]
    
    palavra_secreta = random.choice(lista_palavras).lower()
    
    palavra_oculta = ["_" for _ in palavra_secreta]
    
    vidas_maximas = 6
    vidas_atuais = vidas_maximas
    
    letras_tentadas = set()
    
    print("=" * 40)
    print("       BEM-VINDO AO JOGO DA FORCA!")
    print("=" * 40)
    
    while vidas_atuais > 0 and "_" in palavra_oculta:
        print(f"\nVidas restantes: {vidas_atuais}/{vidas_maximas}")
        print(f"Letras já tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'}")
        print("Palavra: " + " ".join(palavra_oculta))
        
        tentativa = input("Digite uma letra ou chute a palavra inteira: ").strip().lower()
        
        if len(tentativa) > 1:
            if tentativa == palavra_secreta:
                
                for i in range(len(palavra_secreta)):
                    palavra_oculta[i] = palavra_secreta[i]
                break
            else:
                print(f"A palavra '{tentativa}' está incorreta!")
                vidas_atuais -= 1
                continue
                
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida! Digite apenas UMA letra (sem números ou símbolos).")
            continue
            
        if tentativa in letras_tentadas:
            print(f"Você já tentou a letra '{tentativa.upper()}'. Escolha outra.")
            continue
            
        letras_tentadas.add(tentativa)
        
        if tentativa in palavra_secreta:
            print(f"Boa! A letra '{tentativa.upper()}' está na palavra.")
            
            for i, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
        else:
            print(f"Que pena! A letra '{tentativa.upper()}' não está na palavra.")
            vidas_atuais -= 1

    print("\n" + "=" * 40)
    if "_" not in palavra_oculta:
        print(f"PARABÉNS! Você venceu! A palavra era: {palavra_secreta.upper()}")
    else:
        print(f"GAME OVER! Você perdeu todas as vidas. A palavra era: {palavra_secreta.upper()}")
    print("=" * 40)

if __name__ == "__main__":
    while True:
        jogar_forca()
        continuar = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Obrigado por jogar! Até mais.")
            break