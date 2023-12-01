# criar uma classe chamada veiculo
# a classe deve ter os seguintes atributos:
# - proprietario
# - ano
# -modelo
# -marca
# -cor
# -odometro
# e outros atributos que forem necessários para as funcionalidades:
# -mostrar proprietário
# -exibir descrição do veículo ex: Hyunday Tucson 2012
# -trocar cor do vaículo
# -ligar o veículo
# - desligar o veículo
#- fazer trajeto (informar a km)
# - mostrar odômetro
# - km faltantes para próxima troca de óleo (considerar troca a caa 10.000km)

class Veiculo:
    def __init__(self, proprietario, ano, modelo, marca, cor, odometro, ligado=False):
        self.proprietario = proprietario
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.ligado = ligado

    def mostrar_proprietario(self):
        return self.proprietario

    def descricao_veiculo(self):
        return f'{self.modelo} {self.marca} {self.ano}'

    def trocar_cor(self, cor):
        self.cor = cor

    def ligar(self):
        if self.ligado:
            return 'Carro já estava ligado'
        self.ligado = True
        return 'Carro ligado'

    def desligar(self):
        if self.ligado:
            return 'Carro está desligado'
        self.ligado = False
        return 'Carro já estava desligado'

    def mostrar_odometro(self):
        return self.odometro

    def trocar_oleo(self):
        return f'Troca de óleo em {10000 - (self.odometro % 10000)} km'

    def calcular_trajeto(self, trajeto):
        if self.ligado:
            self.odometro = self.odometro + trajeto
            return  f'Seu trajeto foi de {trajeto} km'
        else:
            return f'O carro está desligado'

veiculo1 = Veiculo('Francisco', 2018, 'Mobi', 'Fiat', 'Branco', 28000, True)
print(veiculo1.mostrar_proprietario())
print(veiculo1.descricao_veiculo())
veiculo1.trocar_cor('Preto')
print(veiculo1.cor)
veiculo1.ligar()
print(veiculo1.ligado)
veiculo1.desligar()
print(veiculo1.ligado)
print(veiculo1.mostrar_odometro())
print(veiculo1.trocar_oleo())
veiculo1.ligar()
print(veiculo1.odometro)
print(veiculo1.calcular_trajeto(40000))
print(veiculo1.odometro)
print(veiculo1.calcular_trajeto(100))