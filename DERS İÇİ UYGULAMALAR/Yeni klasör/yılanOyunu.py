import random



def tahtaOlustur(boyuta,karaktera):
    tahta = [boyuta][boyuta]
    for a in range(boyuta):
        for b in range(boyuta):
            tahta[a][b]=karaktera  #oyun tahtası oluşturmak ıcın atamalar yaptım.
            
    for a in range(boyuta):
        for b in range(boyuta):
        print(tahta[a][b])         #olusturdugum tahtayı yazdırdım.

def karakterYerlestir(gelen,boyutx):
    tahtaOlustur(boyutx,".")
    x = random.randint(0,boyut)
    y = random.randint(0,boyut)
    print(x,y,gelen)

boyut = 15

karakterYerlestir("o",boyut)
        
