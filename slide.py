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
			return f'{self.photo1.id}\n'
		else:
			return f'{self.photo1.id} {self.photo2.id}\n'
			
	def getTags(self):
		return self.tags

	@staticmethod
	def getScore(slide1, slide2):
		score1 = len(slide1.tags & slide2.tags)
		score2 = len(slide1.tags) - len(slide1.tags & slide2.tags)
		score3 = len(slide2.tags) - len(slide1.tags & slide2.tags)
		return min(score1, score2, score3)