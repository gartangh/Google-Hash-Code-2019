class Photo:
	"""A picture"""

	def __init__(self, id, orientation, tags):
        self.id = id
		self.orientation = orientation
		self.tags = tags

	def __str__(self):
		return f'{self.orientation} {self.tags}\n'