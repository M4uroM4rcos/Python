# NOTE: o JOIN é um comando que pega os valores de uma lista e junta em uma unica variavel.

# Lista
dias = [
    'Domingo',
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado'
]

separador = ', ' # delimitador
semana = separador.join(dias) # junta os itens da lista

# exibe na tela
print(semana)