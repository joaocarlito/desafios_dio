from time import sleep

saldo_disponivel = 0
valor_saque_maximo = 500
extrato_bancario = ''
confirma_acao = ''
quantidade_saque = 0
LIMITE_SAQUES = 3

print('Bem vindo(a) ao Banco XXXXXXX \n\n')

sleep(2)

menu = ('''############### MENU ###############

[1] - Digite 1 para Depósito(s)
[2] - Digite 2 para Saque(s)
[3] - Digite 3 para ver o Extrato
[4] - Digite 4 para Sair

####################################

''')

while True:
    opcao_escolhida = input(menu)

    #DEPÓSITO
    if opcao_escolhida == "1":
        valor = float(input("Qual o valor a ser depositado R$ ? "))
        confirma_acao = input(f'Confirma o depósito no valor de R$ {valor:.2f} ? \nDigite S para SIM ou N para NÃO. ')

    
        if valor > 0:
            if confirma_acao == 'S':
                saldo_disponivel += valor
                extrato_bancario += (f"Depósito: R$ {valor:.2f}\n")
                print(f'\n\nOperação realizada com sucesso. Seu novo saldo é de {saldo_disponivel:.2f}\n\n')
        
            elif confirma_acao == 'N':
                print('\n\nOperação cancelada... \n\n')

            else:
                print('\n\nOpção inválida...\n\n')

    #SAQUE
    elif opcao_escolhida == "2":
        valor = float(input("Qual o valor a ser sacado R$ ? "))
        confirma_acao = input(f'Confirma o saque no valor de {valor:.2f} ? \nDigite S para SIM ou N para NÃO. ')

        if confirma_acao == 'S':
            if valor > saldo_disponivel or valor > valor_saque_maximo or quantidade_saque >= LIMITE_SAQUES:
                print("\n\n Operação falhou. \n\n")
            
            elif valor > 0:
                saldo_disponivel -= valor
                extrato_bancario += (f"Saque R$ {valor:.2f}\n")
                quantidade_saque += 1
                print(f'\n\nOperação realizada com sucesso. Seu novo saldo é de R$ {saldo_disponivel:.2f}\n\n')

            else:
                print('\n\nOpção inválida...\n\n')
        
        elif confirma_acao == 'N':
            print('\n\nOperação cancelada...')

    #EXTRATO
    elif opcao_escolhida == "3":
        print('\n************** EXTRATO **************')
        print('Não foram realizadas movimentações.' if not extrato_bancario else extrato_bancario)
        print(f'\nSaldo disponível: R$ {saldo_disponivel:.2f}')
        print('*************************************')

    #SAIR
    elif opcao_escolhida == "4":
        break

    else:
        print("\n\nOperação inexistente, favor selecionar umao opção válida.\n\n")