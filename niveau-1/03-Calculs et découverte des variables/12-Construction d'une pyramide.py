totalCubes = 0
largeurArête = 1
for loop in range(9):
   totalCubes = totalCubes + largeurArête**3
   largeurArête = largeurArête + 2
print(totalCubes)