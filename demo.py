import turtle
import random
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")
T=turtle.Turtle()
T.color("green")
T.speed(5)
T.penup()
T.goto(-240,230)
T.pendown()
T.begin_fill()
for x in range(4):
  T.forward(520)
  T.right(90)
  T.begin_fill()
T.end_fill()
T.ht()
screen.update()
scoreT = turtle.Turtle()
scoreT.color("red")
scoreT.speed(0)
scoreT.penup()
scoreT.goto(-240,260)
score = 0
scoreT.write("Score: " + str(score), font=("Times New Roman",17,"normal"))
scoreT.ht()
play = turtle.Turtle()
play.penup()
play.goto(-80,-230)
play.color("pink")
screen.register_shape("paddle",((0,0),(20,0),(20,100),(0,100)))
play.shape("paddle")
ball = turtle.Turtle()
ball.shape("circle")
ball.color("grey")
ball.penup()
ball.goto(-50,-210)
ball.setheading(random.randint(1,193))
screen.update()
screen.register_shape("brick",((0,10),(10,0),(10,50),(0,50)))
colors = ["sky blue", "brown", "green","yellow","red","orange","grey","tomato"]
def func(x,y,colors):
  index = random.randint(0,len(colors)-1)
  row = []
  for i in range(8):
    targetT = turtle.Turtle()
    targetT.speed(0)
    targetT.shape("brick")
    targetT.color(colors[index])
    targetT.penup()
    targetT.goto(x + 60*i,y)
    targetT.pendown()
    row.append(targetT)
    index = random.randint(0,len(colors)- 1)
  return row
screen.update()
def right():
  play.forward(18)
screen.onkey(right, "Right")
def left():
  play.backward(10)
screen.onkey(left, "Left")
screen.listen()
def Brick(obj):
  if abs(ball.xcor() - obj.xcor()) < 50 and obj.ycor() <= ball.ycor() <= obj.ycor() + 10 :
    print("colided with the brick:", obj)
    return True
  return False
def Paddle(obj):
  if abs(ball.xcor() - obj.xcor()) < 100 and (obj.ycor() <= ball.ycor() <= obj.ycor() + 20) :
    return True
  return False
def bounce(game):
  if game == "top" or game == "paddle":
    ball.setheading(360 - ball.heading())
  elif 180 > ball.heading() >= 0:
    ball.setheading(180 - ball.heading())
  elif 180 <= ball.heading() < 360:
    ball.setheading(540 - ball.heading())
screen.update()
def countList():
  count = []
  for i in range(8):
    count.append(0)
  return count
def Ball(row, count, goal):
  global score
  for x in range(len(row)):
    if Brick(row[x]):
      if count[x] > goal:
        row[x].ht()
        row[x].penup()
        row[x].goto(-1000,1000)
      else:
        count[x] += 1
        bounce("paddle")
      score = updateScore(score)
  return count
def updateScore(score):
  score += 5
  scoreT.clear()
  scoreT.write("Score: " + str(score), font=("Arial",14,"normal"))
  return score
row1 = func(-230,220,colors)
count1 = countList()
row2 = func(-230,190,colors)
count2 = countList()
row3 = func(-230,160,colors)
count3 = countList()
row4 = func(-230,130,colors)
count4 = countList()
gameContinue=True
while gameContinue:
  ball.forward(5)
  screen.update()
  count1 = Ball(row1, count1, 4)
  count2 = Ball(row2, count2, 3)
  count3 = Ball(row3, count3, 2)
  count4 = Ball(row4, count4, 1)
  if ball.ycor() < -240:
    T.penup()
    T.goto(-200,0)
    T.color("midnight blue")
    T.write("YOU LOSE! :( ", font=("Calibiri",48,"normal"))
    gameContinue=False
  if score == 720:
    T.penup()
    T.goto(-200,0)
    T.color("orange")
    T.write("You Win!!! :)", font=("Fixedsys",48,"normal"))
    gameContinue=False
  if ball.xcor() > 240:
    bounce("right")
  if ball.xcor() < -240:
    bounce("left")
  if ball.ycor() > 240:
    bounce("top")
  if Paddle(play):
    bounce("paddle")
  if play.xcor() + 100  > 240:
    play.backward(10)
  if play.xcor() < -240:
    play.forward(10)
  screen.update
