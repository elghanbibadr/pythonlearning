class Maison:
        prix:float
        adress:int
        etages:int

        def __init__(self, address, etages,prix):
         self.prix = prix
         self.etages = etages
         self.adress = address
      

        def toString(self):
         return self.adress + self.prix + self.etages
    