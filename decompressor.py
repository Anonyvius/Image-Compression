from PIL import Image

data = open('picture.txt', 'r').read().splitlines()

newPic = Image.new('RGBA', (256, 256), color='white')
#newPic.save('newPic.png')
newPixel = newPic.load()
for d in data:
    pixel = d.split(' ')
    newTuple = (pixel[0], pixel[1], pixel[2], pixel[3])
    #print(newTuple)
    for h in range(256):
        for w in range(256):
            newPixel[w, h] = 1

newPic.save('newPic.png')
