meyveler = ["elma","armut","kiraz"]


eleman = input("meyve ekleyınız:")
meyveler.insert(3,eleman)
print(meyveler)#eklenecek meyveyi 3. sıraya ekler.

print(meyveler)
meyveler.pop()
print(meyveler)
print("pop ile silinmiş:",meyveler)

meyveler.sort()
print("sort ile sıralanmıs:",meyveler)#alfabetik sıraya dizer.
meyveler.reverse()
print("reverse ile ters cevrilmis:",meyveler)#alfabetik sıralanmıs dızıyı ters yazar.
