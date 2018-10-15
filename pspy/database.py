from sqlobject import sqlhub, connectionForURI
from pspy.game import Game
import os


class Database(object):
	def connect(self, db_filename):
		path_to_db = os.path.expanduser(db_filename)
		uri = 'sqlite:{0}'.format(path_to_db)
		#Create and open connection to a database file.
		sqlhub.processConnection = connectionForURI(uri)
		print("Connected to: " + uri)		

	def createTables(self):
		Game.createTable(ifNotExists=True)

	def close(self):
		#close connection
		sqlhub.processConnection.close()

