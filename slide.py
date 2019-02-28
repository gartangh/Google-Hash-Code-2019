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
			self.tags = list(set(self.tags))

	def __str__(self):
		if self.photo2 is None:
			return f'{self.photo1.id}\n'
		else:
			return f'{self.photo1.id} {self.photo2.id}\n'

	def get_tags(self):
		return self.tags

	@staticmethod
	def get_score(slide1, slide2):
		score1 = len(slide1.tags & slide2.tags)
		score2 = len(slide1.tags) - len(slide1.tags & slide2.tags)
		score3 = len(slide2.tags) - len(slide1.tags & slide2.tags)
		return min(score1, score2, score3)

def make_slideshow(slides):
	slideshow = []
	slide0 = slides.pop()
	slideshow.append(slide0)

	max_score = 0
	nest_slide_index = 0

	while not slides.empty():
		for i1,s1 in ennumerate(slides):
			score = getScore(slide0, s1)
			if score > max_score:
				max_score = score
				nest_slide_index = i1

		slideshow.append(slides.pop(i1))
		slide0 = slideshow[-1]

	return slideshow