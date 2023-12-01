import PySimpleGUI as sg
import os
from funcoes import baixar_video, baixar_audio, baixar_varios_audios, baixar_varios_videos

pasta_salvar = r"C:\Users\ana.gomes11\PycharmProjects\ana\exercicio_youtube\YoutubeDownloader"

# link = "https://www.youtube.com/watch?v=vEO_g33pXdI&list=PLZviiKCGlZaAJfFGkS1ChmubUp6_6rbDw&index=14"

# links = open(r"C:\Users\ana.gomes11\PycharmProjects\ana\exercicio_youtube\links_videos.txt")

sg.theme('DarkAmber')

layout = [
    [sg.Image('imagens/icone_youtube.png'), sg.Text('Youtube Downloader')],
    [sg.Text('Download único  '), sg.Input('', key='link')],
    [sg.Text('Download via .txt'), sg.Input('', key='arquivo_text'), sg.FileBrowse('\/')],
    [sg.Checkbox('', key='check'), sg.Text('Apenas aúdio')],
    [sg.Button('Download agora'), sg.Button('Pasta destino')]
]

window = sg.Window('Youtube Downloader', layout)

while True:
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED:
        break

    elif evento == 'Pasta destino':
        caminho = r"C:\Users\ana.gomes11\PycharmProjects\ana\exercicio_youtube\YoutubeDownloader"
        os.startfile(caminho)
        break

    elif evento == 'Download agora':
        baixar_video(valores['link'])


#casos:
#download único vídeo
#download único aúdio
#download vários vídeos
#download vários aúdios

window.close()