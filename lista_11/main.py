# NOTE: o SPLIT separa os valores de uma variavel em uma lista.

# variavel
ano = 'Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez'

# algoritmo
try:
    meses = ano.split(', ')
    for mes in meses:
        print(mes)

except Exception as e:
    print(f'Não foi possivel separar os valores. {e}.')