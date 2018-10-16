from PIL import Image
from urllib.request import urlopen
import os


class Cover(object):
	im = None
	def __init__(self, filename):
		if (filename.find('://') > 0):
			im = Image.open(urlopen(filename))
		else:
			im = Image.open(filename)
			
		im.thumbnail((326, 559), Image.ANTIALIAS)
		self.im = im
			
	def raw(self):
		output = io.BytesIO()
		self.im.save(output, format='JPEG')
		return output.getvalue()
		
	def generateThumbnail(self, outfile, dir_name):
		background = Image.new('RGBA', (342, 582), (255, 0, 0, 0))
		background.paste(self.im, (2, 11), self.im)
		foreground = Image.open("psp-game-cover-template.png")
		background.paste(foreground, (0, 0), foreground)
		background.show()
		try:
			filename = os.path.join(dir_name, outfile + ".thumbnail")
			background.save(filename, "JPEG")
		except IOError:
			print "Cannot create thumbnail"
