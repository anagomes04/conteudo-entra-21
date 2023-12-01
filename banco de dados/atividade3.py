import mysql.connector

def imprimir_registros(registro):
    for i in registro:
        print(i)

def atualiza_tabela(tabela, campo, valor, id_registro):
    query = (f'UPDATE {tabela} '
             f'SET {campo} = "{valor}" '
             f'WHERE id = {id_registro}')
    cursor.execute(query)
    conexao.commit()

def deleta_tabela(tabela, id_registro):
    query = (f'DELETE FROM {tabela} '
             f'WHERE id = {id_registro}')
    cursor.execute(query)
    conexao.commit()

acao = input('O que você deseja fazer? \n'
             '1. Cadastrar um novo registro \n'
             '2. Alterar um registro \n'
             '3. Excluir um registro \n'
             '4. Gerar um relatório \n')

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='viagens_aereas'
)

cursor = conexao.cursor()

if acao == '1':
    cadastro = input('O que você deseja cadastrar? \n'
                     '1. Empresas \n'
                     '2. Aeronaves \n'
                     '3. Aeroportos \n'
                     '4. Voos \n')

    if cadastro == '1':  # cadastro de empresas
        codigo = input('Informe o código da empresa: ')
        nome = input('Informe o nome da empresa: ')
        nacionalidade= input('Informe a nacionalidade da empresa: ')

        query_cadastro_empresa = (f'INSERT INTO empresas'
                                  f'(codigo_empresa, nome_empresa, nacionalidade_empresa) VALUES'
                                  f'("{codigo}", "{nome}", "{nacionalidade}") ')
        cursor.execute(query_cadastro_empresa)
        conexao.commit()

    elif cadastro == '2':  # cadastro de aeronaves
        codigo = input('Informe o código da aeronave: ')
        modelo = input('Informe o modelo da aeronave: ')
        assentos = input('Informe a quantidade de assentos da aeronave: ')
        bagagem = input('Informe o limite de bagagem da aeronave: ')

        query_cadastro_aeronave = (f'INSERT INTO aeronaves'
                                   f'(codigo_aeronave, modelo, assentos_aeronave, limite_bagagem) VALUES'
                                   f'("{codigo}", "{modelo}", "{assentos}", "{bagagem}") ')
        cursor.execute(query_cadastro_aeronave)
        conexao.commit()

    elif cadastro == '3':  # cadastro de aeroportos
        codigo = input('Informe o código do aeroporto: ')
        nome = input('Informe o nome do aeroporto: ')
        sigla = input('Informe a sigla do aeroporto: ')
        cidade = input('Informe a cidade do aeroporto: ')
        estado = input('Informe o estado do aeroporto: ')
        pais = input('Informe o país do aeroporto: ')
        continente = input('Informe o continente do aeroporto: ')

        query_cadastro_aeroporto = (f'INSERT INTO aeroportos'
                                    f'(codigo_aeroporto, nome_aeroporto, sigla_aeroporto, cidade_aeroporto, estado_aeroporto, pais_aeroporto, continente_aeroporto) VALUES'
                                    f'("{codigo}", "{nome}", "{sigla}", "{cidade}", "{estado}", "{pais}", "{continente}") ')
        cursor.execute(query_cadastro_aeroporto)
        conexao.commit()

    elif cadastro == '4': #cadastro de voos
        codigo = input('Informe o código do voo: ')
        data_saida = input('Informe a data de saída do voo: ')
        data_chegada = input('Informe a data de chegada do voo: ')
        passageiros = input('Informe o número de passageiros do voo: ')
        assentos = input('Informe o número de assentos do voo: ')
        carga = input('Informe o peso da carga carregada do voo: ')
        cod_empresa = input('Informe o código da empresa: ')
        cod_aeronave = input('Informe o código da aeronave: ')
        cod_aeroporto_decolagem = input('Informe o código do aeroporto de decolagem: ')
        cod_aeroporto_destino = input('Informe o código do aeroporto de destino: ')

        query_cadastro_voo = (f'INSERT INTO voos'
                              f'(codigo_voo, data_saida, data_chegada, numero_passageiros, assentos_voo, carga_carregada, cod_empresa, cod_aeronave, cod_aeroporto_decolagem, cod_aeroporto_destino) VALUES'
                              f'("{codigo}", "{data_saida}", "{data_chegada}", "{passageiros}", "{assentos}", "{carga}", "{cod_empresa}", "{cod_aeronave}", "{cod_aeroporto_decolagem}", "{cod_aeroporto_destino}") ')
        cursor.execute(query_cadastro_voo)
        conexao.commit()

elif acao == '2':
    alteracao = input('Que tipo de registro você deseja alterar? \n'
                      '1. Empresas \n'
                      '2. Aeronaves \n'
                      '3. Aeroportos \n'
                      '4. Voos \n')

    if alteracao == '1':  # alteração de empresas
        id = input('Informe o ID da empresa: ')
        informacao_empresa = input('Qual informação da empresa você quer alterar:\n'
                                   '1. Código \n'
                                   '2. Nome \n'
                                   '3. Nacionalidade \n')

        if informacao_empresa == '1': # alteração do código da empresa
            query_verifica_voo = (f'SELECT voos.id FROM voos '
                                  f'INNER JOIN (empresas) ON voos.cod_empresa = empresas.codigo_empresa '
                                  f'WHERE empresas.id = {id} ')
            cursor.execute(query_verifica_voo)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                codigo = input('Informe o novo código da empresa: ')
                atualiza_tabela(tabela='empresas', campo='codigo_empresa', valor=codigo, id_registro=id)
            else:
                print('Não foi possível alterar o registro, pois há um voo registrado dessa empresa.')

        elif informacao_empresa == '2': # alteração do nome da empresa
            nome = input('Informe o novo nome da empresa: ')
            atualiza_tabela(tabela='empresas', campo='nome_empresa', valor=nome, id_registro=id)

        elif informacao_empresa == '3':  # alteração da nacionalidade da empresa
            nacionalidade = input('Informe a nova nacionalidade nome da empresa: ')
            atualiza_tabela(tabela='empresas', campo='nacionalidade_empresa', valor=nacionalidade, id_registro=id)

    elif alteracao == '2':  # alteração de aeronaves
        id = input('Informe o ID da aeronave: ')
        informacao_aeronave = input('Qual informação da aeronave você quer alterar:\n'
                                   '1. Código \n'
                                   '2. Modelo \n'
                                   '3. Quantidade de assentos \n'
                                   '4. Limite de bagagem \n')

        if informacao_aeronave == '1': # alteração do código da aeronave
            query_verifica_voo = (f'SELECT voos.id FROM voos '
                                  f'INNER JOIN (aeronaves) ON voos.cod_aeronave = aeronaves.codigo_aeronave '
                                  f'WHERE aeronaves.id = {id} ')
            cursor.execute(query_verifica_voo)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                codigo = input('Informe o novo código da aeronave: ')
                atualiza_tabela(tabela='aeronaves', campo='codigo_aeronave', valor=codigo, id_registro=id)
            else:
                print('Não foi possível alterar o registro, pois há um voo registrado dessa aeronave.')

        elif informacao_aeronave == '2':  # alteração do modelo da aeronave
            modelo = input('Informe o novo modelo da aeronave: ')
            atualiza_tabela(tabela='aeronaves', campo='modelo', valor=modelo, id_registro=id)

        elif informacao_aeronave == '3':  # alteração da quantidade de assentos da aeronave
            qtde_assentos = input('Informe a nova quantidade de assentos da aeronave: ')
            atualiza_tabela(tabela='aeronaves', campo='assentos_aeronave', valor=qtde_assentos, id_registro=id)

        elif informacao_aeronave == '4':  # alteração do limite de bagagem da aeronave
            lim_bagagem = input('Informe o novo limite de bagagem da aeronave: ')
            atualiza_tabela(tabela='aeronaves', campo='limite_bagagem', valor=lim_bagagem, id_registro=id)

    elif alteracao == '3':  # alteração de aeroportos
        id = input('Informe o ID do aeroporto: ')
        informacao_aeroporto = input('Qual informação do aeroporto você quer alterar:\n'
                                    '1. Código \n'
                                    '2. Nome \n'
                                    '3. Sigla \n'
                                    '4. Cidade \n'
                                    '5. Estado \n'
                                    '6. País \n'
                                    '7. Continente \n')

        if informacao_aeroporto == '1': # alteração do código do aeroporto
            query_verifica_voo = (f'SELECT voos.id FROM voos '
                                  f'INNER JOIN (empresas) ON voos.cod_empresa = empresas.codigo_empresa '
                                  f'WHERE empresas.id = {id} ')
            cursor.execute(query_verifica_voo)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                codigo = input('Informe o novo código do aeroporto: ')
                atualiza_tabela(tabela='aeroportos', campo='codigo_aeroporto', valor=codigo, id_registro=id)
            else:
                print('Não foi possível alterar o registro, pois há um voo registrado desse aeroporto.')

        elif informacao_aeroporto == '2': # alteração do nome do aeroporto
            nome = input('Informe o novo nome do aeroporto: ')
            atualiza_tabela(tabela='aeroportos', campo='nome_aeroporto', valor=nome, id_registro=id)

        elif informacao_aeroporto == '3': # alteração da sigla do aeroporto
            sigla = input('Informe a nova sigla do aeroporto: ')
            atualiza_tabela(tabela='aeroportos', campo='sigla_aeroporto', valor=sigla, id_registro=id)

        elif informacao_aeroporto == '4': # alteração da cidade do aeroporto
            cidade = input('Informe a nova cidade do aeroporto: ')
            atualiza_tabela(tabela='aeroportos', campo='cidade_aeroporto', valor=cidade, id_registro=id)

        elif informacao_aeroporto == '5': # alteração do estado do aeroporto
            estado = input('Informe o novo estado do aeroporto: ')
            atualiza_tabela(tabela='aeroportos', campo='estado_aeroporto', valor=estado, id_registro=id)

        elif informacao_aeroporto == '6': # alteração do país do aeroporto
            pais = input('Informe o novo país do aeroporto: ')
            atualiza_tabela(tabela='aeroportos', campo='pais_aeroporto', valor=pais, id_registro=id)

        elif informacao_aeroporto == '7':  # alteração do continente do aeroporto
            continente = input('Informe o novo continente do aeroporto: ')
            atualiza_tabela(tabela='aeroportos', campo='continente_aeroporto', valor=continente, id_registro=id)

    elif alteracao == '4':  # alteração de voos
        id = input('Informe o ID do aeroporto: ')
        informacao_voo = input('Qual informação do voo você quer alterar:\n'
                                    '1. Código \n'
                                    '2. Data de Saída \n'
                                    '3. Data de Chegada \n'
                                    '4. Número de Passageiros \n'
                                    '5. Número de Assentos \n'
                                    '6. Carga carregada \n'
                                    '7. Código da Empresa \n'
                                    '8. Código da Aeornave \n'
                                    '9. Código do aeroporto de decolagem \n'
                                    '10. Código do aeroporto de destino \n')

        if informacao_voo == '1': #alteração do código do voo
            codigo = input('Informe o novo código do voo: ')
            atualiza_tabela(tabela='voos', campo='codigo_voo', valor=codigo, id_registro=id)

        elif informacao_voo == '2': #alteração da data de saída do voo
            data_saida = input('Informe a nova data de saída do voo: ')
            atualiza_tabela(tabela='voos', campo='data_saida', valor=data_saida, id_registro=id)

        elif informacao_voo == '3': #alteração da data de chegada do voo
            data_chegada = input('Informe a nova data de chegada do voo: ')
            atualiza_tabela(tabela='voos', campo='data_chegada', valor=data_chegada, id_registro=id)

        elif informacao_voo == '4': #alteração do número de passageiros do voo
            passageiros = input('Informe o novo número de passageiros do voo: ')
            atualiza_tabela(tabela='voos', campo='numero_passageiros', valor=passageiros, id_registro=id)

        elif informacao_voo == '5': #alteração do número de assentos do voo
            assentos = input('Informe o novo número de assentos do voo: ')
            atualiza_tabela(tabela='voos', campo='assentos_voo', valor=assentos, id_registro=id)

        elif informacao_voo == '6': #alteração da carga carregada do voo
            carga = input('Informe a nova carga carregada do voo: ')
            atualiza_tabela(tabela='voos', campo='carga_carregada', valor=carga, id_registro=id)

        elif informacao_voo == '7': #alteração do código da empresa
            cod_empresa = input('Informe o novo código da empresa: ')
            query_verifica_empresa = (f'SELECT id FROM empresas '
                                      f'WHERE empresas.codigo_empresa = "{cod_empresa}"  ')
            cursor.execute(query_verifica_empresa)
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                atualiza_tabela(tabela='voos', campo='cod_empresa', valor=cod_empresa, id_registro=id)
            else:
                print('Não é possível atualizar o registro. Código da empresa não encontrado.')

        elif informacao_voo == '8': #alteração do código da aeronave
            cod_aeronave = input('Informe o novo código da aeronave: ')
            query_verifica_aeronave = (f'SELECT id FROM aeronaves '
                                       f'WHERE aeronaves.codigo_aeronave = "{cod_aeronave}"  ')
            cursor.execute(query_verifica_aeronave)
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                atualiza_tabela(tabela='voos', campo='cod_aeronave', valor=cod_aeronave, id_registro=id)
            else:
                print('Não é possível atualizar o registro. Código da aeronave não encontrado.')

        elif informacao_voo == '9': #alteração do código do aeroporto de decolagem
            aeroporto_decolagem = input('Informe o novo código do aeroporto de decolagem: ')
            query_verifica_decolagem = (f'SELECT id FROM aeroportos '
                                        f'WHERE aeroportos.codigo_aeroporto = "{aeroporto_decolagem}"  ')
            cursor.execute(query_verifica_decolagem)
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                atualiza_tabela(tabela='voos', campo='cod_aeroporto_decolagem', valor=aeroporto_decolagem, id_registro=id)
            else:
                print('Não é possível atualizar o registro. Código dao aeroporto não encontrado.')

        elif informacao_voo == '10': #alteração do código do aeroporto de decolagem
            aeroporto_destino = input('Informe o novo código do aeroporto de destino: ')
            query_verifica_destino = (f'SELECT id FROM aeroportos '
                                      f'WHERE aeroportos.codigo_aeroporto = "{aeroporto_destino}"  ')
            cursor.execute(query_verifica_destino)
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                atualiza_tabela(tabela='voos', campo='cod_aeroporto_destino', valor=aeroporto_destino, id_registro=id)
            else:
                print('Não é possível atualizar o registro. Código dao aeroporto não encontrado.')

elif acao == '3':
    exclusao = input('Que tipo de registro você deseja deletear? \n'
                      '1. Empresas \n'
                      '2. Aeronaves \n'
                      '3. Aeroportos \n'
                      '4. Voos \n')

    if exclusao == '1': #deletar empresas
        id = input('Informe o ID da empresa que deseja deletar: ')
        query_verifica_empresa = (f'SELECT voos.id FROM voos '
                                  f'INNER JOIN (empresas) ON voos.cod_empresa = empresas.codigo_empresa '
                                  f'WHERE empresas.id = {id} ')
        cursor.execute(query_verifica_empresa)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            deleta_tabela('empresas', id)
        else:
            print('Não foi possível deletar o registro. Há um voo registrado dessa empresa.')

    elif exclusao == '2': #deletar aeronaves
        id = input('Informe o ID da aeronave que deseja deletar: ')
        query_verifica_aeronave = (f'SELECT voos.id FROM voos '
                                   f'INNER JOIN (aeronaves) ON voos.cod_aeronave = aeronaves.codigo_aeronave '
                                   f'WHERE aeronaves.id = {id} ')
        cursor.execute(query_verifica_aeronave)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            deleta_tabela('aeronaves', id)
        else:
            print('Não foi possível deletar o registro. Há um voo registrado dessa aeronave.')

    elif exclusao == '3': #deletar aeroportos
        id = input('Informe o ID do aeroporto que deseja deletar: ')
        query_verifica_aeroporto = (f'SELECT voos.id FROM voos '
                                    f'INNER JOIN (aeroportos) ON voos.cod_aeroporto_decolagem = aeroportos.codigo_aeroporto '
                                    f'WHERE aeroportos.id = {id} ')
        cursor.execute(query_verifica_aeroporto)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            deleta_tabela('aeroportos', id)
        else:
            print('Não foi possível deletar o registro. Há um voo registrado desse aeroporto.')

    elif exclusao == '4':
        id = input('Informe o ID do voo que deseja deletar: ')
        deleta_tabela('voos', id)

elif acao == '4':
    consulta = input('Que tipo de relatório você deseja gerar? \n'
                     '1. Por período \n'
                     '2. Por empresa \n'
                     '3. Por aeroporto \n')

    if consulta == '1': #relatório por período
        data_inicio = input('Informe a data de início para o relatório: ')
        data_fim = input('Informe a data final para o relatório: ')
        query_relatorio_periodo = (f'SELECT numero_passageiros, assentos_voo, numero_passageiros/assentos_voo, carga_carregada FROM voos '
                                   f'WHERE data_saida BETWEEN "{data_inicio}" AND "{data_fim}" ')
        cursor.execute(query_relatorio_periodo)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

    elif consulta == '2': #relatório por empresa
        id = input('Informe o ID da empresa para o relatório: ')
        query_relatorio_empresa = (f'SELECT numero_passageiros, assentos_voo, numero_passageiros/assentos_voo, carga_carregada FROM voos '
                                   f'INNER JOIN (empresas) ON voos.cod_empresa = empresas.codigo_empresa '
                                   f'WHERE empresas.id = "{id}" ')
        cursor.execute(query_relatorio_empresa)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

    elif consulta == '3': #relatório por aeroporto
        id = input('Informe o ID do aeroporto para o relatório: ')
        query_relatorio_aeroporto = (f'SELECT numero_passageiros, assentos_voo, numero_passageiros/assentos_voo, carga_carregada FROM voos '
                                     f'INNER JOIN (aeroportos) ON voos.cod_aeroporto_decolagem = aeroportos.codigo_aeroporto '
                                     f'WHERE aeroportos.id = "{id}" ')
        cursor.execute(query_relatorio_aeroporto)
        resultado = cursor.fetchall()
        imprimir_registros(resultado)

cursor.close()
conexao.close()