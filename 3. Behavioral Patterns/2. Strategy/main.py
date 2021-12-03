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
	pass

class LightningKick(KickBehavior):
	pass

class ShortJump(JumpBehavior):
	pass

class LongJump(JumpBehavior):
	pass


class Fighter(metaclass=abc.ABCMeta):
	_kick_behavior:'KickBehavior'
	_jump_behavior:'JumpBehavior'

	def punch(self):
		print('Normal Punch')
		return None

	def kick(self):
		return self._kick_behavior.kick()

	def jump(self):
		return self._jump_behavior.jump()

	def set_kick_behavior(self, kick_behavior):
		self._kick_behavior = kick_behavior

	def set_jump_behavior(self, jump_behavior):
		self._jump_behavior = jump_behavior