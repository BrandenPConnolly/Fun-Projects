#Add Columns to dataframe

'''
addcolumns(dataframe)
passes in the data frame needing column names
passes out the dataframe with the column names attached
'''
def addcolumns (dataframe):
    #Brings in the column names
    col = []
    for d in cursor.description:
        col.append(d[0])
    #sets the column names to the correct name
    dataframe.columns = col
    return dataframe
