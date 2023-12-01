def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def saudar():
    return 'Bom dia'

#def só roda quando é chamado

# print(saudar())
# print(somar(5, 9))

def get_perimeter(base, altura):
    return 2 * (base + altura)

def is_saqure(base: int, altura: int): #passa o tipo de variável p/ não dar erro
    if base == altura:
        return True
    return False
#não precisa do else, porque é só uma verificação


def saudar_manha(nome):
    return f'Bom dia {nome}'
#não deve estar detro de um print, pode estar numa f string

def is_triangle(a, b, c):
    if a > b + c and b > c + a and c > a + b:
        return True
    if a <= 0 or b <= 0 or c <= 0:
        return 'lado não pode ser zero'
    if a == b == c:
        return 'Triângulo equilátero'
    if (a == b) or (a == c) or (b == c):
        return 'Triângulo isósceles'
    if a != b != c:
        return 'triângulo escaleno'
    return False

def ano_bissexto(a):
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        return True
    return False