#importa bibliotecas
import time
import os

#tratamento de exceção
try:
    #declaração de variavel
    n = int(input('Informe um número inteiro positivo: '))

    #laço de repetição
    for n in range(n, -1, -1):                                  #contagem regressiva
        os.system('cls')                                        #limpa a tela
        print(f'{n} ...')
        time.sleep(1)
    print('BOOOM!!!')
    print('A cobra explodiu!!!')                                           #delay de 1 segundo

except Exception as e:
    print(f'Não foi possivel realizar a contagem. {e}.')

