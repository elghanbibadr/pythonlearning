# class Rectangle:
#     def __init__(self,lng,lar) :
#        self.lng=lng
#        self.lar=lar
    
#     def perimetre(self):
#         return (self.lng + self.lar) * 2
    
#     def superficie(self):
#         return (self.lng + self.lar) * 2
    


# rec1=Rectangle(7,8)

# print(rec1.perimetre())
# print(rec1.superficie())




# # LIVRE



# class Livre :

#   def __init__(self,titre, auteur, annee,dispo):
#       self.lng=titre
#       self.lar=auteur
#       self.annee=annee
#       self.dispo=dispo

#   def emprunte(self):
#       return self.dispo==True
  
#   def retourne(self):
#       return self.dispo==False
  

# class Biblio:
#     def __init__(self,livres):
#         self.livres=[]

#     def mesLivres(self):
#       for livre in self.livres:
#           if livre.dispo==True:
#               return livre
          

# biblio=Biblio([])

# biblio.livres.append(Livre("the secret","john","1999",True))


# print(biblio.mesLivres())