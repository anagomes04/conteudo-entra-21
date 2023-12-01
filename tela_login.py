import PySimpleGUI as sg

sg.theme('DarkTeal4')

layout = [
            [sg.Text('Usuário')],
            [sg.Input(key='usuario')],
            [sg.Text('Senha')],
            [sg.Input(key='senha')],
            [sg.Button('Login')],
            [sg.Text(key='mensagem')],
]

window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event =='login':
        usuario_correto = 'ana.gomes11'
        senha_correta = '12345'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Loging feito com sucesso')
        elif senha != senha_correta or usuario != usuario_correto:
            window['mensagem'].update('Não foi possível fazer o login. Usuário ou senha incorretos.')