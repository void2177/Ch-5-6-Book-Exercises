import jupyturtle
from jupyturtle import forward, left, right, back


def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)
"""I couldn't really visualize what was going on in this expression; ChatGPT was errorring and
couldn't really tell me either, so it took until I could run it to see what it did, and I saw,
yeah, it kinda spirals but goes in different directions."""