import turtle

# Set the screen size
screen = turtle.Screen()
screen.setup(400, 400)

# Ask the user to choose the background color
bgcolor = input('Enter the background color: ')
screen.bgcolor(bgcolor)

# Create a turtle
pen = turtle.Turtle()

# Ask the user to choose the pen size
pensize = int(input('Enter the pen size: '))
pen.pensize(pensize)

# Ask the user to choose the pen color
pencolor = input('Enter the pen color: ')
pen.pencolor(pencolor)

# Define a function to draw a square
def draw_square(pen, size):
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    pen.penup()
    pen.goto(pen.xcor() + size/2, pen.ycor() - 20)
    pen.write("Square",align="center", font=("Arial", 30, "bold"))
    pen.goto(pen.xcor() - size/2, pen.ycor() + 20)
    pen.pendown()

# Define a function to draw a rectangle
def draw_rectangle(pen, width, height):
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.penup()
    pen.goto(pen.xcor() + width/2, pen.ycor() - 20)
    pen.write("Rectangle", align="center", font=("Arial", 30, "normal"))
    pen.goto(pen.xcor() - width/2, pen.ycor() + 20)
    pen.pendown()

# Define a function to draw a triangle
def draw_triangle(pen, size):
    for i in range(3):
        pen.forward(size)
        pen.right(120)
    pen.penup()
    pen.goto(pen.xcor(), pen.ycor() - 20)
    pen.write("Triangle", align="center", font=("Arial", 30, "normal"))
    pen.goto(pen.xcor(), pen.ycor() + 20)
    pen.pendown()

# Define a function to draw a circle
def draw_circle(pen, radius):
    pen.circle(radius)
    pen.penup()
    pen.goto(pen.xcor(), (pen.ycor() - radius) - 20)
    pen.write("Circle", align="center", font=("Arial", 30, "normal"))
    pen.goto(pen.xcor(), (pen.ycor() + radius) + 20)
    pen.pendown()

# Define a function to draw a spiral
def draw_spiral(pen, size):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for i in range(size):
        pen.pencolor(colors[i % len(colors)])
        pen.forward(i * 10)
        pen.right(144)
        pen.write("Spiral", align="center", font=("Arial", 30, "normal"))

# Ask the user to choose a shape
shape = input('Enter a shape (S for square, R for rectangle, T for triangle, C for circle, or SP for spiral): ')

# Draw the chosen shape
if shape == 'S':
    size = int(input('Enter the size of the square: '))
    draw_square(pen, size)
elif shape == 'R':
    width = int(input('Enter the width of the rectangle: '))
    height = int(input('Enter the height of the rectangle: '))
    draw_rectangle(pen, width, height)
elif shape == 'T':
    size = int(input('Enter the size of the triangle: '))
    draw_triangle(pen, size)
elif shape == 'C':
    radius = int(input('Enter the radius of the circle: '))
    draw_circle(pen, radius)
elif shape == 'SP':
    size = int(input('Enter the size of the spiral: '))
    draw_spiral(pen, size)
else:
    print('Invalid shape')

# Keep the window open
turtle.mainloop()