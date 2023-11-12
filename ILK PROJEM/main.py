import adamAsmaca
import hesapMakinesi
import gectiKaldi
import aritmetikSayım
import cokgenCizme





def anaMenu():
  #print("\033[1;32;40m   \n")
  print("╔═══════════════════════════════════════════════════╗")
  #print("║\033[1;31;40m PYTHON PROJELER \033[1;32;40m               ║")
  print("║                    PYTHON PROJELER                ║")
  print("║                                                   ║")
  print("║ 1-Hesap makinesi                                  ║")
  print("║ 2-Adam Asmaca                                     ║")
  print("║ 3-Not Hesaplama                                   ║")
  print("║ 4-Aritmetik Sayım                                 ║")
  print("║ 5-Çokgen Çizme                                    ║") 
  print("║ 6-                                                ║")
  print("║ 7-                                                ║")
  print("║ 8-                                                ║")
  print("║ 9-                                                ║")
  print("║ 10-Çıkış(e)                                       ║")
  print("║ Seçiminiz Nedir?                                  ║")
  print("╚═══════════════════════════════════════════════════╝")
  secim = input()
  print("Seçiminiz Nedir?:", secim)
  if secim == "1":
    hesapMakinesi.hesapMakinesi()
    anaMenu()
  if secim == "2":
    adamAsmaca.adamAsmaca()
    anaMenu()
  if secim == "3":
    gectiKaldi.gectiKaldi()
    anaMenu()
  if secim == "4":
    aritmetikSayım.aritmetikSayım()
    anaMenu()
  if secim == "5":
    cokgenCizme.cokgenCizme()
    anaMenu()
  if secim == "10" or secim == "e" or secim == "E":
    print("PROGRAMDAN ÇIKILIYOR")
    exit() 

anaMenu()
