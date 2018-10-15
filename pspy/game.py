from sqlobject import *
#from math import log
#import os
import humanize
import sys
assert (sys.maxsize & (sys.maxsize+1)) == 0 # checks that maxsize+1 is a power of 2


class Game(SQLObject):
    title = StringCol(length=255, unique=True)
    description = StringCol(length=511, default=None)
    comment = StringCol(default=None)
    cover = BLOBCol(default=None)
    format = StringCol(length=15)
    size = IntCol()
    path = StringCol()

    def humanReadableSize(self, binary=False, gnu=False):
        return humanize.naturalsize(self.size)

    def _set_format(self, value):
        if value in ['ISO', 'CSO', 'Eboot']:
            self._SO_set_format(value)
        else:
            raise ValueError(
                '{0} is not a valid format'.format(value)
            )

    def __hash__(self):
        if self.id is None:
            raise ValueError('It cannot be hashed because it has not id')
        else:
            return hash((self.id, self.title)) & sys.maxsize

#	def _set_cover(self, value):
#        self._SO_set_cover(value.encode('base64'))

#    def _get_cover(self, value):
#        return self._SO_get_cover().decode('base64')		
		
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
