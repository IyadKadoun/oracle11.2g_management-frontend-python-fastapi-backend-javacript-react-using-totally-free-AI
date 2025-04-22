import oracledb
from sqlalchemy import create_engine

#DATABASE_URL = "oracle+oracledb://sbcm:SbcMRkdjdvASAB@HASSAN:1521/?service_name=reef"

try:
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_11_2")
    conn = oracledb.connect(
        user="sbcm",
        password="SbcMRkdjdvASAB",
        dsn="HASSAN:1521/reef"  # or ":1521/ORCL" for service name
    )
    print("Success! Oracle version:", conn.version)
    conn.close()
except Exception as e:
    print("Failed:", e)