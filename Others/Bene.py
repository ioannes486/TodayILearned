import turtle

t = turtle.Turtle()
t.speed(10)

# Draw the yellow part of the logo
t.color("gold", "gold")
t.begin_fill()
t.right(45)
t.forward(100)
t.right(135)
t.forward(200)
t.right(135)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

# Draw the blue part of the logo
t.color("midnight blue", "midnight blue")
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(135)
t.forward(142)
t.right(135)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

# Draw the inner part of the logo
t.color("gold", "gold")
t.begin_fill()
t.right(180)
t.forward(100)
t.right(45)
t.forward(70)
t.right(45)
t.forward(60)
t.left(135)
t.forward(100)
t.right(135)
t.forward(60)
t.right(45)
t.forward(70)
t.right(45)
t.forward(100)
t.end_fill()

# Hide the Turtle and keep the screen open until closed
t.hideturtle()
turtle.done()

