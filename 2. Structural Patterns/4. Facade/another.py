# Notification via Email
class EmailBackEnd:
	pass

class EmailNotification:
	def __init__(self, backend):
		self.backend = backend

	def send_mail(self, email, subject, content):
		print("Sending mail to {} with subject {}".format(email, subject))

# Notification via SMS

class SMSNotification:
	
	def send_sms(self, phonenumber, text):
		print("Sending sms to {} with text {}".format(phonenumber, text))

# Notification via Browser

class WebNotification:
	def __init__(self, token):
		self.token = token

	def notify(self, message):
		print("Sending notification to Web")

# Notification via App

class AppNotification:
	def __init__(self, token):
		self.token = token

	def notify(self, message):
		print("Sending notification to App")

# Save notification to database

class DatabaseNotification:
	
	def save(self, user, notification):
		print("Saving notification \"{}\" of user {} to database".format(notification, user))

class User:
	"""
	Test user that contains
	phone number
	email
	firebase messaging token
	"""
	def __str__(self):
		return "Ajesh"

	def get_phonenumber(self):
		return 9842531999
	
	def get_email(self):
		return 'aj3sshh@gmail.com'

	def get_fcm_token(self):
		return 'ab67df1c7d'

	

class Notifier:
	"""
	Notification sender Facade class
	"""

	def send_notification(self, user, notification_message):
		"""
		sends notification through all medium
		"""

		# sending email notification
		email_backend = EmailBackEnd()
		email_notification = EmailNotification(backend=email_backend)
		email_notification.send_mail(
			email=user.get_email(), 
			subject='You have new notification',
			content=notification_message
		)

		# sending sms notification
		sms_notification = SMSNotification()
		sms_notification.send_sms(user.get_phonenumber(), notification_message)

		# sending web notification
		web_notification = WebNotification(token=user.get_fcm_token())
		web_notification.notify(notification_message)

		# sending app notification
		app_notification = AppNotification(token=user.get_fcm_token())
		app_notification.notify(notification_message)

		# saving notification to database
		database_notification = DatabaseNotification()
		database_notification.save(user=user, notification=notification_message)


# using facade
user = User()
notifier = Notifier()
notifier.send_notification(user, 'You have a new message from your Friend')