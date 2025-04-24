#importa biblioteca
from datetime import date

#declaração de variaveis
dia = date.today().day
mes = date.today().month
ano = date.today().year

#imprime a data atual
print(f'Data de hoje: {dia}/{mes}/{ano}.')


# importação apenas do modulo date da tabela datetime.