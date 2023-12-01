l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))

if (l1 > l2 + l3) or (l2 > l1 + l3) or (l3 > l1 + l2):
    print('Não é um triângulo')
elif l1 <= 0 or l2 <= 0 or l3 <= 0:
    print('Não é um triângulo')
elif l1 == l2 == l3:
    print('Triângulo equilátero')
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
    print('Triângulo isósceles')
elif l1 != l2 != l3:
    print('triângulo escaleno')
else:
    print('valor do lado não informado')

# a última opção já poderia ser um else, não precisava fazer a regra no elif

