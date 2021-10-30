from PIL import Image
import math

raw = open('picture', 'r').read().splitlines()
counter = 0

newPic = Image.new('RGBA', (256, 256))
newPixel = newPic.load()

for h in range(256):
    for w in range(256):
        pixel = raw[counter].split(' ')
        newPixel[h, w] = (int(pixel[0]), int(pixel[1]), int(pixel[2]), int(pixel[3]))
        counter += 1

newPic.save('newPic.png')
