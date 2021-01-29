nbKarva = int(input())# 2

for loop in range(nbKarva):
   poid = int(input())# 100 kg PREMIER KARVA a passer dans la boucle
   age = int(input())# 5 ans
   cornes = int(input())# 25 cm
   garrot = int(input())# 90 cm
   note = cornes * garrot + poid
   
   print(note)