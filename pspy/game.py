class Game(SQLObject):
  title = StringCol(length=255)
  description = StringCol()
  type = EnumCol(['ISO', 'CSO'])
  path = StringCol()
