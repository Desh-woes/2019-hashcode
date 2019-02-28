from object_file import Image
f = open('files/a_example.txt', 'r')

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

