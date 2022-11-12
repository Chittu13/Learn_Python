# Program for Smiley face using Python turtle 
```python
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(99999)
# FACE

t.penup()
t.goto(0, -150)
t.pendown()
t.shape("turtle")
t.color("yellow")
t.begin_fill()
t.circle(200, 360)
t.end_fill()
t.color("black")
t.width(5)
t.penup()
t.goto(0, -152)
t.pendown()
t.circle(202, 360)
# EYES
t.penup()
t.goto(-40, 100)
t.pendown()
t.begin_fill()
t.left(50)
t.circle(40, 360)
t.end_fill()
t.begin_fill()
t.penup()
t.goto(90, 100)
t.pendown()
t.circle(40, -360)
t.end_fill()
# SMILE
t.penup()
t.goto(125, 25)
t.pendown()
t.right(-40)
t.circle(130, -180)
t.hideturtle()

turtle.done()

```