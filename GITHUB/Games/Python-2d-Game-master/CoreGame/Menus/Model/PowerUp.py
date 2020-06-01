




class PowerUp():
    def __init__(self,image,valor,tipo,preco):
        self.image = image
        self.valor = valor
        self.tipo = tipo
        self.preco = preco


    def getimage(self):
        return self.image

    def setimage(self,image):
        self.image = image

    def getvalor(self):
        return self.valor

    def setvalor(self, valor):
        self.valor = valor

    def gettipo(self):
        return self.tipo

    def settipo(self, tipo):
        self.tipo = tipo

    def getpreco(self):
        return self.preco

    def setpreco(self, preco):
        self.preco = preco