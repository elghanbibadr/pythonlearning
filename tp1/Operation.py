
from Employe import Emp

class Operation:
    lemp=[]
   
    def ajouteremplye(self):
        name=input("entre le name")
        cin=input("entre le cin")
        salaire=float(input("entre le salaire"))
        prenom=input("entre le prenom")
        jour=int(input('entre le jour'))
        mois=int(input('entre le mois'))
        anne=int(input('entre l annee'))
        e=Emp(name,cin,salaire,prenom,jour,mois,anne)
        self.lemp.append(e)
    
    def affchee(self):
        for i in range(len(self.lemp)):
         print(self.lemp[i].__str__())

    # def triepardate(self):
        