from sqlobject import *


class Game(SQLObject):
  title = StringCol(length=255, unique=True)
  description = StringCol()
  type = EnumCol(['ISO', 'CSO'])
  path = StringCol()
