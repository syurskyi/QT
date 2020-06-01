from CoreGame.Menus.Model.PowerUp import PowerUp


class ServPowerUp():
    def __init__(self):
        self.arpw = []
        self.mockupdata()

    def addpw(self,image,valor,tipo,preco):
        self.arpw.append(PowerUp(image,valor,tipo,preco))

    def getpw(self):
        return self.arpw


    def mockupdata(self):
        self.addpw('lifeimg.png',100,0,1000) #dividir a vida por 100
        self.addpw('lifeimg.png', 200, 0,2000)
        self.addpw('lifeimg.png', 300, 0,3000)
        self.addpw('velimg.png', 5, 1,1000) #dividir a vida por 10
        self.addpw('velimg.png', 10, 1,2000)
        self.addpw('velimg.png', 20, 1,3000)
        self.addpw('shootimg.png', 20, 2,1000)  #dividir por 10
        self.addpw('shootimg.png', 40, 2,2000)
        self.addpw('shootimg.png', 60, 2,3000)
