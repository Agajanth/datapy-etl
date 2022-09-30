import pyodbc
from .constants import ODBC_TYPES, STRING_CONN
from ...drivers.utils.utils import contains
from ..base import BaseDriver, BASE_DRIVER

class PostgresDriver(BaseDriver):



    def __init__(self, settings_dict, base_driver: BASE_DRIVER, alias: str = "Postgres"):
        self.DATA_TYPE = {item.name:item.value for item in ODBC_TYPES}  if base_driver == BASE_DRIVER.ODBC else {}
        super() .__init__(settings_dict, base_driver, alias)

    def get_connection_params(self,IS_DNS:bool=False, **kwg):
        if IS_DNS and kwg["DNS"] is not None:
            self.conn_params["DNS"] = kwg["DNS"]
        if not IS_DNS:
            check, are_contained = contains(STRING_CONN, **kwg)
            if are_contained:
                string_conn_params: list[str] = []
                for key in kwg.keys():
                    string_conn_params.append(f"{key}={kwg[key]}")
                self.conn_params = ";".join(string_conn_params)
            else:
                raise Exception(f"These values must be inside de connection string: {check}")


    def get_new_connection(self):
        conn_params = self.conn_params
        if conn_params is None:
            raise Exception("Set connection params to create a connection")
        else:
            if self.base_driver == BASE_DRIVER.ODBC:
                self.connection = pyodbc.connect(self.conn_params)
                return self.connection

    def create_cursor(self):
        if self.connection is not None:
            self.cursor = self.connection.cursor()
        else:
            raise Exception("For creating a cursor the connection must have been created")


