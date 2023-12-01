palavra = "matematica"

def contar_letra(palavra):
    contador = palavra.count('a')
    return f'{contador}'
print(contar_letra(palavra))