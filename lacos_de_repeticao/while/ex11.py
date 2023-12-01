estoque = 100

while True:
    menu = input(' O que deseja fazer: \n '
                 'a. Adicionar ao estoque \n'
                 'b. Retirar do estoque \n'
                 'c. Consultar saldo \n'
                 'd. Consultar movimentação (entradas e saídas) \n'
                 'e. Sair \n')

    if menu == 'a':
        adicionar = int(input('Informe quantidade que quer adicionar ao estoque:'))
        if adicionar <= 0:
            print('Você não pode adicionar quantidades negativas ou nulas.')
        else:
            estoque += adicionar
            print(f'Foram adicionados {adicionar} itens ao estoque.')
            print(f'Estoque = {estoque}')

    elif menu == 'b':
        retirar = int(input('Informe quantidade que quer retirar do estoque:'))
        if retirar <= 0:
            print('Você não pode retirar quantidades negativas ou nulas.')
        elif estoque < retirar:
            print('Quantidade indisponível para retirar do estoque.')
        else:
            estoque -= retirar
            print(f'Foram retirar {retirar} itens do estoque.')
            print(f'Estoque = {estoque}')

    elif menu == 'd':
        if adicionar:
            print('Houve uma entrada no estoque.')
        elif retirar:
            print('Houve uma saída no estoque.')
        else:
            print('Não houve movimentação no estoque')

    elif menu == 'c':
        print(f'Estoque = {estoque}')

    elif menu == 'e':
        print('Você saiu do sistema.')
        break