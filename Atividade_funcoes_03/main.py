""" Crie um programa onde o usuário escolhe uma dessas opção do menu:
0 - Sair do programa,
1 - Criar uma conta,
2 - Alterar dados do titular da conta,
3 - Excluir conta,
4 - Fazer saque,
5 - Fazer depósito
6 - Consultar dados da conta
Dados do titular da conta:
- Nome,
- CPF,
- Agencia (1010),
- Número da conta (número aleatório),
- Saldo (sempre vai começar de zero)"""
# NOTE: Consultar dados da conta envolve consultar saldo da conta.
# NOTE: Para número de conta, use a biblioteca random.

import random as r
import os
import modulo as m

if __name__ == "__main__":
    titular = {}
    try:
        while True:
            print(f"{"="*10}Bem vindo ao Banco Pyton!{"="*10}")
            print("0 - Sair do programa.")
            print("1 - Criar conta.")
            print("2 - Alterar dados do titúlar da conta.")
            print("3 - Fazer saque.")
            print("4 - Fazer deósito.")
            print("5 - Consultar dados da conta.")
            print(f"{"="*40}")
            opcao = input("Informe a opção desejada: ")
            os.system('cls')
            match opcao:
                case "0":
                    print("Programa encerrado com sucesso!")
                    print("Volte sempre!")
                    break
                case "1":
                    titular['nome'] = input("Informe o nome do titular: ")
                    titular['cpf'] = input("Informe o CPF do titular: ")
                    titular['agencia'] = 1010
                    titular['num_conta'] = r.randint(10000, 99999)
                    titular['saldo'] = 0.00

                    os.system('cls')
                    print(f"Conta {titular.get('num_conta')} criada com sucesso.\n")
                    continue

                case "2":
                    print(f"Nome: {titular.get('nome')}")
                    print(f"CPF: {titular.get('cpe')}")
                    campo = input("Informe o campo que deseja alterar: ").strip().lower()
                    match campo:
                        case "nome":
                            titular['nome'] = input("Informe o novo nome do titular: ")
                            os.system('cls')
                            print("Nome atualizado com sucesso!")

                        case "cpf":
                            titular['cpf'] = input("Informe o novo CPF do titular: ")
                            os.system('cls')

                        case _:
                            print("Campo inválido.")
                    continue
                
                case "3":
                    valor = float(input("Informe o valor do saque: R$ ").replace(',', "."))
                    saldo = titular['saldo'] = m.fazer.saque(saldo, valor)
                    if valor <= saldo:
                        titular['saldo'] = m.fazer.saque(saldo, valor)
                        os.system('cls')
                        print("Saque efetuado com sucesso.")
                        print(f"Saldo: R$ {titular.get('saldo'):,.2f}\n")
                    else:
                        print("Não foipossível efetuar o saque, Valor indisponivel.")
                    continue

                case "4":
                    valor = float(input("Informe o valor do depósito: R$ ").replace(",", "."))
                    titular['saldo'] = m.fazer_deposito(titular.get('saldo'), valor)
                    os.system('cls')
                    print("Desósito efetuado com sucesso.")
                    print(f"Saldo: R$ {titular.get('saldo'):,.2f}\n")
                    continue

                case "5":
                    m.consultar_dados(titular)
                    continue

                case _:
                    print("Opção Inválida.")
       
    except Exception as e:
        print(f"Não foi possivel executar a operação. {e}.")