import turtle
import random
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, artist):
        pass  # La méthode de dessin sera définie dans les classes enfants


class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)  # Appel correct du constructeur de Shape
        self.radius = radius

    def draw(self, artist):
        artist.penup()
        artist.goto(self.x, self.y - self.radius)
        artist.pendown()
        artist.color(self.color)
        artist.begin_fill()
        artist.circle(self.radius)
        artist.end_fill()


class Rectangle(Shape):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, artist):
        artist.penup()
        artist.goto(self.x, self.y)
        artist.pendown()
        artist.color(self.color)
        artist.begin_fill()
        for _ in range(2):
            artist.forward(self.width)
            artist.left(90)
            artist.forward(self.height)
            artist.left(90)
        artist.end_fill()


class Triangle(Shape):
    def __init__(self, x, y, color, side_length):
        super().__init__(x, y, color)
        self.side_length = side_length

    def draw(self, artist):
        artist.penup()
        artist.goto(self.x, self.y)
        artist.pendown()
        artist.color(self.color)
        artist.begin_fill()
        for _ in range(3):
            artist.forward(self.side_length)
            artist.left(120)
        artist.end_fill()


# Initialisation de la fenêtre de dessin
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Test des formes")

artist = turtle.Turtle()
artist.speed(2)
artist.hideturtle()

# Crée un cercle, un rectangle, et un triangle
circle = Circle(0, 0, "Pink", 50)
rectangle = Rectangle(-100, 100, "purple", 150, 100)
triangle = Triangle(100, -50, "green", 100)

# Dessine les formes
circle.draw(artist)
rectangle.draw(artist)
triangle.draw(artist)

# Garde la fenêtre ouverte jusqu'à ce que l'utilisateur la ferme
screen.mainloop()
