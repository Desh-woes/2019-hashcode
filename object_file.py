class Image:
    def __init__(self, orientation, tag_arr):
        self.orientation = orientation
        self.tag_arr = tag_arr
        self.n_tags = len(tag_arr)
        self.used = False

    def __str__(self):
        return self.orientation + ' ' + str(self.n_tags) + ' ' + ' '.join(i for i in self.tag_arr)

class Slide:
    def __init__(self, total):
        self.total_slides = total
        self.slide_desc = []
class Indiv_slide:
    def __init__(self,imageA,imageB=None):
        self.tags=set(imageA.tag_arr)
        if imageB is not None:
            self.tags.update(imageB.tag_arr)

def score(slide_A,slide_B):
    common=slide_A.tags.intersection(slide_B.tags)
    in_A=slide_A.tags.difference(slide_B.tags)
    in_B = slide_B.tags.difference(slide_A.tags)
    arr=[len(common),len(in_A),len(in_B)]
    score=min(arr)
    return score

