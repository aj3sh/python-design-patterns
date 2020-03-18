"""
Example of Bridge between Device and Remote
"""

import abc

class AbstractDevice(metaclass=abc.ABCMeta):
	__enabled = False
	__volume = 4
	__max_volume = 10
	__min_volume = 0
	name = 'DEVICE'

	def __str__(self):
		if not self.__enabled:
			return '{} is OFF'.format(self.name)
		else:
			return '{} is ON, VOLUME: {}'.format(self.name, self.__volume)

	def enable(self):
		self.__enabled = True

	def disable(self):
		self.__enabled = False

	def is_enabled(self):
		return self.__enabled

	def set_volume(self, volume):
		if volume >= self.min_volume and volume <= self.max_volume:
			self.__volume  = volume

	def get_volume(self):
		return self.__volume

	# properties

	@property
	def min_volume(self):
		return self.__min_volume

	@property
	def max_volume(self):
		return self.__max_volume


class AbstractRemote(metaclass=abc.ABCMeta):

	def __init__(self, device):
		# setting up bridge connection
		self.device = device

	def toggle_power(self):
		self.device.disable() if self.device.is_enabled() else self.device.enable()

	def volume_up(self):
		self.device.set_volume(self.device.get_volume() + 1)

	def volume_down(self):
		self.device.set_volume(self.device.get_volume() - 1)


# Other Devices

class TV(AbstractDevice):
	name = 'TV'

class Radio(AbstractDevice):
	name = 'RADIO'


# Other remote
class NormalRemote(AbstractRemote):
	pass

class AdvanceRemote(AbstractRemote):
	__unmute_volume = 4

	def toggle_mute(self):
		if self.device.get_volume() == self.device.min_volume:
			self.device.set_volume(self.__unmute_volume)
		else:
			self.__unmute_volume = self.device.get_volume()
			self.device.set_volume(self.device.min_volume)

radio = Radio()
radio_remote = NormalRemote(device=radio)
radio_remote.toggle_power()
print(radio)
radio_remote.toggle_power()
print(radio)

tv = TV()
tv_remote = AdvanceRemote(device=tv)
tv_remote.toggle_power()
tv_remote.volume_up()
print(tv)
tv_remote.toggle_mute()
print(tv)
tv_remote.toggle_mute()
print(tv)