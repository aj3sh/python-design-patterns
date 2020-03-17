class RedDotScopeDecorator:
	def __new__(self, rifle):
		rifle.scope = 'RED Dot'
		return rifle

class ExtendedMagazineDecorator:
	def __new__(self, rifle):
		rifle.ext_mag = True
		return rifle

class SuppressorDecorator:
	def __new__(self, rifle):
		rifle.suppressor = True
		return rifle

class ColorDecorator:
	def __new__(self, rifle, color='BLACK'):
		rifle.color = color
		return rifle


class M4Rifle:
	scope = None
	ext_mag = False
	suppressor = False
	color = 'BLACK'

	def  __str__(self):
		return_value = 'M4 Rifle, Serial no: {}, Color: {}'.format(id(self), self.color)

		# for scope
		if self.scope != None:
			return_value += ', Scope: '+self.scope
		
		# for extended magazine
		if self.ext_mag:
			return_value += ', Extended Magazine'
		
		# for suppressor
		if self.suppressor:
			return_value += ', Suppressor'
		
		return return_value


def main():
	m4_rifle = RedDotScopeDecorator(
		M4Rifle()
	)
	print(m4_rifle)
	
	m4_rifle = ExtendedMagazineDecorator(
		SuppressorDecorator(
			RedDotScopeDecorator(
				ColorDecorator(
					M4Rifle(),
					color='RED',
				)
			),
		)
	)
	print(m4_rifle)
	


if __name__ == "__main__":
	main()