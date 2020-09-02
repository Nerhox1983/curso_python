import pyodbc
server = 'P-SCACERES \MSSQLSERVER2017'
database = 'SJCC'

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=P-SCACERES\MSSQLSERVER2017;'
    r'DATABASE=SJCC;'
    r'Trusted_Connection=yes;'
    )
conn = pyodbc.connect(conn_str)
#read(conn)

print ("Reading")
cursor = conn.cursor()
cursor.execute("Select * from hitos")
for row in cursor:
    print (f'row = {row}')


