'''
Instead of creating new objects setting the same attributes every time, 
Prototype method include prototyping the common objects into a cache and clones it to give a new instance.
Later on the distinct attributes can be changed.
'''

import copy

class Player:
	name = None
	
	def set_name(self, name):
		self.name = name

	def set_skill(self, stricker_skill, midfielder_skill, defender_skill):
		self.stricker_skill = stricker_skill
		self.midfielder_skill = midfielder_skill
		self.defender_skill = defender_skill

	def clone(self):
		return copy.copy(self)

class Striker(Player):
	def print_status(self):
		print("Striker, Name: {}, Skill: {}".format(self.name, self.stricker_skill))

class MidFielder(Player):
	def print_status(self):
		print("Midfielder, Name: {}, Skill: {}".format(self.name, self.midfielder_skill))

class Defender(Player):
	def print_status(self):
		print("Defender, Name: {}, Skill: {}".format(self.name, self.defender_skill))


# prototype
class PlayerPrototype:
	players = {}

	@staticmethod
	def load_prototype():
		# stricker prototype
		stricker = Striker()
		stricker.set_skill(90, 40, 10)

		# midfielder prototype
		midfielder = MidFielder()
		midfielder.set_skill(60, 90, 70)

		# defender prototype
		defender = Defender()
		defender.set_skill(15, 60, 90)

		PlayerPrototype.players = {
			'STRICKER': stricker,
			'MIDFIELDER': midfielder,
			'DEFENDER': defender,
		}

	@staticmethod
	def get_player(player_type):
		return PlayerPrototype.players.get(player_type).clone()



def main():
	# loading all prototypes
	PlayerPrototype.load_prototype()

	# loading stricker
	striker1 = PlayerPrototype.get_player('STRICKER')
	striker1.set_name('Max')
	striker1.print_status()

	# loading another stricker
	striker2 = PlayerPrototype.get_player('STRICKER')
	striker2.set_name('John')
	striker2.print_status()

	# loading midfielder
	midfielder = PlayerPrototype.get_player('MIDFIELDER')
	midfielder.set_name('Jason')
	midfielder.set_skill(40, 100, 90)
	midfielder.print_status()


if __name__ == '__main__':
	main()