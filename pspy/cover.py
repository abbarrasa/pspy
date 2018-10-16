from PIL import Image
from urllib.request import urlopen
import os


class Cover(object):
	size = 326, 559
	
	def __init__(self, filename):
		if (filename.find('://') > 0):
			im = Image.open(urlopen(filename))
		else:
			im = Image.open(filename)
		outfile = os.path.splitext(infile)[0] + ".thumbnail"
		if infile != outfile:
			try:
				im = Image.open(infile)
				im.thumbnail(size, Image.ANTIALIAS)
				im.save(outfile, "JPEG")
			except IOError:
				print "cannot create thumbnail for '%s'" % infile			
			
	def raw(self):
		output = io.BytesIO()
		self.im.save(output, format='JPEG')
		return output.getvalue()
		
	def generateThumbnail(self, outfile, dir_name):
		background = Image.open("test1.png")
		background.paste(self.im, (0, 0), self.im)
		background.show()
		try:
			filename = os.path.join(dir_name, outfile + ".thumbnail")
			background.save(filename, "JPEG")
		except IOError:
			print "Cannot create thumbnail"
