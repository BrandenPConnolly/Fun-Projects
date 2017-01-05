'''
Creator: Branden Connolly
Create Date: 12/22/2016
Last Edit Date:
Last Editor:
Edits:


Purpose: creates ODBC connection

'''

import pypyodbc as py


'''
connectserver function
passes in server name and database name
creates an ODBC connection to the SQL server requested
'''
def connectserver(server,database) :
    #SQL Server Connection String
    serv = "DRIVER={SQL Server};SERVER="+server+";DATABASE="+database
    #connect to the server
    conn = py.connect(serv)
    return conn

#connects to the server via ODBCConnect.py
conn = connectserver(serv,dbase)
cursor = conn.cursor()


