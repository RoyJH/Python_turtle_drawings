from turtle import Turtle, Screen
import random

soop = Turtle()
i = 0
soop.color("green")
soop.shape("turtle")
my_colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def draw_square():
    # Draw a Square
    for _ in range(0, 4):
        soop.forward(250)
        soop.right(90)


def dotted_line():
    # Draw a dotted line.
    soop.hideturtle()
    soop.penup()
    soop.goto(-450.00, 0.00)
    soop.showturtle()
    for _ in range(0, 50):
        soop.pendown()
        soop.forward(9)
        soop.penup()
        soop.forward(9)


def draw_shapes():
    # Draw overlaying shapes with decreasing sides
    soop.hideturtle()
    soop.penup()
    soop.goto(-75.00, -375.00)
    soop.showturtle()
    soop.pendown()
    drawing = True
    sides = 16
    c = 0
    for num in range(2, 16):
        if c >= 6:
            c = 0
        soop.color(my_colors[c])
        soop.fillcolor(my_colors[c])
        angle = 360 / sides
        soop.begin_fill()
        for i in range(0, sides):
            soop.forward(150)
            soop.left(angle)
        sides -= 1
        c += 1
        soop.end_fill()


def random_walk():
    soop.pensize(5)
    soop.speed(0)
    soop.color(random.choice(my_colors))
    direction = [90, 270, 180, 0]
    to_go = random.choice(direction)
    soop.seth(to_go)
    soop.forward(random.randrange(20, 60))


# draw_square()
# dotted_line()
# draw_shapes()
for _ in range(0, 200):
    random_walk()
screen = Screen()
screen.exitonclick()
