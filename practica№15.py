#Задание 1
import turtle

okno = turtle.Screen()
t = turtle.Turtle()
t.color("blue")
for i in range(4):
    t.forward(150)
    t.left(90)

turtle.done()
#Задание 2
import turtle

okno = turtle.Screen()
t = turtle.Turtle()
t.color("blue")
t.goto(60,0)
t.goto(60,100)
t.goto(0,0)

turtle.done()
#Задание 3
import turtle

okno = turtle.Screen()
okno.bgcolor("black")
t = turtle.Turtle()
t.color("orange")
t.circle(80)

turtle.done()
#Задание 4
import turtle

okno = turtle.Screen()
t = turtle.Turtle()
t.color("pink")
t.circle(90,90,)
t.circle(180,90,)
t.circle(90,90,)
t.circle(180,90,)

turtle.done()
#Задание 5
import turtle

turtle.begin_fill()
turtle.fillcolor("red")
turtle.goto(40,159)
turtle.goto(80,0)
turtle.goto(80,0)
turtle.goto(-40,90)
turtle.goto(120,90)
turtle.goto(0,0)
turtle.end_fill()

turtle.done()
#Задание 6
import turtle

t = turtle.Turtle()
t.pensize(2)
colors = ["yellow", "red", "blue", "pink", "green" ,"black"]
num_color = 0
for i in range(12):
    t.left(30)
    t.circle(40)
    t.color(colors[num_color % len(colors)])
    num_color += 1

turtle.done()
#Задание 7
import turtle

okno = turtle.Screen()
t1 = turtle.Turtle()
t1.color("green")
t1.shape('turtle')
t2 = turtle.Turtle()
t2.color("red")
t2.shape('turtle')
t1.pensize(3)
t2.pensize(3)
t1.circle(180,180)
t1.goto(0,0)
t2.rt(180)
t2.circle(-180,180)
t2.left(180)
t2.circle(180,90)
t2.left(90)
t2.forward(360)

turtle.done()
#Задание 8
import turtle

okno = turtle.Screen()
t = turtle.Turtle()
t.pensize(2)
t.up()
t.goto(-40,120)
t.down()
for i in range(4):
    t.forward(100)
    t.circle(-60,90)
t.up()
t.goto(0,0)
t.write(">>>Hello World!")

turtle.done()
#Задание 9
import turtle

okno = turtle.Screen()
okno.bgpic('D:\\back1.png')
t = turtle.Turtle()
t.shape('turtle')
t.color('red')
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(195)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)

turtle.done()
#Задание 10
import turtle

okno = turtle.Screen()
okno.bgpic('D:\\back2.png')
t = turtle.Turtle()
t.speed(10)
t.shape('turtle')
t.color('green')
t.forward(54)
t.left(90)
t.circle(54,270)
t.rt(90)
t.forward(120)
t.left(90)
t.circle(155,-180)
t.left(180)
t.forward(192)
t.rt(90)
t.forward(199)
t.rt(55)
t.forward(190)
t.rt(115)
t.forward(85)
t.rt(73)
t.forward(80)

turtle.done()
#Задание 11
import turtle

t = turtle.Turtle()
t.shape('turtle')

colors = ["yellow", "red", "blue", "pink", "green"]
num_color = 0
for i in colors:
    t.begin_fill()
    t.color(colors[num_color % len(colors)])
    num_color += 1
    t.circle(90)
    t.end_fill()

turtle.done()
#Задание 12
import turtle

okno = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('green')
okno.bgcolor('blue')
t.left(90)
summ = 0

while True:
    text = turtle.textinput("Направление: w, a, s, d", "Куда идти?")
    number = turtle.numinput("Сколько шагов сделать?", "Введите число.")
    if text == "w":
        t.forward(number)
    elif text == "a":
        t.left(90)
        t.forward(number)
    elif text == "s":
        t.left(180)
        t.forward(number)
    elif text == "d":
        t.rt(90)
        t.forward(number)
    elif text == "exit":
        break
    summ += number

t.write(f"Всего было сделано  {summ} шагов")
turtle.done()
#Задание 13
import turtle

okno = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('green')

def vpered():
    t.forward(15)

def nazad():
    t.backward(15)

def vlevo():
    t.left(30)

def vpravo():
    t.right(30)

okno.listen()
okno.onkey(vpered, "w")
okno.onkey(nazad, "s")
okno.onkey(vlevo, "a")
okno.onkey(vpravo, "d")

turtle.done()
