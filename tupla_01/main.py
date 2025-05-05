# tupla

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')

# lista a tupla
for dia in dias_semana:
    print(dia)

try:
    #tentativa de fazer operação de Lista
    dias_semana.append('Sétima')

    print('\n')

    for dia in dias_semana:
        print(dia)
except Exception as e:
    print(f'Não foi possivel inserir item na tupla. {e}.')