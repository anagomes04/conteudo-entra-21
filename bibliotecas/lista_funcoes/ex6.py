def is_odd(a):
    if a % 2 != 0:
        return f'Ímpar'

    if a % 2 == 0:
        return f'Par'

    return False

print(is_odd(77))

#ver porque deu certo