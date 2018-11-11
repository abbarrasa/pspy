from PIL import Image
from urllib.request import urlopen
import os
import io
import resources


class Cover(object):
    im = None

    def __init__(self, filename=None, raw=None):
        print("Vamos a guardar filename")
        if filename:
            if filename.find('://') > 0:
                im = Image.open(urlopen(filename))
            else:
                im = Image.open(filename)
                im.thumbnail((326, 559), Image.ANTIALIAS)
        elif raw:
            im = Image.frombytes('RGBA', (326, 559), raw)
        else:
            raise ValueError("File name or raw bytes pictures is required")

        self.im = im

    def save(self, outfile, directory):
        filename = os.path.join(directory, outfile + ".png")
        self.im.save(filename, 'PNG')

    def raw(self):
        output = io.BytesIO()
        self.im.save(output, format='PNG')
        return output.getvalue()

    def generateThumbnail(self, outfile, directory):
        background = Image.new('RGBA', (342, 582), (255, 0, 0, 0))
        background.paste(self.im, (2, 11), self.im)
        foreground = Image.open(":/resources/templates/psp-game-cover-template.png")
        background.paste(foreground, (0, 0), foreground)
        background.show()
        try:
            filename = os.path.join(directory, outfile + ".png")
            background.save(filename, 'PNG')
        except IOError:
            print("Cannot create thumbnail")
