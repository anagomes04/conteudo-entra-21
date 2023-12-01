nome = input('Informe o nome do aluno: ')
media = float(input('Informe a média do aluno: '))

def situacao(media):
    if media >= 7.0:
        return 'Aprovado'
    else:
        return 'Reprovado'

# print(situacao(media))

informacoes_aluno = {
    'Nome': nome,
    'Média': media,
    'Situação': situacao(media)
}

for chave, valor in informacoes_aluno.items():
    print(f'{chave} ------- {valor}')