heureArrivee = int(input())
prixChambreMaxi = 53

prix = heureArrivee * 5 + 10

if prix > prixChambreMaxi:
  print(prixChambreMaxi)
if prix < prixChambreMaxi:
  print(prix)