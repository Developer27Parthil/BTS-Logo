# developerparthil
from turtle import * 
t = Turtle()
s = Screen()
s.setup(width=900, height=750)

t.fillcolor("black")
t.seth(180)
t.begin_fill()
t.penup()
t.goto(0, 375)
t.pendown()
t.circle(340)
t.penup()
t.end_fill()
t.setpos(-125, -125)
t.pendown()
t.pencolor("White")
t.seth(90)
t.fillcolor("white")
t.begin_fill()
t.forward(400)
t.right(131)
t.forward(150)
t.seth(270)
t.forward(250)
t.right(60)
t.forward(124)
t.end_fill()
t.seth(0)
t.penup()
t.forward(250)
t.pendown()
t.begin_fill()
t.seth(90)
t.forward(401)
t.left(131)
t.forward(150)
t.seth(270)
t.forward(250)
t.left(65)
t.forward(124)
t.end_fill()
t.seth(270)
t.penup()
t.ht()
t.forward(150)
t.right(90)
t.forward(240)
t.st()
t.pendown()
t.write("BTS", font=("Times New Roman", 95))
done()
