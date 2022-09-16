from __future__ import (absolute_import, division, print_function)
from factory import DBType, FactoryDriverInterface
from typing import Optional
#import Logging
import pyodbc

class SQLServer(FactoryDriverInterface):

    __connection = None
    def __init__(self,driver: DBType, database:str, **kwargs):
        try:
            self.__DRIVER = driver
            self.__DATABASE = database
            if kwargs:
                for key,val in kwargs.items():
                    setattr(self, '_' + self.__class__.__name__ + '__'+key, val)
        except ValueError as e:
            print(f'Error trying to initialize SQL server with error: {e}')

    def __str__(self):
        return str(self.__dict__)

    def create_connection(self):
        self.__connection = False
        conn_str = (
        "DRIVER={psqlodbcw.so};"
        "trusted_connection=tcon;"
        "DATABASE=postgres;"
        "UID=postgres;"
        "PWD=postgres;"
        "SERVER=0.0.0.0;"
        "PORT=5432"
        )
        conn = pyodbc.connect(conn_str)
        print(conn)



    def kill_connection(self):
        pass

    def getData(self):
        pass

    @classmethod
    def get_string_connection(cls,*args):
        return ";".join([arg for arg in args])

server = SQLServer('Driver','test',UID = 'Hola', DSN = 'Holamundo')

server.create_connection()
print(server)
