


class NAV():
    def __init__(self,preco,velocidade,disparo,vida):
        self.preco = preco
        self.velocidade = velocidade
        self.disparo = disparo
        self.vida = vida


    def getpreco(self):
        return self.preco

    def setpreco(self,preco):
        self.preco = preco

    def getvelocidade(self):
        return self.velocidade

    def setvelocidade(self, velocidade):
        self.velocidade = velocidade

    def getdisparo(self):
        return self.disparo

    def setdisparo(self, disparo):
        self.disparo = disparo

    def getvida(self):
        return self.vida

    def setvida(self, vida):
        self.vida = vida