# TODO: Atividade
'''
Crie um programa em que o usuário informa várias notas de um aluno de 0 a 10 (quantas notas ele quiser inserir), e ao final,
o programa calcula a média desse aluno e informa se ele está aprovado, de recuperação ou reprovado.
Obs: média para aprovação: 7, média para recuperação: entre 5 e 7, abaixo de 5: reprovado.
'''
# NOTE: Usar o replace() para substituir a virgula por ponto em valores decimais.

import os

notas = []

try:
    while True:
        nota = float(input('Informe a nota do aluno: ').replace(',', '.'))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            print('Nota inserida com sucesso!')
            while True:
                continuar = input('Deseja inserir outra nota? (s/n)')
                if continuar == 's' or continuar == 'n':
                    os.system('cls')
                    break
                else:
                    print('Opção invalida')
                    continue
            match continuar:
                case 's':
                    continue
                case 'n':
                    break
        else:
            print('Nota invalida. Favor inserir uma nota válida.')
            continue

    for i in range(len(notas)):
        print(f'Nota {i}: {notas[i]}.')

    media = sum(notas)/len(notas)
except Exception as e:
    print(f'\nNão foi possivel inserir as notas e calcular a média. {e}.')
finally:
    print(f'Médias das notas: {media:,.2f}.')
    if media >= 7:
        print('O aluno está aprovado.')
    elif media >= 5:
        print('O aluno está de recuperação.')
    else:
        print('O aluno está reprovado.')