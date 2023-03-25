import turtle

# create a turtle object
t = turtle.Turtle()

# create a screen for the turtle to draw on
screen = turtle.Screen()

# set the screen's background color
screen.bgcolor("black")

# set the turtle's color and shape
t.color("darkgreen")
t.shape("turtle")

# create a function to move the turtle forward
def move_forward():
    t.forward(100)

# create a function to turn the turtle left
def turn_left():
    t.left(90)

# create a function to turn the turtle right
def turn_right():
    t.right(90)

# create a function to hide turtle
def hide():
    t.ht()

# create a function to unhide turtle
def show():
    t.st()

# create a function to not draw
def penup():
    t.penup()

# create a function to draw
def pendown():
    t.pendown()

# create a function to return to home
def home():
    t.goto(0,0)

# create a function to draw a circle
def circle():
    t.circle(100)

# bind the functions to key events on the screen
screen.onkeypress(move_forward, "w")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(hide, "space")
screen.onkeypress(show, "s")
screen.onkeypress(penup, "p")
screen.onkeypress(pendown, "l")
screen.onkeypress(home, 'h')
screen.onkeypress(circle,  'c')

# start the screen's event loop
screen.listen()
screen.mainloop()
