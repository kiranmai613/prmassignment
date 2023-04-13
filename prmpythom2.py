class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print("Valid Triangle")
        else:
            print("Invalid triangle")

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def validate_rectangle(self):
        if self.l == self.b:
            print("Valid Rectangle")
        else:
            print("Invalid rectangle")

a, b, c = map(int, input("enter : ").split())
t = Triangle(a, b, c)
t.validate_triangle()

l, b = map(int, input("enter : ").split())
r = Rectangle(l, b)
r.validate_rectangle()
