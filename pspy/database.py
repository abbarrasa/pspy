from sqlobject import sqlhub, connectionForURI
from game import Game
from format import Format
import os


class Database(object):
    def connect(self, db_filename):
        self.path_to_db = os.path.expanduser(db_filename)
        uri = 'sqlite:{0}'.format(self.path_to_db)
        # Create and open connection to a database file.
        sqlhub.processConnection = connectionForURI(uri)
        print("Connected to: " + uri)

    def getDatabasePath(self):
        return self.path_to_db

    def createSchema(self):
        Format.createTable(ifNotExists=True)
        Game.createTable(ifNotExists=True)

    def close(self):
        # Close connection
        sqlhub.processConnection.close()
