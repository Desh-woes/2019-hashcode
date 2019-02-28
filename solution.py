from object_file import Image, Slide
f = open('files/e_shiny_selfies.txt', 'r')

total_photos = int(f.readline())

# print(total_photos)
images_arr = []

for i in range(total_photos):
    read_list = f.readline().split()
    orientation = read_list[0]
    tags = read_list[2:]
    new_object = Image(orientation, tags)
    images_arr.append(new_object)

# for image in images_arr:
#     print(image)
n_horizontal = 0
n_vertical = 0
for image in images_arr:
    if image.orientation == 'H':
        n_horizontal += 1
    elif image.orientation == 'V':
        n_vertical += 1

total_slides = n_horizontal + n_vertical//2
print(total_slides)

output = open('output', 'a')
output.write(str(total_slides) + '\n')

new_slide = Slide(total_slides)
count = 0
while count < total_slides:
    for y in images_arr:
        if not y.used and y.orientation == "H":
            new_slide.slide_desc.append(images_arr.index(y))
            y.used = True
            count += 1

    new_arr = []
    for y in images_arr:
        if not y.used and y.orientation == "V" and len(new_arr) < 2:
            new_arr.append(images_arr.index(y))
            y.used = True
    new_slide.slide_desc.append(new_arr)
    count += 1

for i in range(total_slides):
    output_element = new_slide.slide_desc[i]
    if not isinstance(output_element, list):
        output.write(str(output_element) + '\n')
    else:
        output.write(' '.join(str(i) for i in output_element) + '\n')








