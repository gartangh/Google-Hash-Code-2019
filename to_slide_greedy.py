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

    # sort photos by number of tags
    photos = bucketSort(photos)

    while len(photos)>1:
        slides.append(Slide(photos[0], photos[len(photos)-1]))
        photos.pop(len(photos)-1)
        photos.pop(0)

    return slides

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

def bucketSort(photos): 
    arr = [] 

    # find max amount of tags
    slot_num = 0
    for s in photos:
    	n_tags = len(s.tags)
    	if slot_num < n_tags:
    		slot_num = n_tags
    
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for s in photos:
        arr[len(s.tags)-1].append(s) 
    
    x = []
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x.append(arr[i][j])
            k += 1
    return x 