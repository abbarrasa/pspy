from sqlobject import *
#import os


class Format(SQLObject):
    name = StringCol(length=32, unique=True)

    def _set_name(self, value):
        if value and value in ['ISO', 'CSO', 'Eboot']:
            self._SO_set_name(value)
        else:
            raise ValueError('{0} is not a valid format'.format(value))
