from slide import Slide


def to_slide_greedy(photos):
    # define target nuber of tags per slide
    number_pics = len(photos)
    number_tags = 0
    for photo in photos:
        number_tags += len(photo.tags)
    target = number_tags/number_pics

    # array containing slides
    slides = []

    # only vertical should remain
    slides, photos = get_horizontal(slides, photos)

    # find matches for vertical pictures
    print("Matching vertical pictures to slides...")
    while len(photos)>1:
        print(len(photos), end="\r", flush=True)
        # look for an "ok" combination of pictures
        photo = photos[0]
        other = 0

        better = False
        i = 1
        while not better:
            num_tags = calc_tags(photo, photos[i])
            if num_tags > target:
                other = i
                better = True
            i+=1

        if other is not 0:
            # if 0 not usefull
            slides.append(Slide(photo,photos[other]))
            photos.pop(other)
            photos.pop(0) 

    # print number of unused pictures
    print(len(photos))
    return slides

def calc_tags(photo1, photo2):
    combined_tags = list(set().union(photo1.tags, photo2.tags))
    return len(combined_tags)

def get_horizontal(slides, photos):
    i = 0
    print("Sorting horizontal pictures...")
    while i < len(photos):
        if photos[i].orientation is 'H':
            # horizontal pictures are the same as a slide
            slides.append(Slide(photos[i]))
            photos.pop(i)
            # one index back so you end up in the next place
            i-=1
        i+=1
    
    return slides, photos
