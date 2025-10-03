"""The **Koch curve** (sometimes called the Koch snowflake curve) is a famous example of a *fractal*—a geometric figure that is self-similar and infinitely detailed.

Here’s how it works:

1. **Start with a straight line segment.**
2. **Divide it into three equal parts.**
3. **Replace the middle part with two sides of an equilateral triangle**, sticking outward.

   * So instead of one middle third, you now have two sides of a "bump."
4. **Repeat this process for every line segment**, again and again.

Each iteration makes the curve more jagged. If you keep repeating infinitely:

* The curve becomes infinitely long, even though it stays inside a finite space.
* It has a fractional (non-integer) dimension: about **1.2619**.
* The **Koch snowflake** is formed by applying this process to all three sides of an equilateral triangle.

Would you like me to show you a **diagram of the first few iterations** of the Koch curve so you can visualize it?
"""

import turtle
t = turtle.Turtle()
turtle.speed(0)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()

def koch(x):
    if x < 5:
        t.forward(x)
    else:
        koch(x/3)
        turtle.left(60)
        koch(x/3)
        turtle.right(120)
        koch(x/3)
        turtle.left(60)
        koch(x/3)



koch(400)
turtle.done()
