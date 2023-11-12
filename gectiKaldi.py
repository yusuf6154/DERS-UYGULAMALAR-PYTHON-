def gectiKaldi():
    sonuç = int(input("notunuzu giriniz:"))

    if sonuç <0 or sonuç >100:
        print ("geçersiz değer")
        gectiKaldi() 
        
    else:
        if sonuç >50 :
            print ("geçtin.")
            if sonuç> 90: print("süper")
            elif sonuç >75: print ("iyi")
            elif sonuç >50: print ("eh işte")
            gectiKaldi() 
   
            
        else:
            print("kaldın")
            gectiKaldi() 
    


