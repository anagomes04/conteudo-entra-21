from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import os

pasta_salvar = r"C:\Users\ana.gomes11\PycharmProjects\ana\exercicio_youtube\YoutubeDownloader"

# link = "https://www.youtube.com/watch?v=vEO_g33pXdI&list=PLZviiKCGlZaAJfFGkS1ChmubUp6_6rbDw&index=14"
#
# links = open(r"C:\Users\ana.gomes11\PycharmProjects\ana\exercicio_youtube\links_videos.txt")

def baixar_video(link):
    try:
        yt = YouTube(link)
        mp4 = yt.filter('mp4')
        d_video = yt.get(mp4[-1].extension, mp4[-1].resolution)
        d_video.download(pasta_salvar)
    except:
        return f'Erro de conexão'

    return 'Download feito com sucesso'

def baixar_varios_videos(arquivo_txt):
    for i in links:
        try:
            yt = YouTube(i)
            yt.download(pasta_salvar)
        except VideoUnavailable:
            print('Erro de conexão')
    return 'Download feito com sucesso'

def baixar_audio(link):
    try:
        yt = YouTube(link)
        t = yt.streams.filter(only_audio=True)
        t[0].download(pasta_salvar)
    except:
        print('Erro de conexão')
    return 'Download feito com sucesso'

def baixar_varios_audios(arquivo_txt):
    for i in links:
        try:
            yt = YouTube(i)
            t = yt.streams.filter(only_audio=True).all()
            t[0].download(pasta_salvar)
        except VideoUnavailable:
            print('Erro de conexão')
    return 'Download feito com sucesso'

