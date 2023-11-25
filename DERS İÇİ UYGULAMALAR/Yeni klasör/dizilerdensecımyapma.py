meyveler = [["elma","armut","kiraz"]]
corbalar = [["mercimek",40],["lahana",50],["tarhana",45]]
yemekler = [["tavuk sote",85],["orman kebabı",110],["iskender",135]]
tutar = 0

import random
print("           MENU TAVSIYESI                ")
x = random.randint(0,len(corbalar)-1)
print(corbalar[x][0],"(fiyatı:",corbalar[x][1])
tutar += corbalar[x][1]

xx = random.randint(0,len(yemekler)-1)
print(yemekler[xx][0],"(fiyatı:",yemekler[xx][1])
tutar += yemekler[xx][1]

