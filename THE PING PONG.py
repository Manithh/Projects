#import os.path
import turtle

wn = turtle.Screen()
wn.title("THE PING PONG")
wn.bgpic(r"C:\Users\hp\OneDrive\Desktop\Desktop\THE PING PONG.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260 )
pen.write("Player A:0    Player B :0", align="center", font=("courier", 24, "normal"))


# Function
def paddle_a_up():
    global paddle_a
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    global paddle_a
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    global paddle_b
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    global paddle_b
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# def keyThreadFunction():
# keyboard.on_press_key("w", lambda _: paddle_a_up())
# keyboard.on_press_key("s", lambda _: paddle_a_down())
# keyboard.on_press_key("i", lambda _: paddle_b_up())
# keyboard.on_press_key("k", lambda _: paddle_b_down())


# keyThread = threading.Thread(target=keyThread)
# keyThread.start()


while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}    Player B :{}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}    Player B :{}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))

    # paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    if (-340 > ball.xcor() > -350) and (
            paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
   
