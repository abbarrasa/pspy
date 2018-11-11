from sqlobject import *
#import os


class Game(SQLObject):
    title = StringCol(length=255, unique=True)
    description = StringCol(length=511, default=None)
    comment = StringCol(default=None)
    cover = BLOBCol(default=None)
    format = StringCol(length=15)
    size = IntCol()
    path = StringCol()

    def _set_title(self, value):
        if value:
            self._SO_set_title(value)
        else:
            raise ValueError('Title is required')

    def _set_description(self, value):
        if value:
            self._SO_set_description(value)

    def _set_format(self, value):
        if value and value in ['ISO', 'CSO', 'Eboot']:
            self._SO_set_format(value)
        else:
            raise ValueError('{0} is not a valid format'.format(value))

    def _set_size(self, value):
        if value and value > 0:
            self._SO_set_size(value)
        else:
            raise ValueError('Size must be greater than 0')

    def _set_comment(self, value):
        if value:
            self._SO_set_comment(value)

    def _set_path(self, value):
        if value:
            self._SO_set_path(value)
        else:
            raise ValueError('Path is required')

    def _set_cover(self, value):
        if value:
            self._SO_set_cover(value)

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
