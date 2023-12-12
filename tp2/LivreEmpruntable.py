from Livre import Livre

class LivreEmpruntable(Livre):
  
  def __init__(self,auteur,anne,livre ,emprunte):
   super().__init__(auteur,anne,livre)
   self.emprunte =emprunte


  def emprunteLivre(self):
      self.emprunte=True
      print("vous aver empruntez : " + self.livre)


  def retourne(self):
      self.emprunte=False
      print("vous retourne : " + self.livre)