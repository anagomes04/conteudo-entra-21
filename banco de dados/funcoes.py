import mysql.connector
import pandas as pd
from tabulate import tabulate

conexao = mysql.connector
cursor = None


def conectar_banco():
    global conexao, cursor
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='anac'
    )
    cursor = conexao.cursor()


def encerrar_conexao():
    global conexao, cursor
    if conexao is not None and cursor is not None:
        cursor.close()
        conexao.close()


def inserir_empresa(nome, nacionalidade):
    conectar_banco()
    global conexao, cursor
    query = 'INSERT INTO empresas(nome, nacionalidade) VALUES (%s, %s)'
    dados = nome, nacionalidade
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def inserir_aeronave(modelo, assentos, limite_bagagem):
    conectar_banco()
    global conexao, cursor
    query = 'INSERT INTO aeronaves(modelo, assentos, limite_bagagem) VALUES (%s, %s, %s)'
    dados = modelo, assentos, limite_bagagem
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def inserir_aeroporto(nome, sigla, cidade, estado, pais, continente):
    conectar_banco()
    global conexao, cursor
    query = 'INSERT INTO aeroportos(nome, sigla, cidade, estado, pais, continente) VALUES (%s, %s, %s, %s, %s, %s)'
    dados = nome, sigla, cidade, estado, pais, continente
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def inserir_voo(data_partida, data_chegada, cod_aeroporto_decolagem, cod_aeroporto_destino, cod_empresa, passageiros, assentos, carga, cod_aeronave):
    conectar_banco()
    global conexao, cursor
    query = ('INSERT INTO voos (data_partida, data_chegada, cod_aeroporto_decolagem, cod_aeroporto_destino, '
             'cod_empresa, passageiros, assentos, carga, cod_aeronave) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')
    dados = data_partida, data_chegada, cod_aeroporto_decolagem, cod_aeroporto_destino, cod_empresa, passageiros, assentos, carga, cod_aeronave
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def atualizar_empresa(id, novo_nome, nova_nacionalidade):
    conectar_banco()
    global conexao, cursor
    query = 'UPDATE empresas SET nome=%is, naconalidade=%s WHERE id=%s'
    dados = (novo_nome, nova_nacionalidade, id)
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def atualizar_aeronave(id, novo_modelo, novos_assentos, novo_limite_bagagem):
    conectar_banco()
    global conexao, cursor
    query = 'UPDATE aeronaves SET modelo=%s, assentos=%s, limite_bagagem=%s WHERE id=%s'
    dados = (novo_modelo, novos_assentos, novo_limite_bagagem, id)
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def atualizar_aeroporto(id, novo_nome, nova_sigla, nova_cidade, novo_estado, novo_pais, novo_continente):
    conectar_banco()
    global conexao, cursor
    query = 'UPDATE aeroportos SET nome=%s, sigla=%s, cidade=%s, estado=%s, pais=%s, continente=%s WHERE id=%s'
    dados = (novo_nome, nova_sigla, nova_cidade, novo_estado, novo_pais, novo_continente, id)
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def desativar_empresa(id):
    conectar_banco()
    global conexao, cursor
    query = 'UPDATE empresas SET Ativo=False WHERE id=%s'
    dados = (id,)
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def desativar_aeroporto(id):
    conectar_banco()
    global conexao, cursor
    query = 'UPDATE aeroportos SET Ativo=False WHERE id=%s'
    dados = (id,)
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def desativar_aeronave(id):
    conectar_banco()
    global conexao, cursor
    query = 'UPDATE aeronaves SET Ativo=False WHERE id=%s'
    dados = (id,)
    cursor.execute(query, dados)
    conexao.commit()
    encerrar_conexao()


def filtro_por_periodo():
    conectar_banco()
    global conexao, cursor
    query = """
        SELECT 
            MONTH(data_partida) as mes,
            SUM(passageiros) AS total_passageiros,
            SUM(assentos) AS total_assentos,
            SUM(passageiros) / SUM(assentos) AS ocupacao_media,
            SUM(carga) AS carga_total
        FROM 
            voos
        GROUP BY 
            mes
        ORDER BY 
            mes;
    """
    cursor.execute(query,)
    resultados = cursor.fetchall()
    resultados = pd.DataFrame(resultados)
    print(tabulate(resultados,
                   headers=['Mês', 'total_passageiros', 'total_assentos', 'ocupacao_media', 'carga_total'], showindex=False))
    encerrar_conexao()
    return resultados


def filtro_por_empresa():
    conectar_banco()
    global conexao, cursor
    query = """
        SELECT 
            empresas.nome as empresa,
            SUM(passageiros) AS total_passageiros,
            SUM(assentos) AS total_assentos,
            SUM(passageiros) / SUM(assentos) AS ocupacao_media,
            SUM(carga) AS carga_total
        FROM 
            voos
        INNER JOIN empresas ON empresas.id = voos.cod_empresa

        GROUP BY 
            empresa
        ORDER BY 
            empresa;
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    resultados = pd.DataFrame(resultados)
    print(tabulate(resultados,
                   headers=['aeroporto', 'total_passageiros', 'total_assentos', 'ocupacao_media', 'carga_total'], showindex=False))
    encerrar_conexao()
    return resultados


def filtro_por_aeroporto():
    conectar_banco()
    global conexao, cursor
    query = """
        SELECT 
            aeroportos.nome as aeroporto,
            SUM(passageiros) AS total_passageiros,
            SUM(assentos) AS total_assentos,
            SUM(passageiros) / SUM(assentos) AS ocupacao_media,
            SUM(carga) AS carga_total
        FROM 
            voos
        INNER JOIN aeroportos ON aeroportos.id = voos.cod_aeroporto_decolagem

        GROUP BY 
            aeroporto
        ORDER BY 
            aeroporto;
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    resultados = pd.DataFrame(resultados)
    print(tabulate(resultados,
                   headers=['aeroporto', 'total_passageiros', 'total_assentos', 'ocupacao_media', 'carga_total'], showindex=False))
    encerrar_conexao()
    return resultados


anac = r"""

 █████  ███    ██  █████   ██████ 
██   ██ ████   ██ ██   ██ ██      
███████ ██ ██  ██ ███████ ██      
██   ██ ██  ██ ██ ██   ██ ██      
██   ██ ██   ████ ██   ██  ██████                                                               
"""
