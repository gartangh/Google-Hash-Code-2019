# imports
from photo import Photo
from slide import Slide
from toslide import verticalslide


# main
if __name__ == '__main__':

	photos = []

	with open('in/a_example.txt') as file_in:
		N = int(file_in.readline().split()[0])

		for i in range(N):
			line = file_in.readline().split()
			tags = []
			for j in range(int(line[1])):
				tags.append(line[j+2])
			photos.append(Photo(i, line[0], tags))

	slides = verticalslide(photos)
	slideshow = make_slideshow(slides)

	with open('out/a_example.txt', 'w') as file_out:
		file_out.write(f'{len(slides)}\n')
		for slide in slides:
			file_out.write(str(slide))
