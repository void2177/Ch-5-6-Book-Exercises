##First one is missing a base case
##Second one returns before the last line can be executed
##Third one doesn't need if then, the equation already equates to true or false

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Example usage
print(distance(0, 0, 3, 4))  # Output: 5.0
