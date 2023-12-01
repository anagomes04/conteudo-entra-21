conta_correta = 3883183
senha_correta = 12345678
saldo = 9999
#movimentacoes = []

conta = int(input('Informe sua conta: '))
senha = int(input('Informe sua senha: '))

if conta != conta_correta:
    print('Conta incorrta.')

elif senha != senha_correta:
    print('Senha incorreta.')

else:
    while True:
        menu = input(' O que deseja fazer: \n '
                     'a. Consultar saldo \n'
                     'b. Pagar conta \n'
                     'c. Depositar na conta \n'
                     'd. Saque \n'
                     'e. Sair \n')

#acrescentar a opção f de extrato

        if menu == 'a':
            print(f'Saldo: {saldo}')

        elif menu == 'b':
            pagamento = float(input('Informe o valor do pagamento: '))
            if pagamento <= 0:
                print('Não é possível fazer o pagamento de valores negativos ou nulos.')
            elif saldo < pagamento:
                print('Saldo insuficiente. Não é possível pagar a conta.')
            else:
                saldo -= pagamento
                print('Pagamento realizado com sucesso.')
                print(f'Saldo: {saldo}')

        elif menu == 'c':
            deposito = float(input('Informe o valor a ser depositado na conta: '))
            if deposito <= 0:
                print('Não é possível depositar valores negativos ou nulos.')
            else:
                saldo += deposito
                print('Depósito realizado com sucesso.')
                print(f'Saldo: {saldo}')

        elif menu == 'd':
            saque = float(input('Informe o valor a ser sacado da conta: '))
            if saque <= 0:
                print('Não é possível sacar valores negativos ou nulos.')
            elif saldo < saque:
                print('Saldo insuficiente. Não é possível sacar dinheiro.')
            else:
                saldo -= saque
                print('Saque realizado com sucesso.')
                print(f'Saldo: {saldo}')


        elif menu == 'e':
            print('Você saiu da sua conta.')
            break

        # elif menu == 'f':
        #     for movimento in movimentacoes:
        #         print(movimento)

#pode acrescentar a função de descrção e movimentação