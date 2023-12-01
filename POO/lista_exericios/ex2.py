class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado

    def mostrar_lado(self):
        return f'O lado do quadrado é de {self.lado} cm'

    def calcular_area(self):
        return f'A área é {self.lado * self.lado} cm²'

    def calcular_perimetro(self):
        return f'O perímetro é {2*(self.lado + self.lado)} cm'

quadrado1 = Quadrado(10)

quadrado1.mudar_lado(8)
print(quadrado1.mostrar_lado())
print(quadrado1.calcular_area())
print(quadrado1.calcular_perimetro())