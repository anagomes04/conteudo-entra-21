class Bomba:
    def __init__(self, tipo, valor_litro, valor_abastecer, quantidade_abastecida, total_bomba):
        self.tipo = tipo
        self.valor_litro = valor_litro
        self.valor_abastecer = valor_abastecer
        self.quantidade_abastecida = quantidade_abastecida
        self.total_bomba = total_bomba

    def trocar_combusivel(self, tipo):
        self.tipo = tipo

    def mostrar_tipo(self):
        return f'O tipo de combustível é {self.tipo}'

    def mudar_valor(self, valor_litro):
        self.valor_litro = valor_litro

    def mostrar_valor_litro(self):
        return f'O valor do combustível por litro é {self.valor_litro}'

    def mudar_total(self, quantidade_abasecida):
        self.quantidade_abastecida = quantidade_abasecida
        self.total_bomba = self.total_bomba - self.quantidade_abastecida

    def mostrar_total(self):
        return f'Restam na bomba {self.total_bomba} litros de combustível'

    def mostrar_quantidade_abastecida(self):
        return f' A quantidade abastecida foi de {self.quantidade_abastecida} litros.'

    def abastecer_valor(self, valor_abastecer):
        self.valor_abastecer = valor_abastecer
        self.quantidade_abastecida = self.valor_abastecer / self.valor_litro
        return f'O valor pago é de {self.valor_abastecer}, foram abastecidos {self.valor_abastecer / self.valor_litro} litros.'

    def abastecer_litro(self, quantidade_abastecida):
        self.quantidade_abastecida = quantidade_abastecida
        self.valor_abastecer = self.quantidade_abastecida * self.valor_litro
        return f'Foram abastecidos {self.quantidade_abastecida} litros, o valor a pagar é de {self.quantidade_abastecida * self.valor_litro} reais.'

bomba1 = Bomba('gasolina', 5.99, 50, 8.3, 100)

bomba1.trocar_combusivel('etanol')
print(bomba1.mostrar_tipo())

bomba1.mudar_valor(6.09)
print(bomba1.mostrar_valor_litro())

bomba1.mudar_total(16)
print(bomba1.mostrar_total())
print(bomba1.mostrar_quantidade_abastecida())

print(bomba1.abastecer_valor(50))

print(bomba1.abastecer_litro(10))