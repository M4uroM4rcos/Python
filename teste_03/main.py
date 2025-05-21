import math

# Função para resolver equação do 1º grau: ax + b = 0
def equacao_1_grau(a, b):
    if a != 0:
        x = -b / a
        print(f"A solução da equação {a}x + {b} = 0 é x = {x}")
    else:
        if b == 0:
            print("A equação tem infinitas soluções (0x + 0 = 0).")
        else:
            print("A equação não tem solução (0x + b = 0, com b diferente de 0).")

# Função para resolver equação do 2º grau: ax² + bx + c = 0
def equacao_2_grau(a, b, c):
    if a == 0:
        print("Não é uma equação do 2º grau (a não pode ser 0).")
        return

    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes da equação {a}x² + {b}x + {c} = 0 são x1 = {x1} e x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação tem uma raiz real: x = {x}")
    else:
        print("A equação não possui raízes reais (delta < 0).")

# Função principal com loop
def menu():
    while True:
        print("\nEscolha a equação que deseja resolver:")
        print("1. Equação do 1º grau (ax + b = 0)")
        print("2. Equação do 2º grau (ax² + bx + c = 0)")
        print("3. Sair")
        
        opcao = input("Digite o número da opção (1, 2 ou 3): ")
        
        if opcao == "1":
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            equacao_1_grau(a, b)
        elif opcao == "2":
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            equacao_2_grau(a, b, c)
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
menu()
