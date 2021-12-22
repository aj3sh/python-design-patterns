'''
Builder pattern builds a complex object using simple objects and using a step by step approach.
'''

class Person:

	def __init__(self, first_name, last_name, age, fathers_name, mothers_name, height, weight):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.fathers_name = fathers_name
		self.mothers_name = mothers_name
		self.height = height
		self.weight = weight

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

	class Builder:

		def set_first_name(self, first_name):
			self.first_name = first_name
			return self

		def set_last_name(self, last_name):
			self.last_name = last_name
			return self

		def set_age(self, age):
			self.age = age
			return self

		def set_fathers_name(self, fathers_name):
			self.fathers_name = fathers_name
			return self

		def set_mothers_name(self, mothers_name):
			self.mothers_name = mothers_name
			return self

		def set_height(self, height):
			self.height = height
			return self

		def set_weight(self, weight):
			self.weight = weight
			return self

		def build(self):
			return Person(first_name=self.first_name, last_name=self.last_name, age=self.age, fathers_name=self.fathers_name, 
							mothers_name=self.mothers_name, height=self.height, weight=self.weight)



def main():
	person = Person.Builder().set_first_name('Ajesh').set_last_name('Thapa').set_age(21).set_fathers_name('test').set_mothers_name('Test'
				).set_height(30).set_weight(30).build()
	print(person)


if __name__ == '__main__':
	main()