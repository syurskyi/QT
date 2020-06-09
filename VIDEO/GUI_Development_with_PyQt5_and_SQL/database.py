from PyQt5 import QtSql
from PyQt5.QtWidgets import *

class Database:
    is_instance = False
    
    def __init__(self):
        if not Database.is_instance:
            print('Database has been instantiated')
            self.db = QtSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('database.db')
            self.open()
            Database.is_instance = True
        else:
            print('Has already been created')