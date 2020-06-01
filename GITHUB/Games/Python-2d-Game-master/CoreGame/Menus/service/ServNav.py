
from CoreGame.Menus.Model.Nav import NAV
from CoreGame import Settings

class ServNav():
    def __init__(self):
        self.arnavs = []
        self.mockupdata()

    def addnav(self,preco,vel,disp,life):
        self.arnavs.append(NAV(preco,vel,disp,life))

    def getnavs(self):
        return self.arnavs


    def mockupdata(self):
        self.addnav(0,30,80,1000)
        self.addnav(2000, 50, 130, 600)
        self.addnav(4000, 40, 180, 800)
