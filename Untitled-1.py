import turtle
t = turtle.Turtle()
t.pensize(15)

turtle.bgcolor("#1B2631")

def declare_pen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#Sombra
t.pencolor("#17202A")
declare_pen(-10,-150)
for i in range(7):
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
t.left(90)
t.forward(65)
t.right(90)


t.pencolor("black")
t.fillcolor("#78281F")
t.begin_fill()


#Parte derecha
declare_pen(-25,-150)
for i in range(7):
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
t.left(90)
t.forward(70)
t.left(90)

for i in range(3):
    if i > 1:
        t.left(180)
    t.forward(25)
    t.right(90)
t.forward(25)
t.left(90)
t.forward(75)
t.left(90)

for i in range(3):
    if i > 1:
        t.left(180)
    t.forward(25)
    t.right(90)
t.forward(25)

#Parte Izquierda
t.right(90)
for i in range(3):
    if i > 1:
        t.right(180)
    t.forward(25)
    t.left(90)
t.forward(75)
t.left(90)

for i in range(3):
    if i > 1:
        t.right(180)
    t.forward(25)
    t.right(90)
t.forward(25)
t.left(90)
t.forward(95)
t.left(90)

for i in range(6):
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)

t.end_fill()


#Brillo
t.fillcolor("#FBFCFC")
t.pencolor("#FBFCFC")
t.begin_fill()

declare_pen(-137,93)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)

t.end_fill()
t.hideturtle()

#Escrito
t.penup()
t.goto(-8,0)
t.pendown()
style = ("Courier", 15, "bold")
t.color("white")
t.write("TQM", font=style, align="center")
t.penup()

turtle.Screen().exitonclick()