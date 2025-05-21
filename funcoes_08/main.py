# função
import math

def calcular_area_circulo(r):
    area = math.pi * r**2
    return area

if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do circulo: "))
        result = calcular_area_circulo(r)

        print(f"A área do circulo é {result:,.2f}.")
    except Exception as e:
        print(f"Não foi possível calcular a área do circulo. {e}.")

    """ Função com Lambda
    calcular_area_circulo = lambda r: match.pi * r**2"""