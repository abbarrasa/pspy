from sqlobject import *
import os


class Database(SQLObject):	
	def connect(self, db_filename):
		path_to_db = os.path.abspath(db_filename)		
		uri = 'sqlite3:{0}'.format(path_to_db)
		#Create and open connection to a database file.
		sqlhub.processConnection = connectionForURI(uri)
 				
	def createTables(self):
		for entity in (Game):
			entity.createTable(ifNotExists=True)
			
	def close(self):
		#close connection
		sqlhub.processConnection.close()
		
