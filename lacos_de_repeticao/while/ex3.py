massa = float(input('Informe a massa do material: '))

massa_inicial = massa

tempo_segundos = 0

while massa >= 0.5:
    tempo_segundos += 1
    if tempo_segundos % 50 == 0:
        massa = massa/2


print(massa_inicial)
print(massa)
print(tempo_segundos)
print(tempo_minutos)

#tempo = tempo -tempo//60*60 -> para fazer minutos e segundo