
class Livre:
   

   def __init__(self,livre,auteur,anne):
      self.livre=livre
      self.auteur=auteur
      self.anne=anne

   def afficheinfo(self):
      return self.livre + self.auteur + self.anne
   



