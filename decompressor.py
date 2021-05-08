from PIL import Image

data = open('picture.txt', 'r').read().splitlines()

newPic = Image.new('RGBA', (256, 256), color='white')
newPixel = newPic.load()
for d in data:
    print(tuple(d))
    for h in range(256):
        for w in range(256):
            #newPixel[w, h] = tuple(d)
            pass

newPic.save('newPic.png')
