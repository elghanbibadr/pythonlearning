class Membre:
    def __init__(self, nom, adresse, maxlivresemprunte):
        self.nom = nom
        self.adresse = adresse
        self.maxlivresemprunte = maxlivresemprunte

    def __str__(self):
        return "Nom: " + self.nom + ", Adresse: " + self.adresse + ", Max Livres Empruntables: " + str(self.maxlivresemprunte)




