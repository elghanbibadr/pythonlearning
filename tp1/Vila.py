from Imobilier import Imobilier
class Vila(Imobilier):
       prix:float
       nbj:int
       caution:float

       def __init__(self, titre, address, superficie,prix,caution,nbj=0):
        super().__init__(titre, address,superficie)
        self.prix = prix
        self.nbj = nbj
        self.caution = caution
      

       def totalprix(self):
        return self.nbj * self.prix + self.caution
    
       def str(self):
        if f"{self.nbj}" == 0 :
            return "appartment ",super().str() , "et disponible"
        
        return "appartment ",super().str() , "et reserve" 