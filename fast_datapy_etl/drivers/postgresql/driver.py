from ..base.driver import BaseDriver, BASE_DRIVER
import pyodbc
import psycopg3
from .constants import ODBC_TYPES
class PostgresDriver(BaseDriver):



    def __init__(self, settings_dict, base_driver: BASE_DRIVER, alias: str = "Postgres"):
        self.DATA_TYPE = {item.name:item.value for item in ODBC_TYPES}  if base_driver == BASE_DRIVER.ODBC else {}
        super() .__init__(settings_dict, base_driver, alias)

    def get_connection_params(self, **kwg):


    def get_new_connection(self, conn_params):
        return


