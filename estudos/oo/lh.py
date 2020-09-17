norte = 'Norte'
leste = 'Leste'
sul = 'Sul'
oeste = 'Oeste'


class Carro:
    def __init__ (self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()


class Motor:
    def __init__ (self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0, self.velocidade)

class Direcao:
    direcoes_direita = {norte: leste, leste: sul, sul: oeste, oeste: norte}
    direcoes_esquerda = {norte: oeste, oeste: sul, sul: leste, leste: norte}

    def __init__(self):
        self.valor = norte

    def girar_a_direita(self):
        self.valor = self.direcoes_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.direcoes_esquerda[self.valor]

if __name__ ==  '__main__':
    carro = Carro(norte, 0)
    direcao = Direcao()
    print(direcao.valor)
    
    # print(carro.calcular_velocidade)
    # carro.acelerar
    # carro.girar_a_esquerda
    # print(carro.calcular_direcao)
    # print(carro.calcular_velocidade)