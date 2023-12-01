import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='microsoft'
)

software = 'word'
descricao = 'word 2021 LT'

cursor = conexao.cursor()
# query = ('INSERT INTO softwares'
#          '(nome, versao, descricao, requisitos, valor, data_cadastro) '
#          'VALUES ("excel", "2021", "excel 2021 LT", "internet", 150.00, "2021-02-03")')

query = (f'INSERT INTO softwares'
         f'(nome, versao, descricao, requisitos, valor, data_cadastro) VALUES'
         f' ("{software}", "2021", "{descricao}", "internet", 150.00, "2021-02-03")')

cursor.execute(query)
#fetch para select, commit para insert, update, delete...
# resultado = cursor.fetchall()

conexao.commit()

# for linha in resultado:
#     print(linha)

cursor.close()
conexao.close()