# Programa com 2 funções criadas, no arquivo funcoes.py
from funcoes import calcular_quadrilatero, calcular_triangulo

if __name__ == "__main__":
    try:
        print("Escolha a figura da qual deseja calcular a área:\n")
        print("1 - Quadrilatero")
        print("2 - Triângulo")
        print("3 - Trapézio")
        opcao = input("Opção desejada: ")
        if opcao == "1" or opcao == "2":
            b = float(input("Informe o valor de base: ").replace(",", "."))
            h = float(input("Informe o valor de Altura: ").replace(",", "."))
            match opcao:
                case "1":
                    resultado = calcular_quadrilatero(b, h)
                    print(f"A área do quadrilatero é: {resultado}.")
                case "2":
                    resultado = calcular_triangulo(b, h)
                    print(f"A área do triângulo é: {resultado}.")
        
        else:
            print("Opção inválida. Programa encerrado!")   
    except Exception as e:
        print(f"Não foi possivel executar a operação. {e}.")