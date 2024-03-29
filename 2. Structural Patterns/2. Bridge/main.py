"""
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes 
into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

Example of Bridge between Shape and Color
Suppose if we need objects like red triangle, green circle, green triangle and red circle
We can do this by making four classes RedTriangle, GreenCircle, GreenTriangle and RedCircle
But bridge pattern allows us to do this by simple way by making Triangle, Circle shape classes and Green, Red color classes.
In this way, if new shape and Color is added we don't have to make every color class for shapes 
eg. NewColorTriangle and NewColorCircle. Just make color class NewColor
"""

import abc

class Color(metaclass=abc.ABCMeta):
	def fill(self):
		pass

class Shape(metaclass=abc.ABCMeta):

	def __init__(self, color):
		self.color = color

	def draw(self):
		pass


# Colors
class Green(Color):
	def fill(self):
		return "#00ff00"

class Red(Color):
	def fill(self):
		return "#ff0000"

# Shapes
class Triangle(Shape):
	def draw(self):
		print("Drawing triangle with color "+self.color.fill())

class Circle(Shape):
	def draw(self):
		print("Drawing circle with color "+self.color.fill())


def main():
	red_triangle = Triangle(Red())
	red_triangle.draw()

	green_circle = Circle(Green())
	green_circle.draw()


if __name__ == '__main__':
	main()