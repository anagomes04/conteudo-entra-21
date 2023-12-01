import os
import shutil

def abre_documento(arquivo_docx):
    os.rename(arquivo_docx, arquivo_docx.replace('.docx', '.zip'))
    shutil.unpack_archive(arquivo_docx.replace('.docx', '.zip'), 'temp-modelo-contrato')
    with open('temp-modelo-contrato/word/document.xml', 'r') as arquivo_contrato:
        contrato = arquivo_contrato.read()
    return contrato

def criar_documento(contrato, nome):
    contrato_customizado = contrato.replace('NOME', nome)
    with open('temp-modelo-contrato/word/document.xml', 'w') as arquivo_contrato:
        arquivo_contrato.write(contrato_customizado)
    shutil.make_archive(f'CONTRATO - {nome}', 'zip', root_dir='temp-modelo-contrato')
    os.rename(f'CONTRATO - {nome}.zip', f'CONTRATO - {nome}.docx')