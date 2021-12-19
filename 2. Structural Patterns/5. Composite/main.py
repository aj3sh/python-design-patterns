'''
Composite is a structural design pattern that lets you compose objects into tree structures 
and then work with these structures as if they were individual objects.

eg. If some event is happened to the node, it will handle that event and pass it to its children
and the children node does the same.
'''

class Item:
	def __init__(self, *, weight):
		self._weight = weight
	
	@property
	def weight(self):
		return self._weight

class Box(Item):
	items: list

	def __init__(self, *args, **kwargs):
		self.items = []
		super().__init__(*args, **kwargs)

	def add(self, item):
		self.items.append(item)

	@property
	def weight(self):
		total_weight = self._weight
		for item in self.items:
			total_weight += item.weight
		return total_weight

class Product(Item):
	
	def __init__(self, *, name, weight):
		self._name = name
		super().__init__(weight=weight)

def main():
	main_box = Box(weight=10)
	main_box.add(Product(name='Product 1', weight=10))
	sub_box = Box(weight=5)
	sub_box.add(Product(name='Product 2', weight=15))
	sub_box.add(Product(name='Product 3', weight=5))
	main_box.add(sub_box)
	print('Weight of main box', main_box.weight)
	


if __name__ == "__main__":
	main()