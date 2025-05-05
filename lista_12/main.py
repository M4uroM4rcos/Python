import os

nomes = ['Fulano', 'Cicrano', 'Beltrano', 'João', 'Maria', 'José']

try:
    for i in range(len(nomes)):
        print(f'Código {i}: {nomes[i]}.')
    posicao = int(input('Informe o código do item a ser separao: '))
    nome_separado = nomes.pop(posicao)
    os.system('cls')
    print(nome_separado)
    print(nomes)

except Exception as e:
    print(f'Não foi possivel separar o item da lista. {e}')