class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mostrar_lados(self):
        return f' O retângulo tem {self.comprimento} cm de comprimento e {self.largura} cm de largura'

    def calcular_area(self):
        return f'A área é {self.comprimento * self.largura} cm²'

    def calcular_perimetro(self):
        return f'O perímetro é {2*(self.comprimento + self.largura)} cm'

retangulo1 = Retangulo(6, 4)

retangulo1.mudar_lados(8,5)
print(retangulo1.mostrar_lados())
print(retangulo1.calcular_area())
print(retangulo1.calcular_perimetro())

#faltou fazer a última parte