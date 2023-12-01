class Console:
    #método contrutor
    def __init__(self, midia, marca, cor, controles, ligado=False, jogo=''):
        self.midia = midia
        self.marca = marca
        self.cor = cor
        self.controles = controles
        self.ligado = ligado
        self.jogo = jogo

#atributos

    def ligar(self):
        self.ligado = True
        # print(f'Ligando videogame marca {self.marca}')

    def desligar(self):
        self.ligado = False
        # print(f'Desligando videogame marca {self.marca}')

    def mostrar_marca(self):
        return self.marca

    def adicionar_controle(self, quantidade):
        self.controles += quantidade

    def trocar_cor(self, cor):
        self.cor = cor

    def inserir_jogo(self, nome_jogo):
        self.jogo = nome_jogo

#métodos ou funções

# console1 = Console('DVD', 'Sony', 'Preto', 2)
# console2 = Console('Bluray', 'Sony', 'Branco', 1)
# console3 = Console('Fita', 'Nintendo', 'Branco', 1)
#
# console1.ligar()
# console3.ligar()
# console3.desligar()
#
# print(console1.cor)
# print(console2.cor)

console1 = Console('DVD', 'Microsoft', 'Preto', 2)
print(console1.ligado)
console1.ligar()
print(console1.ligado)
print(console1.mostrar_marca())
console1.adicionar_controle(3)
print(console1.controles)
console1.trocar_cor('rosa')
print(console1.cor)
console1.inserir_jogo('Call of Duty')
print(console1.jogo)

#modifique os atributos por meio das funções

