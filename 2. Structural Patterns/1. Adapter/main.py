import abc


class Player(metaclass=abc.ABCMeta):
	def __init__(self, file_name, file_type):
		self.file_name = file_name
		self.file_type = file_type

	@abc.abstractmethod
	def play(self):
		pass


class VlcPlayer(Player):
	supported_file_types = ['mp3', 'mp4', 'avi', 'mkv']

	def play(self):
		
		if self.file_type not in self.supported_file_types:
			# wav file not supported by vlc is playing through adapter
			adapter = MediaAdapter(self.file_name, self.file_type)
			adapter.play()
			return

		# playing audio file
		print('Playing {} from VLC Player'.format(self.file_name))


class MediaAdapter(Player):
   
	def play(self):
		if self.file_type == 'wav':
			wav_player = WAVPlayer()
			wav_player.play_music(self.file_name)
		else:
			raise Exception('Unsupported audio format')

class WAVPlayer:
	"""
	plays legacy wav audio format
	"""

	def play_music(self, file_name):
		print('Playing {} from WAVPlayer'.format(file_name))


def main():
	# playing mp3 file
	vlc_player = VlcPlayer('on the horizon.mp3', 'mp3')
	vlc_player.play()

	# playing mp4 file
	vlc_player = VlcPlayer('on the horizon.mp4', 'avc')
	vlc_player.play()

	# playing wav file
	vlc_player = VlcPlayer('on the horizon.wav', 'wav')
	vlc_player.play()


if __name__ == "__main__":
	main()