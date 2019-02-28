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
