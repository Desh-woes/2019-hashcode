from object_file import *
filename = 'a_example.txt'
f = open('files/'+filename, 'r')

total_photos = int(f.readline())

# print(total_photos)
horizontal_images_arr = {}
vertical_images_arr = {}
image_list = []
list_index = 0
for i in range(total_photos):
    read_list = f.readline().split()
    orientation = read_list[0]
    tags = read_list[2:]
    new_object = Image(orientation, tags)
    if orientation == 'H':
        horizontal_images_arr[list_index] = new_object
    else:
        vertical_images_arr[list_index] = new_object
    list_index += 1
    image_list.append(new_object)

# for image in images_arr:
#     print(image)
n_horizontal = len(horizontal_images_arr)
n_vertical = len(vertical_images_arr)


# for image in images_arr:
#     if image.orientation == 'H':
#         n_horizontal += 1
#     elif image.orientation == 'V':
#         n_vertical += 1

total_slides = n_horizontal + n_vertical//2
print(total_slides)

output = open(filename + 'output', 'a')
output.write(str(total_slides) + '\n')

new_slide = Slide(total_slides)
count = 0
while count < total_slides:
    for y in horizontal_images_arr:
        if not horizontal_images_arr[y].used:
            new_slide2 = Indiv_slide(y, horizontal_images_arr[y])
            new_slide.slide_desc.append(new_slide2)
            horizontal_images_arr[y].used = True
            count += 1

    new_arr = []
    for y in vertical_images_arr:
        if not vertical_images_arr[y].used and len(new_arr) < 2:
            new_arr.append(y)
            vertical_images_arr[y].used = True
    new_slide2 = Indiv_slide(new_arr, vertical_images_arr[new_arr[0]], vertical_images_arr[new_arr[1]])
    new_slide.slide_desc.append(new_slide2)
    count += 1

for x in new_slide.slide_desc:
    print(x)


def sortSlideList(slide_list):
    highest_score = 0
    # temp = 0
    highest_index = 0

    for i in range(len(slide_list)):
        if i + 1 < len(slide_list) - 1:
            for j in range(i + 1, len(slide_list)):
                new_score = slide_list[i].score(slide_list[j])
                if new_score > highest_score:
                    highest_score = new_score
                    highest_index = j

            temp = slide_list[i + 1]
            slide_list[i + 1] = slide_list[highest_index]
            slide_list[highest_index] = temp

sortSlideList(new_slide.slide_desc)

for i in range(total_slides):
    output_element = new_slide.slide_desc[i].get_index()
    if not isinstance(output_element, list):
        output.write(str(output_element) + '\n')
    else:
        output.write(' '.join(str(i) for i in output_element) + '\n')