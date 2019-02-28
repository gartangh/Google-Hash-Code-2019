from photo import Photo

class Slide:
	"""A slide"""

	def __init__(self, photo1, photo2=None):
		self.photo1 = photo1
		self.photo2 = photo2

		self.tags = []
		self.tags.extend(photo1.tags)

		if photo2 is not None:
			self.tags.extend(photo2.tags)

	def __str__(self):
		if self.photo2 is None:
			return f'{self.photo1}\n'
		else:
			return f'{self.photo1} {self.photo2}\n'
			
	def getTags(self):
		return self.tags
