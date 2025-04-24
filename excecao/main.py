# tratamento de exceção
try:
    # declaração de bariavel
    x = int(input('Informe um número inteiro: '))

    # saída de dados
    print(f'O número informado foi {x}.')
except Exception as é:
    print(f'Não foi possível ler o número informado pelo usuário. {é}')
finally:
    print('Meu programa foi executado com sucesso!')