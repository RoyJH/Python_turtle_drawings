from turtle import Turtle, Screen

soop = Turtle()
i = 0
soop.color("green")
soop.shape("turtle")

# # Draw a Square
# while i < 4:
#     timmy_the_turtle.forward(250)
#     timmy_the_turtle.right(90)
#     i += 1
soop.hideturtle()
soop.penup()
soop.goto(-450.00, 0.00)
soop.showturtle()
while i < 50:
    soop.pendown()
    soop.forward(9)
    soop.penup()
    soop.forward(9)
    i += 1

screen = Screen()
screen.exitonclick()
