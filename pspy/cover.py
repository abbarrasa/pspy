from PIL import Image
from urllib.request import urlopen
import os
import io
import resources


class Cover(object):
    im = None

    def __init__(self, filename):
        print("Vamos a guardar filename: " + filename)
        if filename:
            if filename.find('://') > 0:
                im = Image.open(urlopen(filename))
            else:
                im = Image.open(filename)
                im.thumbnail((326, 559), Image.ANTIALIAS)
        else:
            raise ValueError("File name of picture is required")

        self.im = im

    def generateThumbnail(self, outfile, directory):
        background = Image.new('RGBA', (342, 582), (255, 0, 0, 0))
        print("Create background")
        background.paste(self.im, (2, 11), self.im)
        print("Paste background")
        foreground = Image.open(":/resources/templates/psp-game-cover-template.png")
        background.paste(foreground, (0, 0), foreground)
        print("Paste foreground")
        background.show()
        print("Show")
        try:
            filename = os.path.join(directory, outfile + ".png")
            background.save(filename, 'PNG')
            print("Saving")
        except IOError:
            print("Cannot create thumbnail")
