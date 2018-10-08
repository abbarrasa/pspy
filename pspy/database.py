from sqlobject import *


class Database:	
	def connect(path_to_db):
		#Create and open connection to a database file.
		sqlhub.processConnection = connectionForURI('sqlite3:'+path_to_db)
 				
	def createTables():
		for table in (Game):
			table.createTable(ifNotExists=True)
			
	def close():
		#close connection
		sqlhub.processConnection.close()		
		
