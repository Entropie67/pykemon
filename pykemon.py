class Pokemon:

    def __init__(self, nom1, nom2, nom3, power, hp, exp=0):
        self.stade = (exp//1000) % 3
        self.noms = [nom1, nom2, nom3, "Méga-"+nom3]
        self.nom = self.noms[self.stade]
        self.power = power
        self.hp = hp
        self.exp = exp
        self.type = "plante"


    def _evolution(self):

        if self.stade >= 2:
            print(f"{self.nom} ne peut plus évoluer. Sa puissance est au max")
        else:
            print("\n *** Evolution *** \n")
            print(f"Votre{self.nom} devient un {self.noms[self.stade]}")
            print(" \n ***           *** \n")
            self.nom = self.noms[self.stade]

    def add_xp(self, exp):
        self.exp += exp
        if self.stade != (exp//1000) % 3:
            self.stade = (exp//1000) % 3
            self._evolution()



 ############################
 # TEST
 ###########################

abra = Pokemon("Abra", "Kadabra", "Alakazam", 1000, 100)

print(abra.nom)
abra.add_xp(1000)
print(abra.nom)