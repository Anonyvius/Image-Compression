from PIL import Image

data = open('picture', 'w+')

InputImage = Image.open('input.png')
pixel = InputImage.load()
width, height = InputImage.size
for h in range(height):
    for w in range(width):
        data.write(str(pixel[h, w]).replace(',', '').replace('(', '').replace(')', '') + '\n')
