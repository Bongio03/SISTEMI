import turtle
import random

border=600
control=290

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=border, height=border)

snake= turtle.Turtle()
snake.color("green")
snake.penup()

food=turtle.Turtle()
food.color("red")
food.shape("circle")
food.shapesize(0.3)
food.penup()

speed=3

def newFood():
    x = random.randint(- border / 2 ,border / 2)
    y = random.randint(- border / 2 , border/ 2)
    food.setx(x)
    food.sety(y)

def travel():
    snake.forward(speed)
    wn.ontimer(travel,10)
    
    '''
    if snake.xcor()-food.xcor()<5 or food.xcor()-snake.xcor()<5:
        newFood()
    elif snake.ycor()-food.ycor()<5 or food.ycor()-snake.ycor()<5:
        newFood()
    '''
    if snake.ycor() >control or snake.ycor() < -control:
        snake.goto(0,0)

    if snake.xcor() > control or snake.xcor() < -control:
        snake.goto(0,0)

wn.onkey(lambda: snake.setheading(90), 'Up')
wn.onkey(lambda: snake.setheading(180), 'Left')
wn.onkey(lambda: snake.setheading(0), 'Right')
wn.onkey(lambda: snake.setheading(270), 'Down')

wn.listen()
newFood()
travel()
wn.mainloop()
