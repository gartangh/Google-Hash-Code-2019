# imports
from photo import Photo
from slide import Slide
from toslide import toSlide

file_names = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
file_index = 2

# main
if __name__ == '__main__':

	photos = []

	with open('in/{}.txt'.format(file_names[file_index])) as file_in:
		N = int(file_in.readline().split()[0])

		for i in range(N):
			line = file_in.readline().split()
			tags = []
			for j in range(int(line[1])):
				tags.append(line[j+2])
			photos.append(Photo(i, line[0], tags))

	slides = toSlide(photos)
	slideshow = Slide.make_slideshow(slides)

	with open('out/{}.txt'.format(file_names[file_index]), 'w') as file_out:
		file_out.write(f'{len(slideshow)}\n')
		for slide in slideshow:
			file_out.write(str(slide))
