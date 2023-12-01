class Macaco:
    def __init__(self, nome, comida, total, quantidade_engolida, quantidade_digerida):
        self.nome = nome
        self.comida = comida
        self.total = total
        self.quantidade_engolida = quantidade_engolida
        self.quantidade_digerida = quantidade_digerida

    def mostrar_nome(self):
        return f'O nome é {self.nome}'

    def comer(self, quantidade_engolida, comida):
        self.quantidade_engolida = quantidade_engolida
        self.comida = comida
        self.total = self.total + self.quantidade_engolida

    def mostrar_quantidade_engolida(self):
        return self.quantidade_engolida

    def digerir(self, quantidade_digerida):
        self.quantidade_digerida = quantidade_digerida
        self.total = self.total - self.quantidade_digerida

    def mostrar_quantidade_digerida(self):
        return self.quantidade_digerida

    def mostrar_total(self):
        return self.total

    def mostrar_comida(self):
        return self.comida

macaco1 = Macaco('bob', 'banana', 50, 10, 6)
macaco2 = Macaco('fred', 'alface', 50, 10, 6)

print(macaco2.mostrar_nome())

macaco1.comer(10, 'alface')
print(macaco1.mostrar_comida())
print(macaco1.quantidade_engolida)
print(macaco1.mostrar_total())

macaco2.digerir(10)
print(macaco2.quantidade_digerida)
print(macaco2.total)

macaco2.comer(100, 'macaco1')
print(macaco2.comida)