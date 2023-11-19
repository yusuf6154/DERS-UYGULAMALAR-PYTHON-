from datetime import *

today = date.today()
print ("today:",today)
# dd/mm/YY
cevrilmisToday = today.strftime("%d / %m / %Y")
print ("Çevrilmiş şekli =",cevrilmisToday)

# gun = today.strftime("%d")
# ay = today.strftime("%m")
# print("Gün:",gun)
# print("Ay:",ay)