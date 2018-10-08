import sqlite3


class Database:
	
	def createTables():
		for table in (Game):
			table.createTable(ifNotExists=True)

	def connect(database):
		try:
			bd = sqlite3.connect(database)
			cursor = bd.cursor()
			print("Connected to database successfuly")
		except 
