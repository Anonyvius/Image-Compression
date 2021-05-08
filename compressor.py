from PIL import Image

data = open('picture.txt', 'w+')

InputImage = Image.open('input.png')  # Can be many different formats.
pixel = InputImage.load()
width, height = InputImage.size
for h in range(height):
    for w in range(width):
        print(pixel[w, h])
        data.write(str(pixel[w, h]).replace(',', '').replace('(', '').replace(')', '') + '\n')
        # pixel[w, h] = (11, 38, 80, 255)

# InputImage.save('alive_parrot.png')
