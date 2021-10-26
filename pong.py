#simple pong game up to change to work on UI Design
#By Tyleek Jones

import turtle

win = turtle.Screen()
win.title("Pong by Tyleek Jones")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)


#Score
score_A = 0
score_B = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # default shape is 20 x 20 px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # default shape is 20 x 20 px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") # default shape is 20 x 20 px
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))



#Functions to make paddles move
def paddle_a_up(): #function to make paddle go up
    y = paddle_a.ycor() #returns the y cordinate
    y += 20
    paddle_a.sety(y) #sets original Y to new Y

def paddle_a_down(): #function to make paddle go down
    y = paddle_a.ycor() #returns the y cordinate
    y -= 20
    paddle_a.sety(y) #sets original Y to new Y

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y) 

def paddle_b_down(): 
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 


#keyboard binding
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

#main loop
while True:
    win.update() #very time the loop runs it updates the screen


    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #ball will be move by set pixel which is currently 2
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking 

        #top an bottom
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1 #reverse the direction making a bounce sequence

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1 #reverse the direction making a bounce sequence

        #Left and Right send back to the center
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1