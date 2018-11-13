from PIL import Image
from pkg_resources import resource_filename
from urllib.request import urlopen
from settings import Settings
import os
import io

template_file = resource_filename('pspy', 'resources/templates/psp-game-cover-template.png')

class Cover(object):
    def open(self, filename):
        print("Vamos a guardar filename: " + filename)
        if filename:
            if filename.find('://') > 0:
                return Image.open(urlopen(filename))
            else:
                return Image.open(filename)
        else:
            raise ValueError("File name of picture is required")

    def generateThumbnail(self, infile, outfile):
        #background = Image.new('L', (342, 582), 0)
        #background = Image.new('RGBA', (342, 582), (255, 0, 0, 0))
        #print("Create background")
        #self.im.putalpha(background)
        #print("SetAlpha")
        #background.paste(self.im, (2, 11), self.im)
        #print("Paste background")

        im = self.open(infile)
        im.convert("RGBA")
        im.thumbnail((326, 559), Image.ANTIALIAS)
        background = Image.new('RGBA', (342, 582), (255, 255, 255, 0))
        background.paste(im, (2, 11))
        background.show()
        print("Create background")
        foreground = Image.open(template_file)
        print("Open foreground")
        #background.paste(self.im, (2, 11), self.im)
        thumbnail = Image.alpha_composite(background, foreground)
        print("Paste foreground")
        thumbnail.show()
        print("Show")
        try:
            settings = Settings()
            directory = settings.read().get('General', 'thumbnail_directory')
            path = os.path.expanduser(directory)
            os.makedirs(path, exist_ok=True)
            filename = os.path.join(path, outfile + ".thm")
            thumbnail.save(filename, 'PNG')
            print("Saving")
        except IOError:
            print("Cannot create thumbnail")
