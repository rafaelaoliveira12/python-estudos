"""
CALCULADORA DE IMC - ÍNDICE DE MASSA CORPORAL
Autor: Rafaela Vitória Oliveira da Silva
Data: 15/03/2026
Versão: 1.0 
"""

def exibir_menu():
    print("\n" + "-"*60)
    print("CALCULADORA DE IMC - MENU PRINCIPAL")
    print("-"*60)
    print("1 - Calcular IMC")
    print("2 - Sair")
    print("-"*60)

# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Rato = (Abaixo do peso)"
    elif 18.5 <= imc < 25:
        return "Alfa = (Peso normal)"
    elif 25 <= imc < 30:
        return "Beta = (Sobrepeso)"
    else:
        return "Estrondoso = (Obesidade)"

# Função da calculadora IMC
def calculadora_imc():
    while True:
        try:
            print("\n" + "="*30)
            print("Calculadora de IMC")
            print("="*30)
            
            peso = float(input("Digite seu peso em kg: "))
            altura = float(input("Digite sua altura em metros: "))
            
            # Validações básicas
            if peso <= 0 or peso > 300:
                print("Erro: Peso deve estar entre 1kg e 300kg!")
                continue
                
            if altura <= 0 or altura > 2.5:
                print("Erro: Altura deve estar entre 0.1m e 2.5m!")
                print("Use ponto ao invés de vírgula (ex: 1.75)")
                continue
            
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            
            print(f"\nSeu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")
            
        except ValueError:
            print("Erro: Digite apenas números válidos!")
            print("Use ponto ao invés de vírgula (ex: 1.75 ou 70.5)")
            continue
        
        continuar = input("\nDeseja calcular outro IMC? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado! Até mais!")
            break

# Função principal com menu
def main():
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção (1-2): "))
            
            if opcao == 1:
                calculadora_imc()
            elif opcao == 2:
                print("\nPrograma encerrado! Até mais!")
                break
            else:
                print("\nOpção inválida! Escolha uma opção entre 1 e 2.")
                
        except ValueError:
            print("\nEntrada inválida! Digite um número (1 ou 2).")

if __name__ == "__main__":
    main()