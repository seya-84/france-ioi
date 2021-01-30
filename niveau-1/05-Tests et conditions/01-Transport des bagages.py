nbPaquets = int(input())
poidsPaquet = int(input())

poidTotal = nbPaquets * poidsPaquet
poidMaxi = 105

if poidTotal > poidMaxi:
  print('Surcharge !')