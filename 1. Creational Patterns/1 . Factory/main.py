from abc import ABC

class Shape(ABC):
	def draw(self):
		pass

class Rectangle(Shape):
	def draw(self):
		print('Draw RECTANGLE')

class Square(Shape):
	def draw(self):
		print('Draw SQUARE')

class Circle(Shape):
	def draw(self):
		print('Draw CIRCLE')


class ShapeFactory:

	def produce(self, object_type):
		""" returns Shape object """
		
		if object_type == 'CIRCLE':
			return Circle()
		elif object_type == 'RECTANGLE':
			return Rectangle()
		elif object_type == 'SQUARE':
			return Square()
		
		return None


shape_factory = ShapeFactory()

circle = shape_factory.produce(object_type='CIRCLE')
circle.draw()

square = shape_factory.produce(object_type='SQUARE')
square.draw()
