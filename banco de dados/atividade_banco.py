# criar um programa que faça as seguintes funções:
#criar banco
#criar tabela no banco
# e permita ao usuario interegir com ele por meio de:
# inserir registros - INSERT
# editar registros (nome, estado civil)- UPDATE
# apagar registros (pelo cpf - consultar id)- DELETE
# consultar registros (consultar tudo, filtrar por data, cidade, estado)- SELECT
# o banco de dados modelado contém apenas 1 tabela, com as seguintes colunas:
# id, cpf, nome, estado civil, cep(cidade, estado, bairro e rua), data cadastro
# informações do cep devem ser coletadas através de requests no VIACEP

import mysql.connector
import requests

acao = input('O que você deseja fazer?'
             '1. Inserir um registro'
             '2. Editar um registro'
             '3. Apagar um registro'
             '4. Consultar um registro')

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='informacoes'
)

cursor = conexao.cursor()

if acao == '1':
    cpf = input('Informe seu CPF: ')
    nome = input('Informe seu nome: ')
    estado_civil = input('Informe seu estado civil: ')
    cep = input('Informe seu cep: ')
    data_cadastro = input('Informe a data de cadastro: (YYYY-MM-DD)')

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    cidade = response['localidade']
    estado = response['uf']
    bairro = response['bairro']
    rua = response['logradouro']

    query = (f'INSERT INTO registros'
             f'(nome, cpf, estado_civil, cep, cidade, estado, bairro, rua, data_cadastro) VALUES'
             f'("{cpf}", "{nome}", "{estado_civil}", "{cep}", "{cidade}", "{estado}", "{bairro}", "{rua}", "{data_cadastro}")')
    cursor.execute(query)
    conexao.commit()

elif acao == '2':
    alteracao = input('Você quer editar:'
                      '1. Nome'
                      '2. Estado Civil')

    if alteracao == '1':
        nome = input('Informe o novo nome: ')
        query2_nome = (f'UPDATE registros'
                       f'SET nome = {nome}'
                       f'WHERE id = id[nome]')
        cursor.execute(query2_nome)
        conexao.commit()

    elif alteracao == '2':
        estado_civil = input('Informe o novo estado civil: ')
        query2_civil = (f'UPDATE registros'
                        f'SET estado_civil = {estado_civil}'
                        f'WHERE estado_civil = id[estado_civil]')
        cursor.execute(query2_civil)
        conexao.commit()

elif acao == '3':
    cpf = input('Informe seu CPF do registro a ser deletado: ')
    query3 = (f'DELETE registros'
              f'WHERE id[cpf]')

elif acao == '4':
    consulta = input('Você quer consultar:'
                     '1. Todos os registros'
                     '2. Por data'
                     '3. Por cidade'
                     '4. Por estado')

    if consulta == '1':
        query4_tudo = (f'SELECT * FROM registros')
        cursor.execute(query4_tudo)
        resultado = cursor.fetchall()

    elif consulta == '2':
        data_inicio = input('Informe a data inicial do período de consulta: ')
        data_final = input('Informe a data final do período de consulta: ')
        query4_data = (f'SELECT * FROM registros'
                       f'WHERE data BETWEEN `{data_inicio} AND {data_final}')
        cursor.execute(query4_data)
        resultado = cursor.fetchall()

    elif consulta == '3':
        cidade_consuta = input('Informe a cidade de consulta: ')
        query4_cidade = (f'SELECT * FROM registros'
                         f'WHERE cidade LIKE {cidade_consuta}')
        cursor.execute(query4_cidade)
        resultado = cursor.fetchall()

    elif consulta == '4':
        estado_consulta = input('Informe o estado de consulta: ')
        query4_estado = (f'SELECT * FROM registros'
                         f'WHERE estado = {estado_consulta}')
        cursor.execute(query4_estado)
        resultado = cursor.fetchall()

cursor.close()
conexao.close()