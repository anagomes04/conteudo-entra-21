senha_correta = 1234

while True:
    senha = int(input('Informe sua senha: '))

    if len(str(senha)) != len(str(senha_correta)) or senha != senha_correta:
        print('Senha Incorreta.')
        continue

    else:
        print('Senha Correta.')
        break