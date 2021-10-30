from PIL import Image

raw = open('picture', 'r').read().splitlines()
counter = 0

newPic = Image.new('RGBA', (256, 256))
newPixel = newPic.load()

for h in range(256):
    for w in range(256):
        newPixel[h, w] = eval(raw[counter])
        counter += 1

newPic.save('newPic.png')
