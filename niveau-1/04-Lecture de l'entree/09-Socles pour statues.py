largeurBas = int(input())# 7
largeurHaut = int(input())# 3
boucle = largeurBas - largeurHaut
volume = 0

for loop in range(boucle + 1):
  volume = volume + largeurBas * largeurBas
  largeurBas = largeurBas - 1
print(volume)