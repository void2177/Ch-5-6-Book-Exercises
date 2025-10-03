def is_triangle(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a:
                print("Yes")
                return True
    else:
        print("No")

is_triangle(1, 12, 1)