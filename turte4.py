import turtle
turtle.shape('turtle')
hi=turtle.clone()
hi.shape('square')
hi.goto(100,0)
hi.left(90)
turtle.goto(100,50)
hi.forward(50)
hi.stamp()
hi.goto(100,100)

hi.clearstamps()
turtle.mainloop()
