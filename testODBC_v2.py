'''
Creator: Branden Connolly
Create Date: 12/22/2016
Last Edit Date: 12/30/2016
Last Editor: Branden Connolly
Edits: cleaning code

Purpose: counts the financial class based on OCM_Coverage
'''
import pandas as pd
import numpy as np

#Server and Database Name
serv = 'aaaaaa'
dbase = 'bbbbbbb'
file1 = "ccccccc"
file2 = "ddddddd"

#Runs the ODBC Connect script    
with open(file1) as f:
    code = compile(f.read(),file1,'exec')
    exec(code)

#Runs the add columns script
with open(file2) as f:
    code = compile(f.read(),file2,'exec')
    exec(code)

#pull data out of the v_OCM_Coverage View
testdata = cursor.execute('Select * From v_OCM_COVERAGE')
testdata = cursor.fetchall()

#puts the outputed data into a dataframe
testdata_df = pd.DataFrame(testdata)

#add columns from addcolumns.py
addcolumns(testdata_df)

#Looks at count of financial classes
op = testdata_df.groupby('financial_class_name').pat_id.count().sort_values(ascending = False)

#Puts in the percentage
test_op = pd.DataFrame(op)
test_op['Count'] = test_op.pat_id
test_op['Total'] = test_op.pat_id.sum()
test_op['Percent (%)'] = np.round((test_op.pat_id.divide(test_op['Total']))*100 ,3)
test_op_df = test_op[['Count','Percent (%)']]

#outputs count
print(test_op_df)

#close connections
conn.close()
cursor.close()

#delete variables
del connectserver
del addcolumns
del serv
del conn
del cursor
del testdata
del testdata_df
del op
del test_op
del test_op_df
