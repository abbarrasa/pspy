import sqlite3


class Database:

	def connect(database):
		try:
			bd = sqlite3.connect(database)
			cursor = bd.cursor()
			print("Connected to database successfuly")
		except 