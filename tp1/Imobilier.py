class Imobilier :
   _titre:str
   _address:str
   _superficie:float
  
   def __init__(self,titre,address,superficie):
     self._titre=titre
     self._address=address
     self._superficie=superficie

   def str(self):
    return self._titre , " " , self._address , " " , self._superficie
   

   def getTitre(self):
     return self._titre
   
   def setTitre(self,titre):
      self._titre =titre

   def totalprix(self):
     pass
   
   