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
    def __init__(self,index, imageA, imageB=None):
        self.index = index
        self.tags = set(imageA.tag_arr)
        if imageB is not None:
            self.tags.update(imageB.tag_arr)

    def get_index(self):
        return self.index

    def score(self, slide_B):
        common = self.tags.intersection(slide_B.tags)
        in_A = self.tags.difference(slide_B.tags)
        in_B = slide_B.tags.difference(self.tags)
        arr = [len(common), len(in_A), len(in_B)]
        score = min(arr)
        return score


