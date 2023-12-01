nome = input('Informe seu nome: ')
ano_nascimento = int(input('Informe seu ano de nascimento: '))
carteira_trabalho = int(input('Informe o numero da sua carteira de trabalho: '))
genero = input('Informe seu genêro: \n '
               '[1] masculino \n' 
               '[2] feminio')

informacoes = {
    'Nome': nome,
    'Ano de nascimento': ano_nascimento,
    'Carteira de Trabalho': carteira_trabalho,
}

idade = 2023 - ano_nascimento

informacoes['Idade'] = idade

print(informacoes)

if genero == '1' and idade < 65:
    idade_aposentadoria = 65 - idade
elif genero == '2' and idade < 60:
    idade_aposentadoria = 60 - idade

informacoes['Idade de aposentadoria'] = idade_aposentadoria

print(informacoes)