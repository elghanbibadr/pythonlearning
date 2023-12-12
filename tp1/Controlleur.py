from Vila import Vila
from Appartement import Appartement

class Controlleur:
   
    vilas=[]
    appartements=[]

 
    def ajouterapp(self) :
       titre=input('entre le titre de appartement :')
       address=input('entre l adress de appartement :')
       prix=input('entre le prix de appartement :')
       perimetre=float(input('entre le perimetre de appartement :'))
       perimetre=int(input('entre le nbj de appartement :'))
       app1=Appartement(titre,address,prix,perimetre)
       return self.vilas.append(app1)

    def afficherapp(self):
         return self.vilas


