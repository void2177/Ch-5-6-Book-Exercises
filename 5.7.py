import turtle


def draw_triangle(points, color):
    """Draws a filled triangle with the given corner points."""
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()


def midpoint(p1, p2):
    """Returns the midpoint between two points."""
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


def sierpinski(points, depth):
    """Recursively draws a Sierpiński triangle."""
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(points, colormap[depth % len(colormap)])

    if depth > 0:
        sierpinski([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])],
                   depth - 1)
        sierpinski([points[1],
                    midpoint(points[0], points[1]),
                    midpoint(points[1], points[2])],
                   depth - 1)
        sierpinski([points[2],
                    midpoint(points[2], points[1]),
                    midpoint(points[0], points[2])],
                   depth - 1)


# Setup turtle
turtle.speed(0)  # fastest
turtle.bgcolor("black")

# Define the big triangle coordinates
points = [[-200, -100], [0, 200], [200, -100]]

# Draw the Sierpiński triangle with depth 5
sierpinski(points, 5)

turtle.done()
