import turtle
a=turtle.Turtle()
a.goto(0,0)
def up():
     a.forward(50)
def back():
     a.back(50)
def left():
     a.left(90)
def right():
     a.right(90)
def color_green():
     a.color('green')
def color_blue():
     a.color('blue')
def color_red():
     a.color('red')

turtle.onkeypress(up, 'w')
turtle.onkeypress(back, 's')
turtle.onkeypress(left, "a")
turtle.onkeypress(right, 'd')
turtle.onkeypress(color_green, 'g')
turtle.onkeypress(color_red, 'r')
turtle.onkeypress(color_blue, 'b')
turtle.listen()
turtle.mainloop()
