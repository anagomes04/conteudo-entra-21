class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cor):
        self.cor = cor

    def mostrar_cor(self):
        return self.cor

bola1 = Bola('verde', 3.14, 'plastico')

bola1.trocar_cor('rosa')
print(bola1.mostrar_cor())