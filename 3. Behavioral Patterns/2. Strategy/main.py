import abc

#
# Abstract class

class KickBehavior(metaclass=abc.ABCMeta):
	def kick(self):
		raise NotImplementedError('Kick method is not implemented in this kick behavior.')

class JumpBehavior(metaclass=abc.ABCMeta):
	def jump(self):
		raise NotImplementedError('Jump method is not implemented in this jump behavior.')


# Implementation

class LightningKick(KickBehavior):
	def kick(self):
		print('Lightning kick.')

class TornadoKick(KickBehavior):
	def kick(self):
		print('Tornado kick.')

class ShortJump(JumpBehavior):
	def jump(self):
		print('Short kick.')

class LongJump(JumpBehavior):
	def jump(self):
		print('Long kick.')


class Fighter(metaclass=abc.ABCMeta):
	_kick_behavior:'KickBehavior'
	_jump_behavior:'JumpBehavior'

	def punch(self):
		print('Normal Punch.')
		return None

	def kick(self):
		return self._kick_behavior.kick()

	def jump(self):
		return self._jump_behavior.jump()

	def set_kick_behavior(self, kick_behavior):
		self._kick_behavior = kick_behavior

	def set_jump_behavior(self, jump_behavior):
		self._jump_behavior = jump_behavior


def main():
	human_fighter = Fighter()
	human_fighter.set_jump_behavior(ShortJump())
	human_fighter.set_kick_behavior(TornadoKick())
	# actions
	print("Human Fighter")
	human_fighter.punch()
	human_fighter.jump()
	human_fighter.kick()

	
	alien_fighter = Fighter()
	alien_fighter.set_jump_behavior(LongJump())
	alien_fighter.set_kick_behavior(LightningKick())
	# actions
	print("\nAlien Fighter")
	alien_fighter.punch()
	alien_fighter.jump()
	alien_fighter.kick()

	# changing behavior
	alien_fighter.set_kick_behavior(TornadoKick())
	alien_fighter.kick()


if __name__ == "__main__":
	main()