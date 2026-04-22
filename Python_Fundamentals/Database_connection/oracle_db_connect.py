# import os

# os.environ["TNS_ADMIN"] = r"C:\oracle\product\10.2.0\client_1\NETWORK\ADMIN"

import oracledb

# oracledb.init_oracle_client(config_dir=r"C:\oracle\product\10.2.0\client_1\NETWORK\ADMIN")
connection = oracledb.connect(
    user="HRMSN_STD06_DEV",
    password="HRMSN_STD06_DEV",
    dsn="HR-T-DB-DEV-1.ad.tlogica.com:1521/dev11g"
)
#connection = oracledb.connect(
#   user="HRMSN_STD06_DEV",
#   password="HRMSN_STD06_DEV",
#   dsn="HR-T-DB-DEV11G"
#)

print("Connected!")

cursor = connection.cursor()
cursor.execute("SELECT sysdate FROM dual")

for row in cursor:
    print(row[0])

cursor.close()
connection.close()