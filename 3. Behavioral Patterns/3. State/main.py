class AudioPlayerState:
	def __init__(self) -> None:
		self.audio_player = None

	def play(self):
		# do nothing
		pass

	def pause(self):
		# do nothing
		pass

	def stop(self):
		# do nothing
		pass

	def next(self):
		# do nothing
		self.audio_player.current_song_index = (self.audio_player.current_song_index + 1) % len(self.audio_player.songs)
		print('Playing {}'.format(self.get_current_song()))
		self.audio_player.set_state(PlayingState())

	def previous(self):
		# do nothing
		self.audio_player.current_song_index = (self.audio_player.current_song_index - 1) % len(self.audio_player.songs)
		print('Playing {}'.format(self.get_current_song()))
		self.audio_player.set_state(PlayingState())

	def get_current_song(self):
		return self.audio_player.songs[self.audio_player.current_song_index]

class PlayingState(AudioPlayerState):
	def pause(self):
		print('Pausing {}'.format(self.get_current_song()))
		self.audio_player.set_state(PlayingState())

	def stop(self):
		print('Stoping {}'.format(self.get_current_song()))
		self.audio_player.set_state(PlayingState())

class PauseState(AudioPlayerState):
	def play(self):
		print('Resuming {}'.format(self.get_current_song()))
		self.audio_player.set_state(PlayingState())

class StopedState(AudioPlayerState):
	def play(self):
		print('Playing {}'.format(self.get_current_song()))
		self.audio_player.set_state(PlayingState())
		

class AudioPlayer:
	# player data
	songs = ['Song 1', 'Song 2', 'Song 3', 'Song 4']
	
	# state
	__state: 'AudioPlayerState'

	def __init__(self) -> None:
		self.current_song_index = 0
		self.set_state(StopedState())

	def set_state(self, state):
		self.__state = state
		self.__state.audio_player = self


	def play(self):
		self.__state.play()

	def stop(self):
		self.__state.stop()

	def pause(self):
		self.__state.pause()

	def next(self):
		self.__state.next()

	def previous(self):
		self.__state.previous()


def main():
	audio_player = AudioPlayer()
	audio_player.play()
	audio_player.previous()
	audio_player.pause()
	audio_player.next()
	audio_player.play()
	audio_player.stop()


if __name__ == "__main__":
	main()