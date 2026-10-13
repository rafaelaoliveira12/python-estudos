"""
CALCULADORA 
Autor: Rafaela Vitória Oliveira da Silva
Data: 17/03/2026
Versão: 1.0 
"""
def exibir_menu():
    print("\n" + "-"*60)
    print("CALCULADORA - MENU PRINCIPAL")
    print("-"*60)
    print("1 - Calculadora básica")
    print("2 - Sair")
    print("-"*60)

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))

            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
            else:
                print("Operador inválido! Por favor, use +, -, *, ou /.")
                continue

            print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")

        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Calculadora encerrada! Até mais!")
            break

# Função principal com menu
def main():
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção (1-2): "))
            
            if opcao == 1:
                calculadora()
            elif opcao == 2:
                print("\nPrograma encerrado! Até mais!")
                break
            else:
                print("\nOpção inválida! Escolha uma opção entre 1 e 2.")
                
        except ValueError:
            print("\nEntrada inválida! Digite um número (1 ou 2).")

if __name__ == "__main__":
    main()