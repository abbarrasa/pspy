class Game(SQLObject):
  title = StringCol()
  description = StringCol()
  type = EnumCol(['ISO', 'CSO'])
