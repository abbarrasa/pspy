from sqlobject import *
from pspy.game import Game
import os


class Database(SQLObject):
	def connect(db_filename):
		path_to_db = os.path.abspath(db_filename)
		uri = 'sqlite:{0}'.format(path_to_db)
		#Create and open connection to a database file.
		sqlhub.processConnection = connectionForURI(uri)

	def createTables():
		for entity in (Game):
			entity.createTable(ifNotExists=True)

	def close():
		#close connection
		sqlhub.processConnection.close()

