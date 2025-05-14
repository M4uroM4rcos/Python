# Programa com as 3 funções criadas, no arquivo funcoes.py
# importar módulo
import funcoes as f

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
                    resultado = f.calcular_quadrilatero(b, h)
                    print(f"A área do quadrilatero é: {resultado}.")
                case "2":
                    resultado =f.calcular_triangulo(b, h)
                    print(f"A área do triângulo é: {resultado}.")
        
        elif opcao == "3":
            b = float(input("Informe o valor de base menor: ").replace(",", "."))
            B = float(input("Informe o valor de base maior: ").replace(",", "."))
            h = float(input("Informe o valor de Altura: ").replace(",", "."))
            resultado = f.calcular_trapezio(b, B, h)
            print(f"A área do trapézio é: {resultado}")

        else:
            print("Opção inválida. Programa encerrado!")   
    except Exception as e:
        print(f"Não foi possivel executar a operação. {e}.")