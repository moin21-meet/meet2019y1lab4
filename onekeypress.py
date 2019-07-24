import turtle
a=turtle.Turtle()
a.goto(0,0)
def up():
     fd(50)
     lt(50)

a.onkeypress(up,'w')
a.listen()
a.mainloop()
