lista = []

qtd_str = 0
qtd_int = 0
qtd_flt = 0
qtd_boo = 0

while True:
    elemento = input('Digite um elemento: ')

    if elemento == '*':
        break

    try:
        f = float(elemento)
        i = int(f)
        if f - i == 0:
            lista.append(i)
            qtd_int += 1
        else:
            lista.append(f)
            qtd_flt += 1
    except ValueError:
        if elemento == 'True':
            lista.append(True)
            qtd_boo += 1
        elif elemento == 'False':
            lista.append(False)
            qtd_boo += 1
        else:
            lista.append(elemento)
            qtd_str += 1

lista.reverse()
print(lista)