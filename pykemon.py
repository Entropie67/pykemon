class Pokemon:

    def __init__(self, nom1, nom2, nom3, power, hp, exp=0):
        self.stade = 0
        self.noms = [nom1, nom2, nom3]
        self.nom = self.noms[self.stade]
        self.power = power
        self.hp = hp
        self.exp = exp


    def evolution(self):
        if self.stade >= 2:
            print(f"{self.nom} ne peut plus évoluer. Sa puissance est au max")


