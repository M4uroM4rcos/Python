# Crie um programa que receba do usuario uma lista de compras e ordene a lista em ordem alfabetica.
# 1º Obs: só quero os nomes dos itens, deixe os preços e a quantidade de fora.
# 2º Obs: após terminarem, faça o comit no GitHub.

#Adição de lista

nomes = []

# tratamento de execeção

try:
    while True:
        # informe os intens de sua compra
        item = input('Informe os intens de sua compra e confira na lista: ')

        #verifica se o nome foi inserido
        if item != "":
            nomes.append(item)
            continue
        else:
            break

    # ordenar lista
    nomes.sort()

except Exception as e:
    print(f'Não foi possivel inserir dados ma lista. {e}.')

finally:
    for item in nomes:
        print(item) 
