class Pokemon:

    def __init__(self, nom1, nom2, nom3, power, hp, exp=0):
        self.stade = (exp//1000)
        self.noms = [nom1, nom2, nom3, "Méga-"+nom3]
        self.nom = self.noms[self.stade if self.stade <= 4 else 4]
        self.power = power
        self.hp = hp
        self.exp = exp
        self.type = "plante"


    def _evolution(self):


        print("\n *** Evolution *** \n")
        print(f"Votre{self.nom} devient un {self.noms[self.stade if self.stade <= 3 else 3]}")
        print(" \n ***           *** \n")
        self.nom = self.noms[self.stade if self.stade <= 3 else 3]

    def add_xp(self, exp):
        self.exp += exp
        if self.stade != (exp//1000):
            print(self.stade)
            self.stade = (exp//1000)
            print(self.stade)
            self._evolution()



 ############################
 # TEST
 ###########################

abra = Pokemon("Abra", "Kadabra", "Alakazam", 1000, 100)

print(abra.nom)
abra.add_xp(6000)
print(abra.nom)