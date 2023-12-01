import PySimpleGUI as sg
import os
import shutil
from docx2pdf import convert
import py7zr
from funcoes import abre_documento, criar_documento

sg.theme('Reddit')

layout = [
    [sg.Text('Contrato Padrão'), sg.Image('imagens/icone_word.png'), sg.InputText('', key='contrato'), sg.FileBrowse('\/')],
    [sg.Text('Base de Dados'), sg.Image('imagens/icone_csv.png'), sg.InputText('', key='base'), sg.FileBrowse('\/')],
    [sg.Text('Nome Arquivo'), sg.Image('imagens/icone_rar.png'), sg.InputText('', key='arquivo'), sg.FolderBrowse('\/')],
    [sg.Button('Executar'), sg.Button('Limpar Campos')],
    [sg.Text('', key='mensagem')]
]

window = sg.Window('Automação de Contrato', layout)

while True:
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'Limpar Campos':
        window['contrato'].update('')
        window['base'].update('')
        window['arquivo'].update('')
    elif evento == 'Executar':

        if not valores['contrato'] or not valores['base'] or not valores['arquivo']:
            window['mensagem'].update('Todos os campos devem ser preenchidos')

        elif not os.path.exists(valores['contrato']) or not os.path.exists(valores['base']):
            window['mensagem'].update('Caminho informado não existe')

        else:
            window['mensagem'].update('')
            with open(valores['base'], 'r') as arquivo_dados:
                dados = arquivo_dados.read()

            contrato = abre_documento(valores['contrato'])

            for nome in dados.splitlines()[1:]:
                criar_documento(contrato, nome)
                convert(f'CONTRATO - {nome}.docx', f'CONTRATO - {nome}.pdf')
                os.remove(f'CONTRATO - {nome}.docx')
                shutil.move(fr"CONTRATO - {nome}.pdf", valores['arquivo'])
                shutil.make_archive(f'Contratos_pdf', 'zip', root_dir=valores['arquivo'])

            os.rename(valores['contrato'].replace('.docx', '.zip'), valores['contrato'])
            shutil.rmtree('temp-modelo-contrato')
            sg.popup('concluido')


window.close()