import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("red")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 7
while True:
    for i in range(7):
        my_pen.fd(size + 2)
        my_pen.left(90)
        size = size - 6
    size = size + 2