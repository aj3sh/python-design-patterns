'''
Abstract Factory creates other Factory class instance.
'''

from abc import ABC

# shapes
class Shape(ABC):
	def draw(self):
		""" draws shape """
		pass

# normal shape
class Rectangle(Shape):
	def draw(self):
		print('Draw RECTANGLE')

class Square(Shape):
	def draw(self):
		print('Draw SQUARE')

# rounded shape
class RoundedRectangle(Shape):
	def draw(self):
		print('Draw Rounded RECTANGLE')

class RoundedSquare(Shape):
	def draw(self):
		print('Draw Rounded SQUARE')


# factories
class AbstractFactory(ABC):
	def produce(self, object_type):
		""" returns Shape object """
		pass

class ShapeFactory(AbstractFactory):
	def produce(self, object_type):
		""" returns Shape object """

		if object_type == 'RECTANGLE':
			return Rectangle()
		elif object_type == 'SQUARE':
			return Square()
		return None

class RoundedShapeFactory(AbstractFactory):
	def produce(self, object_type):
		""" returns Shape object """

		if object_type == 'RECTANGLE':
			return RoundedRectangle()
		elif object_type == 'SQUARE':
			return RoundedSquare()
		return None


# factory producer
class FactoryProducer:
	@staticmethod
	def get_factory(rounded=False):
		""" returns Abstract Factory object """
		if rounded:
			return RoundedShapeFactory()
		return ShapeFactory()


def main():
	# normal shape factory
	shape_factory = FactoryProducer.get_factory(rounded=False)

	rectangle = shape_factory.produce(object_type='RECTANGLE')
	rectangle.draw()

	square = shape_factory.produce(object_type='SQUARE')
	square.draw()


	# rounded shape factory
	rounded_shape_factory = FactoryProducer.get_factory(rounded=True)

	rounded_rectangle = rounded_shape_factory.produce(object_type='RECTANGLE')
	rounded_rectangle.draw()

	rounded_square = rounded_shape_factory.produce(object_type='SQUARE')
	rounded_square.draw()


if __name__ == '__main__':
	main()