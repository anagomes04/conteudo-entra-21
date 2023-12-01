import funcoes as fn


print(fn.anac)
todas_funcoes = {'1': ['nome', 'nacionalidade', fn.inserir_empresa],
                 '2': ['nome', 'sigla', 'cidade', 'estado', 'pais', 'continente', fn.inserir_aeroporto],
                 '3': ['modelo', 'assentos', 'limite_bagagem', fn.inserir_aeronave],
                 '4': ['data_partida', 'data_chegada', 'cod_aeroporto_decolagem', 'cod_aeroporto_destino', 'cod_empresa', 'passageiros', 'assentos', 'carga', 'cod_aeronave', fn.inserir_voo],
                 '5': fn.filtro_por_empresa,
                 '6': fn.filtro_por_aeroporto,
                 '7': fn.filtro_por_periodo
                 }


while True:
    print("""
[1] CADASTRAR EMPRESA
[2] CADASTRAR AEROPORTO
[3] CADASTRAR AERONAVE
[4] CADASTRAR VOO
[5] FILTRO POR EMPRESA
[6] FILTRO POR AEROPORTO
[7] FILTRO POR PERÍODO""")

    opcao = input('Qual opção desejada:')
    dados = []

    if opcao in todas_funcoes:
        if opcao in '567':
            todas_funcoes[opcao]()
        else:
            for atributo in todas_funcoes[opcao][:-1]:
                dados.append(input(f'{atributo}: '))
            try:
                todas_funcoes[opcao][-1](*dados)
            except:
                print('Erro recebido.')



