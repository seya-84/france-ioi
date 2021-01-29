positionDepart = int(input(10))
largeurEmplacement = int(input(5)) 
nbVendeurs = int(input(3))

print(positionDepart)

for loop in range (nbVendeurs):
   positionDepart = positionDepart + largeurEmplacement
   print(positionDepart)