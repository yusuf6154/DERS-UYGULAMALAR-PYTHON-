import turtle
import triangle
import square
import cokgenCiz

def menu():
    print("ÇİZİM MENÜSÜ")
    print("1-Üçgen Çiz")
    print("2-Kare Çiz")
    print("3-Çokgen Çiz")
    print("4-ANA MENÜ")
    secim= input()
    if secim== "1":
        triangle.triangle()
        menu()
    if secim== "2":
        square.square()
        menu()
    if secim== "3":
        a=int(input("Kenar sayısı ne olsun?"))
        b=int(input("UZUNLUK"))     
        cokgenCiz.cokgenCiz(a,b)
        menu()
    if secim== "4":
        anaMenu()
menu()
