from sqlobject import *
from math import log
#import os


class Game(SQLObject):
	title = StringCol(length=255, unique=True)
	description = StringCol(length=511, default=None)
	comment = StringCol(default=None)
	format = EnumCol(['ISO', 'CSO', 'Eboot'])
	size = IntCol()
	path = StringCol()
	cover = BlobCol(default=None)
	
	def humanReadableSize(n, pow=0, b=1024, u='B', pre=['']+[p+'i'for p in'KMGTPEZY']):
		pow,n=min(int(log(max(n*b**pow,1),b)),len(pre)-1),n*b**pow
		return "%%.%if %%s%%s"%abs(pow%(-pow-1))%(n/b**float(pow),pre[pow],u)	
		
#    def imageFilename(self):
#        return 'covers/game-%s.jpg' % self.id

#    def _get_cover(self):		
#		with open(filename, 'wb') as output_file:
#			output_file.write(ablob)
		
#        if not os.path.exists(self.imageFilename()):
#            return None
#        f = open(self.imageFilename())
#        v = f.read()
#        f.close()
#        return v

#    def _set_cover(self, value):
#        # assume we get a string for the image
#        f = open(self.imageFilename(), 'w')
#        f.write(value)
#        f.close()

#    def _del_cover(self, value):
#        os.unlink(self.imageFilename())	
