while True:
    opcao = int(input('Selecione uma opção: '
                     '[0]'
                     '[1]'
                      ': '))

    if opcao not in range(2):
        print('Opção inválida')

    else:
        print('Opção válida')
        break