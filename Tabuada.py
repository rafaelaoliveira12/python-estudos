"""
TABUADA
Autor: Rafaela Vitória Oliveira da Silva
Data: 16/03/2026
Versão: 1.0 
"""

def exibir_menu():
    print("\n" + "-"*60)
    print("TABUADA - MENU PRINCIPAL")
    print("-"*60)
    print("1 - Ver tabuada")
    print("2 - Sair")
    print("-"*60)

def tabuada():
    while True:
        numero = int(input("Digite um número para ver sua tabuada: "))
        
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        
        continuar = input("\nDeseja ver outra tabuada? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado!")
            break
        
        print()

# Função principal com menu
def main():
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção (1-2): "))
            
            if opcao == 1:
                tabuada()
            elif opcao == 2:
                print("\nPrograma encerrado! Até mais!")
                break
            else:
                print("\nOpção inválida! Escolha uma opção entre 1 e 2.")
                
        except ValueError:
            print("\nEntrada inválida! Digite um número (1 ou 2).")

if __name__ == "__main__":
    main()