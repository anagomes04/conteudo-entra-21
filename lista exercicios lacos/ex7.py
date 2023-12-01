times = ['São Paulo', 'Santos', 'Red Bull Bragantino', 'Palmeiras', 'Juventude', 'Internacional', 'Goiás', 'Fortaleza', 'Fluminense', 'Flamengo', 'Cuiabá', 'Coritiba', 'Corinthians', 'Ceará', 'Botafogo', 'Avaí', 'Atlético Mineiro', 'Atlético Goianiense', 'Athletico Paranaense', 'América Mineiro']

for i in times:
    for j in times:
        if i != j:
            print(f'{i} [] X [] {j}')
