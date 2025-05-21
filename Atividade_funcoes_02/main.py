"""Crie um programa que calcule um número informado pelo usuário da 
sequência Fibonacci"""
# NOTE: ultilizar função recursica.

# declaração função recurciva
def sequencia_fibonacci(n):
    return n if n <= 1 else sequencia_fibonacci(n-1) + sequencia_fibonacci(n-2)

if __name__ == "__main__":
    try:
        n = int(input("Informe um número da sequência de Fibonacci: "))
        # result = sequencia_fibonacci(n)
        for i in range(1, n+1):
            print(sequencia_fibonacci(i))

       # print(f"Valor na sequência de Fibonacci na posição {n} é: {result}.")
    except Exception as e:
        print(f"Não foi possível calcular oa sequência de Fibonacci. {e}.")