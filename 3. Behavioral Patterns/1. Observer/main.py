'''
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
'''

import abc

class ObserverSubject(metaclass=abc.ABCMeta):
	observers:list

	def __init__(self):
		self.observers = []

	def register(self, observer:'Observer'):
		self.observers.append(observer)

	def unregister(self, observer:'Observer'):
		self.observers.remove(observer)

	def notifyObservers(self):
		for observer in self.observers:
			observer.observe(self)


class CricketData(ObserverSubject):
	runs:int
	wickets:int
	overs:float

	def __init__(self) -> None:
		self.runs, self.wickets, self.overs = 0, 0, 0
		super().__init__()

	def set_runs(self, runs) -> None:
		self.runs = runs
		self.notifyObservers()

	def set_wickets(self, wickets) -> None:
		self.wickets = wickets
		self.notifyObservers()

	def set_overs(self, overs) -> None:
		self.overs = overs
		self.notifyObservers()
	


class Observer(metaclass=abc.ABCMeta):
	def observe(self, instance:ObserverSubject):
		raise NotImplementedError('The method "observe" method is not implemented.');

class CurrentScoreDisplay(Observer):
	runs:int
	wickets:int
	overs:float

	def observe(self, instance:ObserverSubject):
		self.runs = instance.runs
		self.wickets = instance.wickets
		self.overs = instance.overs

	def display(self):
		print('Score: {}/{} in {} overs'.format(self.runs, self.wickets, self.overs))

class AverageScoreDisplay(Observer):
	run_rate:float
	predicted_score:int

	def __init__(self) -> None:
		self.run_rate, self.predicted_score = 0, 0

	def observe(self, instance: ObserverSubject):
		if instance.overs == 0: return
		self.run_rate = instance.runs/instance.overs
		self.predicted_score = self.run_rate * 20 # assuming 20 overs in total

	def display(self):
		print('Run rate: {}'.format(self.run_rate))
		print('Predicted score: {}'.format(self.predicted_score))

def main():
	# creating subject
	data = CricketData()

	# creating observer
	current_score = CurrentScoreDisplay()
	average_score = AverageScoreDisplay()
	
	# registering observer
	data.register(current_score)
	data.register(average_score)

	# setting data
	data.set_runs(70)
	data.set_overs(5)
	data.set_wickets(2)

	current_score.display()
	average_score.display()



if __name__ == "__main__":
	main()