class LowBattery(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return self.message


class FullTrashTank(Exception):
	def __init__(self, message):
		self.message = message


class EmptyWatterTank(Exception):
	def __init__(self, message):
		self.message = message
