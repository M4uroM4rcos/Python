# tratamento de exceção
#try:
    # declaração de variavel
    #n = int(input('Informe um número inteiro positivo: '))

    # laço for                                                     #1º try contagem crescente
    #for i in range(n+1):
        #print(i)

#except Exception as e:
    #print(f'Não foi possivel realizar a contagem. {e}.')

    # tratamento de exceção
try:
    # declaração de variavel
    n = int(input('Informe um número inteiro positivo: '))

    # laço for
    for n in range(n, -1, -1):                                  #2º try contagem decrescente
        print(n)

except Exception as e:
    print(f'Não foi possivel realizar a contagem. {e}.')
