#importa bibliotecas
import calendar
from datetime import date

# declaração de variveis
mes = date.today().month
ano = date.today().year 


# Imprime o calendario do mês
print(calendar.month (ano, mes))