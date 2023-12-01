import mysql.connector

def imprimir_registros(registro):
    for i in registro:
        print(i)

acao = input('O que você deseja fazer? \n'
             '1. Cadastrar um novo registro \n'
             '2. Alterar um registro \n'
             '3. Excluir um registro \n'
             '4. Consultar um registro \n')

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='registro'
)

cursor = conexao.cursor()

if acao == '1':
    cadastro = input('O que você deseja cadastrar? \n'
                     '1. Clientes \n'
                     '2. Produtos \n'
                     '3. Vendas \n')

    if cadastro == '1': #cadastro de clientes
        cpf_clientes = input('Informe o CPF do cliente: ')
        nome_cliente = input('Informe o nome do cliente: ')
        cep = input('Informe o CEP do cliente: ')
        cidade = input('Informe a cidade do cliente: ')
        estado = input('Informe o estado do cliente: ')
        logradouro = input('Informe o lograoduro do cliente: ')
        numero = input('Informe o número da residência do cliente: ')

        query_cadastro_clientes = (f'INSERT INTO clientes'
                                   f'(cpf_clientes, nome_cliente, cep, cidade, estado, logradouro, numero) VALUES'
                                   f'("{cpf_clientes}", "{nome_cliente}", "{cep}", "{cidade}", "{estado}", "{logradouro}", "{numero}") ')
        cursor.execute(query_cadastro_clientes)
        conexao.commit()

    elif cadastro == '2':  # cadastro de produtos
        cod_barras = input('Informe o código de barras do produto: ')
        nome_produto = input('Informe o nome do produto: ')
        fabricante_produto = input('Informe o fabricante do produto: ')

        query_cadastro_produtos = (f'INSERT INTO produtos'
                                   f'(cod_barras, nome_produto, fabricante_produto) VALUES'
                                   f'("{cod_barras}", "{nome_produto}", "{fabricante_produto}") ')
        cursor.execute(query_cadastro_produtos)
        conexao.commit()

    elif cadastro == '3': # cadastro de vendas
        data_venda = input('Informe a data da venda: ')
        hora_venda = input('Informe a hora da venda: ')
        cpf_cliente = input('Informe o CPF do cliente: ')
        codigo_barras = input('Informe o código de barras do produto: ')
        quantidade = int(input('Informe a quantidade vendida: '))
        valor_unitario = float(input('Informe o valor do produto: '))
        valor_total = quantidade * valor_unitario

        query_cadastro_vendas = (f'INSERT INTO vendas'
                                 f'(data_venda, hora_venda, cpf_cliente, codigo_barras, quantidade, valor_unitario, valor_total) VALUES'
                                 f'("{data_venda}", "{hora_venda}", "{cpf_cliente}", "{codigo_barras}", "{quantidade}", "{valor_unitario}", "{valor_total}") ')
        cursor.execute(query_cadastro_vendas)
        conexao.commit()


elif acao == '2':
    aletracao = input('Que tipo de registro você deseja alterar? \n'
                     '1. Clientes \n'
                     '2. Produtos \n'
                     '3. Vendas \n')

    if aletracao == '1': #alteração de clientes
        id = input('Informe o ID do cliente: ')
        informacao_cliente = input('Qual informação do cliente você quer alterar:\n'
                           '1. Nome \n'
                           '2. CEP \n'
                           '3. Cidade \n'
                           '4. Estado \n'
                           '5. Logradouro \n'
                           '6. Número da residência \n')

        if informacao_cliente == '1':
            nome = input('Informe o novo nome: ')
            query_altera_cliente_nome = (f'UPDATE clientes '
                                         f'SET nome_cliente = "{nome}"  '
                                         f'WHERE id = "{id}" ')
            cursor.execute(query_altera_cliente_nome)
            conexao.commit()

        elif informacao_cliente == '2':
            cep = input('Informe o novo CEP: ')
            query_altera_cliente_cep = (f'UPDATE clientes '
                                        f'SET cep = "{cep}" '
                                        f'WHERE id = "{id}" ')
            cursor.execute(query_altera_cliente_cep)
            conexao.commit()

        elif informacao_cliente == '3':
            cidade = input('Informe a nova cidade: ')
            query_altera_cliente_cidade = (f'UPDATE clientes '
                                           f'SET cidade = "{cidade}" '
                                           f'WHERE id = "{id}" ')
            cursor.execute(query_altera_cliente_cidade)
            conexao.commit()

        elif informacao_cliente == '4':
            estado = input('Informe o novo estado: ')
            query_altera_cliente_estado = (f'UPDATE clientes '
                                           f'SET estado = "{estado}" '
                                           f'WHERE id = "{id}" ')
            cursor.execute(query_altera_cliente_estado)
            conexao.commit()

        elif informacao_cliente == '5':
            logradouro = input('Informe o novo logradouro: ')
            query_altera_cliente_logradouro = (f'UPDATE clientes '
                                               f'SET logradouro = "{logradouro}" '
                                               f'WHERE id = "{id}" ')
            cursor.execute(query_altera_cliente_logradouro)
            conexao.commit()

        elif informacao_cliente == '6':
            numero = input('Informe o novo número da residência: ')
            query_altera_cliente_numero = (f'UPDATE clientes '
                                           f'SET numero = "{numero}" '
                                           f'WHERE id = "{id}" ')
            cursor.execute(query_altera_cliente_numero)
            conexao.commit()

    elif aletracao == '2': #alteração de produtos
        id = input('Informe o id do produto cadastrado: ')
        informacao_produto = input('Qual informação do produto você quer alterar: \n'
                           # '1. Códido de barras: \n'
                           '2. Nome: \n'
                           '3. Fabricante: \n')

        # if informacao_produto == '1':
        #     codigo = input('Informe o novo código de barras do produto: ')
        #     query_altera_produto_codigo = (f'UPDATE produtos '
        #                                    f'SET cod_barras = "{codigo}" '
        #                                    f'WHERE id = "{id}" ')
        #     cursor.execute(query_altera_produto_codigo)
        #     conexao.commit()

        if informacao_produto == '2':
            nome = input('Informe o novo nome do produto: ')
            query_altera_produto_nome = (f'UPDATE produtos '
                                           f'SET nome_produto = "{nome}" '
                                           f'WHERE id = "{id}" ')
            cursor.execute(query_altera_produto_nome)
            conexao.commit()

        elif informacao_produto == '3':
            fabricante = input('Informe o novo fabricante do produto: ')
            query_altera_produto_fabricante = (f'UPDATE produtos '
                                               f'SET fabricante_produto = "{fabricante}" '
                                               f'WHERE id = "{id}" ')
            cursor.execute(query_altera_produto_fabricante)
            conexao.commit()

    elif aletracao == '3': #alteração de vendas
        id = input('Informe o ID de barras do produto: ')
        informacao_venda = input('Qual informação do cliente você quer alterar:\n'
                           '1. Data da venda: \n'
                           '2. Hora da venda: \n'
                           # '3. CPF do cliente: \n'
                           '4. Quantidade \n'
                           '5. Valor unitário \n')

        if informacao_venda == '1':
            data = input('Informe a nova data da venda: ')
            query_altera_venda_data = (f'UPDATE vendas '
                                       f'SET data_venda = "{data}" '
                                       f'WHERE id = "{id}" ')
            cursor.execute(query_altera_venda_data)
            conexao.commit()

        elif informacao_venda == '2':
            hora = input('Informe a nova hora da venda: ')
            query_altera_venda_hora = (f'UPDATE vendas '
                                       f'SET hora_venda = "{hora}" '
                                       f'WHERE id = "{id}" ')
            cursor.execute(query_altera_venda_hora)
            conexao.commit()

        # elif informacao_venda == '3':
        #     cpf = input('Informe o novo CPF do cliente: ')
        #     query_altera_venda_cpf = (f'UPDATE vendas '
        #                               f'SET cpf_cliente = "{cpf}" '
        #                               f'WHERE codigo_barras = "{codigo_barras}" ')
        #     cursor.execute(query_altera_venda_cpf)
        #     conexao.commit()

        elif informacao_venda == '4':
            quantidade = input('Informe a nova quantidade da venda: ')
            query_altera_venda_quantidade = (f'UPDATE vendas '
                                             f'SET quantidade = {quantidade}, valor_total = {quantidade} * valor_unitario '
                                             f'WHERE id = "{id}" ')
            cursor.execute(query_altera_venda_quantidade)
            conexao.commit()

        elif informacao_venda == '5':
            valor_produto = input('Informe o valor unitário do produto: ')
            query_altera_venda_valor_produto = (f'UPDATE vendas '
                                                f'SET valor_unitario = "{valor_produto}" , valor_total = {valor_produto} * quantidade '
                                                f'WHERE id = "{id}" ')
            cursor.execute(query_altera_venda_valor_produto)
            conexao.commit()

elif acao == '3':
    exclusao = input('Que tipo de registro você deseja excluir? \n'
                     '1. Clientes \n'
                     '2. Produos \n'
                     '3. Vendas \n')

    if exclusao == '1': #exclusão de clientes
        cpf_clientes = input('Informe o CPF do cliente: ')

        query_verifica_vendas = (f'SELECT id FROM vendas '
                                 f'WHERE vendas.cpf_cliente = "{cpf_clientes}" ')
        cursor.execute(query_verifica_vendas)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            query_exclusao_cliente = (f'DELETE FROM clientes '
                                      f'vendas.cpf_cliente = "{cpf_clientes}" ')
            cursor.execute(query_exclusao_cliente)
            conexao.commit()
        else:
            print('Não foi possível deletar o registro, por causa da FK.')

    elif exclusao == '2': #excluir produto
        codigo_barras = input('Informe o código de barras do produto: ')

        query_verifica_prodtuos = (f'SELECT id FROM vendas '
                                   f'WHERE vendas.codigo_barras = "{codigo_barras}" ')
        cursor.execute(query_verifica_prodtuos)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            query_exclusao_produtos = (f'DELETE FROM clientes '
                                      f'vendas.codigo_barras = "{codigo_barras}" ')
            cursor.execute(query_exclusao_produtos)
            conexao.commit()
        else:
            print('Não foi possível deletar o registro, por causa da FK.')


    elif exclusao == '3': #excluir venda
        id = input('Informe o id do produto cadastrado: ')

        query_exclusao_venda = (f'DELETE FROM vendas '
                                f'WHERE id = {id}')
        cursor.execute(query_exclusao_venda)
        conexao.commit()

elif acao == '4':
    consulta = input('O que você deseja consultar:\n'
                     '1. Vendas por cpf \n'
                     '2. Compras por código de barras \n'
                     '3. Ranking de vendas por produto \n'
                     '4. Ranking de vendas por cliente \n')

    if consulta == '1': #Lista todas as vendas por CPF
        query_vendas_cpf = (f'SELECT clientes.cpf_clientes, vendas.codigo_barras, quantidade, valor_unitario, valor_total, data_venda, hora_venda FROM vendas '
                            f'INNER JOIN (clientes) ON vendas.cpf_cliente = clientes.cpf_clientes')
        cursor.execute(query_vendas_cpf)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

    elif consulta == '2': #Listar todas as compras por código de barras
        query_vendas_codigo = (f'SELECT vendas.codigo_barras, produtos.nome_produto, produtos.fabricante_produto FROM produtos '
                               f'INNER JOIN (vendas) ON produtos.cod_barras = vendas.codigo_barras')
        cursor.execute(query_vendas_codigo)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

    elif consulta == '3': #Ranking de vendas por produto - quantidade daquele produto vendido
        query_ranking_produtos = (f'SELECT vendas.codigo_barras, SUM(vendas.quantidade) AS vendas_produto FROM vendas '
                                  f'GROUP BY vendas.codigo_barras '
                                  f'ORDER BY 2 ASC')
        cursor.execute(query_ranking_produtos)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

    elif consulta == '4': #Ranking de vendas por cliente - quantidadde que cada cliente comprou
        query_ranking_clientes = (f'SELECT clientes.cpf_clientes, SUM(vendas.quantidade) AS vendas_clientes FROM vendas '
                                  f'INNER JOIN (clientes) ON vendas.cpf_cliente = clientes.cpf_clientes '
                                  f'GROUP BY clientes.cpf_clientes '
                                  f'ORDER BY 2 ASC')
        cursor.execute(query_ranking_clientes)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

cursor.close()
conexao.close()