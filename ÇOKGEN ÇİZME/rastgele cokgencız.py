import random
import turtle
turtle.speed(100)
#turtle.goto(100,200)

renkler = ["red","green","blue","orange","yellow","purple"]


def ciz(kenar,buyukluk):
    for a in range(kenar):
        turtle.forward(buyukluk)
        turtle.right(360/kenar)

for a in range(20):
    #print (random.choice(renkler))
    turtle.penup()
    xx = random.randint(-100,100)
    yy = random.randint(-100,100)
    turtle.goto(xx,yy)
    turtle.pendown()
    turtle.color(random.choice(renkler))
    b = random.randint(50,100)
    ciz (random.randint(3,7),b)
