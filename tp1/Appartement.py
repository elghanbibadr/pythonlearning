from Imobilier import Imobilier

class Appartement(Imobilier):
    prix:float
    nbj:int
    
    def __init__(self, titre, address, superficie,prix,nbj=0):
        super().__init__(titre, address,superficie)
        self.prix = prix
        self.nbj = nbj
      

    def totalprix(self):
        return self.nbj * self.prix
    
    def str(self):
        if f"{self.nbj}" == 0 :
            return "appartment ",super().str() , "et disponible"
        
        return "appartment ",super().str() , "et reserve" 