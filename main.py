import turtle
import random
import time
gravity = -1.5
velocity = 0
bird_height = 0
you_lose = turtle.Turtle()
pipe = turtle.Turtle()
high_score_display = turtle.Turtle()
score_display = turtle.Turtle()
high_score = 0
screen = turtle.Screen()    
screen.bgpic("background (1).png")
def go_up():
  global velocity
  velocity = 7
  #gravity += 0.75
  pass

def apply_physics():
  global bird_height
  global velocity
  global gravity
  velocity += gravity
  velocity *= 0.9
  bird_height += velocity
  turtle.seth(90 + velocity * 3)
  pass
while True:
  pipe.st()
  points = 0
  high_score_display.penup()
  high_score_display.ht()
  high_score_display.speed(0)
  high_score_display.setpos(100, 175)
  high_score_display.clear()
  high_score_display.write(high_score, font = ("Arial", 13, "normal"))
  score_display.penup()
  score_display.ht()
  score_display.speed(0)
  score_display.setpos(75, 175)
  you_lose.color("Red")
  you_lose.penup()
  you_lose.clear()
  you_lose.ht()
  you_lose.speed(0)
  you_lose.setpos(0, 0)
  turtle.penup()
  turtle.speed(0)
  turtle.setpos(-150, 0)
  turtle.seth(90)
  pipe.speed(0)                       
  pipe.seth(90)
  pipe.penup()
  pipe.setpos(400, random.randint(-150, 150))
  screen.addshape("bIRd2 (1).png")
  screen.addshape("pipes2.png")
  pipe.shape("pipes2.png")
  turtle.color("Green")
  turtle.shape("bIRd2 (1).png")
  # gravity = 0
  screen.listen()
  screen.onkey(go_up, "space")
  print(gravity, velocity)
  velocity = 0
  bird_height = 0
  while True:
    apply_physics()
    turtle.setpos(turtle.xcor(), bird_height)
   # gravity -= 0.25
    pipe.setpos(pipe.xcor() - 10, pipe.ycor())
    if pipe.xcor() < -200:
      pipe.setpos(400, random.randint(-150, 150))
    if turtle.ycor() > 200 or turtle.ycor() < -200:
      break
  you_lose.write("You Lose!", font = ("Arial", 50, "normal"), align = ("center"))
  turtle.seth(270)
  while turtle.ycor() > -200:
    turtle.setpos(turtle.xcor(), turtle.ycor() - 10)
  if points > high_score:
    high_score = points
    print("You got " + str(points) + " points! NEW HIGH SCORE!")
  else:
    print("You got " + str(points) + " points!")
  score_display.clear()
  score_display.write("0", font = ("Arial", 13, "normal"))
  time.sleep(5) > pipe.ycor() + 40 or turtle.ycor() < pipe.ycor() - 78
  if turtle.xcor() > pipe.xcor() - 60 and turtle.xcor() < pipe.xcor() + 50:
    break
    if turtle.xcor() > pipe.xcor() - 50 and pipe.xcor() == -110:
      if turtle.ycor() > pipe.ycor() + 78 or turtle.ycor() < pipe.ycor() - 78:
        break
      else:
        points +=1
        score_display.clear()
        score_display.write(points, font = ("Arial", 13, "normal"))
      print(points)
      pass
    pass
  pipe.ht()