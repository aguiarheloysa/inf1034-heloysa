def calculadora_vagabunda():
    print("=" * 45)
    print("       CALCULADORA VAGABUNDA (MODO TERMINAL)")
    print("=" * 45)
    print("Regras: Digite a operação (+, -, *, /) e o número.")
    print("Digite 'c' para limpar a memória ou 'sair' para fechar.\n")
    
    memoria = None
    
    while True:
        if memoria is None:
            try:
                entrada_inicial = input("Digite o primeiro número: ").strip().lower()
                if entrada_inicial == 'sair':
                    break
                memoria = float(entrada_inicial)
            except ValueError:
                print("Valor inválido! Digite um número.")
                continue
        
        print(f"\n[Memória Atual / Valor na Tela]: {memoria}")
        
        operador = input("Digite a operação (+, -, *, /), 'c' para zerar ou 'sair': ").strip().lower()
        
        if operador == 'sair':
            break
        elif operador == 'c':
            memoria = None
            print("🧹 Memória limpa!")
            continue
            
        if operador not in ['+', '-', '*', '/']:
            print("Operador inválido! Use apenas +, -, * ou /.")
            continue
            
        try:
            segundo_numero_str = input(f"Digite o número para operar com {memoria}: ").strip().lower()
            if segundo_numero_str == 'sair':
                break
            proximo_numero = float(segundo_numero_str)
        except ValueError:
            print("Valor inválido! Digite um número.")
            continue
            
        if operador == '+':
            memoria = memoria + proximo_numero
        elif operador == '-':
            memoria = memoria - proximo_numero
        elif operador == '*':
            memoria = memoria * proximo_numero
        elif operador == '/':
            if proximo_numero == 0:
                print("Erro: Divisão por zero não permitida!")
                continue
            memoria = memoria / proximo_numero
            
        print(f"Resultado parcial: {memoria}")

    print("\nObrigado por usar a Calculadora Vagabunda!")

if __name__ == "__main__":
    calculadora_vagabunda()