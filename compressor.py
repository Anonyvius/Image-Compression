from PIL import Image

data = open('picture.txt', 'w+')

InputImage = Image.open('input.png')  # Can be many different formats.
pixel = InputImage.load()
width, height = InputImage.size
#print(width, height)
for h in range(height):
    for w in range(width):
        print(pixel[h, w])
        #print(type(pixel[h, w]))
        data.write(str(pixel[h, w]).replace(',', '').replace('(', '').replace(')', '') + '\n')
        pixel[h, w] = (100, 1, 90, 255)

InputImage.save('alive_parrot.png')
