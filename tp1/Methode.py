from Vila import Vila
from Appartement import Appartement
from Imobilier import Imobilier
import pickle
class Methode:
  imobilier=[]

  def creéImobilier(self):
    app1=Appartement("appartement 1","marrakeche 1","27992m","7837dh")
    app2=Appartement("appartement 2","marrakeche 1","292m","3788dh") 
    vila1=Vila("vila 1","marrakeche 1","4684m","4939839dh","7388") 
    self.imobilier.append(app1)
    self.imobilier.append(app2)
    self.imobilier.append(vila1)

  
  def afficherTout(self):
      for i in range(len(self.imobilier)) :
       print(self.imobilier[i].__str__())
  

  def verifier(self,obj):
    if(isinstance(obj,Imobilier)):
      return True
    
    return False
  
  
  def afficheAppartement(self):
    for i in range(len(self.imobilier)):
        if isinstance(self.imobilier[i], Appartement):
            print(self.imobilier[i].__str__())


  def sauvgardefichierobjet(self):
     f=open("imobilier.pkl",'ab')
     for i in range(len(self.imobilier)):
        pickle.dump(self.imobilier[i],f)
     print("donne sauvgardé avec succes")
    
  def lirefichierobjet(self):
    f=open("imobilier.pkl",'rb')
    for i in range(len(self.imobilier)):
     pickle.load(self.imobilier[i],f)
     
     