import cv2
import turtle

# Read outline image
img = cv2.imread("outline.png", 0)

# Find contours
contours, _ = cv2.findContours(
    img,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

# Turtle setup
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
canvas = screen.getcanvas()
canvas.master.state("zoomed")
screen.bgcolor("black")
screen.title("🚩 Jai Shree Ram 🚩")

pen = turtle.Turtle()
turtle.tracer(10, 10)
pen.color("orange")
pen.pensize(2)
pen.hideturtle()

# Scale
scale = 0.6

height, width = img.shape

for contour in contours:

    pen.penup()

    first = contour[0][0]

    x = (first[0] - width/2) * scale
    y = (height/2 - first[1]) * scale

    pen.goto(x, y)
    pen.pendown()

    for point in contour:

        x = (point[0][0] - width/2) * scale
        y = (height/2 - point[0][1]) * scale

        pen.goto(x, y)

pen.penup()
pen.goto(0, -380)
pen.color("orange")
pen.write(
    "🚩 JAI SHREE RAM 🚩",
    align="center",
    font=("Arial",18,"bold")
)

turtle.done()
screen.update()