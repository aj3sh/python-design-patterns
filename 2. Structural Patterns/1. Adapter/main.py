import abc

class CameraCard:
	def save(self, image):
		pass

class SDCard(CameraCard):
	def save(self, image):
		print('Saving image {} on SD Card'.format(image))

class MicroSDCard:
	def save_image(self, image, filename):
		print('Saving image {} on MICRO SD Card'.format(filename))

class MicroSDCardAdapter(CameraCard):
	
	def __init__(self, micro_sd_card):
		self.__micro_sd_card = micro_sd_card
	
	def save(self, image):
		self.__micro_sd_card.save_image(
			image, 
			filename=self.get_filename(image)
		)

	def get_filename(self, image):
		# returns filename from image
		return image

class Camera:
	__card = None

	def insert_card(self, card):
		self.__card = card

	def click(self):
		if self.__card == None:
			raise Exception('No card available')
		image = self.get_clicked_image()
		self.__card.save(image=image)

	def get_clicked_image(self):
		from datetime import datetime
		return str(datetime.now())+'.JPEG'


def main():
	# this is my camera
	my_camera = Camera()

	print('Using Normal SD Card')
	memory_card = SDCard()
	my_camera.insert_card(memory_card)
	my_camera.click()

	print('Using Micro SD Card')
	memory_card = MicroSDCardAdapter(MicroSDCard())
	my_camera.insert_card(memory_card)
	my_camera.click()


if __name__ == "__main__":
	main()