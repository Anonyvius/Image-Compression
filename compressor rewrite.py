from PIL import Image

data = open('pictureNEW', 'w+')

InputImage = Image.open('input.png')
pixel = InputImage.load()
width, height = InputImage.size
for h in range(height):
    for w in range(width):
        toWrite = data.write(str(pixel[h, w]) + '\n')
        
