def hesapMakinesi():
    print("\033[1;32;40m   \n")
    print("╔═══════════════════════════════════════════════════╗")
    print("║\033[1;31;40m HESAP MAKİNESİ \033[1;32;40m         ║")
    print("║                                                   ║")
    print("║ 1-Toplama İşlemi                                  ║")
    print("║ 2-Çıkarma İşlemi                                  ║")
    print("║ 3-Çarpma İşlemi                                   ║")
    print("║ 4-Bölme İşlemi                                    ║")
    print("║ 5-Ana Menü                                        ║")
    print("║ Seçiminiz Nedir                                   ║")
    print("╚═══════════════════════════════════════════════════╝")
    secim = input()
    print("Seçiminiz Nedir?:", secim)
    if secim == "1":
      print("Toplama İşlemi")
      sayı1 = int(input("1. Sayıyı Giriniz:"))
      sayı2 = int(input("2. Sayıyı Giriniz:"))
      print("Toplam:", sayı1 + sayı2)
      hesapMakinesi()
    
    if secim == "2":
      print("Çıkarma İşlemi")
      sayı1 = int(input("1. Sayıyı Giriniz:"))
      sayı2 = int(input("2. Sayıyı Giriniz:"))
      print("Fark:", sayı1 - sayı2)
      hesapMakinesi()
    
    if secim == "3":
      print("Çarpma İşlemi")
      sayı1 = int(input("1. Sayıyı Giriniz:"))
      sayı2 = int(input("2. Sayıyı Giriniz:"))
      print("Çarpım:", sayı1 * sayı2)
      hesapMakinesi()
    
    if secim == "4":
      print("Bölme İşlemi")
      sayı1 = int(input("1. Sayıyı Giriniz:"))
      sayı2 = int(input("2. Sayıyı Giriniz:"))
      print("Bölüm:", sayı1 / sayı2)
      hesapMakinesi()

    
        
  #201 ╔
  #205 ═
  #187 ╗
  #186 ║
  #200 ╚
  #188 ╝
