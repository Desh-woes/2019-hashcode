from object_file import *
filename = 'e_shiny_selfies.txt'
f = open('files/'+filename, 'r')

total_photos = int(f.readline())

# print(total_photos)
horizontal_images_arr = {}
vertical_images_arr = {}
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
            new_silde = Indiv_slide
            new_slide.slide_desc.append(y)
            horizontal_images_arr[y].used = True
            count += 1

    new_arr = []
    for y in vertical_images_arr:
        if not vertical_images_arr[y].used and len(new_arr) < 2:
            new_arr.append(y)
            vertical_images_arr[y].used = True
    new_slide.slide_desc.append(new_arr)
    count += 1

for i in range(total_slides):
    output_element = new_slide.slide_desc[i]
    if not isinstance(output_element, list):
        output.write(str(output_element) + '\n')
    else:
        output.write(' '.join(str(i) for i in output_element) + '\n')