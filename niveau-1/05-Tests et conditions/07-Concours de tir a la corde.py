nbMembres = int(input())

poidTotalEquipe1 = 0
poidTotalEquipe2 = 0

for loop in range(nbMembres):
  poidTotalEquipe1 = poidTotalEquipe1 + int(input())
  poidTotalEquipe2 = poidTotalEquipe2 + int(input())

if poidTotalEquipe1 > poidTotalEquipe2:
  print("L'équipe 1 a un avantage")
else:
  print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 :" , poidTotalEquipe1)
print("Poids total pour l'équipe 2 :" , poidTotalEquipe2)