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
import turtle, random

massiv = ["yellow", "red", "blue", "pink"]
for i in range(12):
    y = random.choice(massiv)
    pen = turtle.Turtle
    turtle.color(y)
    turtle.rt(30)
    turtle.circle(40)
turtle.done()
