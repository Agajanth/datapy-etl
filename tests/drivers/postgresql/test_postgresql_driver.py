from fast_datapy_etl.drivers.postgresql.driver import PostgresDriver
from fast_datapy_etl.drivers.base.driver import BASE_DRIVER
import pyodbc

def test_driver_class():
    pos = PostgresDriver({},BASE_DRIVER.ODBC,"hi")
    pos.get_connection_params(User="postgres",Driver='{psqlodbcw.so}',Password='admin',Database='postgres',Server='127.0.0.1',Port='5432')
    con = pos.get_new_connection()
    cursor_ = con.cursor().execute("SET TIME ZONE EST")
    assert isinstance(con,pyodbc.Connection)
