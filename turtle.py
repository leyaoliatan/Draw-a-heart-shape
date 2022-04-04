
import turtle

# set a window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("shape@kaimifami")
wn.screensize(800, 600)

# set a pen
pen = turtle.Turtle()
pen.color("pink")
pen.shape("turtle")
pen.fillcolor("pink")
turtle.speed(10)

# define functions
def curve():
    for i in range(180):
        pen.right(1)
        pen.forward(2)
        
def heart():
    pen.left(135)
    pen.forward(720/3.14)
    curve()
    pen.left(90)
    curve()
    pen.forward(720/3.14)
    
def text():
    pen.penup()
    pen.setpos(-50,50)
    pen.pendown()
    pen.color("white")
    pen.write(input("enter the words:"), font = ("Verdana", 30, "bold"))
    
# painting!
pen.begin_fill()
pen.penup()
pen.setpos(0,-150)
pen.pendown()
heart()
pen.end_fill()
text()
turtle.done()
