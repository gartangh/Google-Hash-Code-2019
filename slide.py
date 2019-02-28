class Slide:
	"""A slide"""

	def __init__(self, photo1, photo2=None):
		self.photo1 = photo1
		self.photo2 = photo2

	def __str__(self):
		if self.photo2 is None:
			return f'{self.photo1}\n'
		else:
			return f'{self.photo1} {self.photo2}\n'

