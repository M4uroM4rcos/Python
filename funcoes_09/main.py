# lambda
calcular_pg = lambda x: x*2
# lista numérica
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(calcular_pg, numeros))

print("Progressão geométrica: \n")
for n in result:
    print(n)