class CPU:
	"""
	Simple CPU representation.
	"""
	def freeze(self):
		print("Freezing processor.")

	def jump(self, position):
		print("Jumping to memory address:", position)

	def execute(self):
		print("Executing.")


class Memory:
	"""
	Simple RAM Memory representation.
	"""
	def load(self, data):
		print('loading data on memory')
		# return memory address
		return 0x0b

class SSD:
	"""
	Simple Solid State Drive representation.
	"""
	def read_os(self):
		print('Reading os files from disk')

class ComputerFacade:
	"""
	Represents a facade for various computer parts.
	"""
	def __init__(self):
		self.cpu = CPU()
		self.memory = Memory()
		self.ssd = SSD()

	def start(self):
		self.cpu.freeze()
		memory_address = self.memory.load(self.ssd.read_os())
		self.cpu.jump(memory_address)
		self.cpu.execute()



computer_facade = ComputerFacade()
computer_facade.start()