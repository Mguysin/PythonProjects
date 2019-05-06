import pyodbc

#Our variable to create a connection

server = 'localhost,1433'
database = 'Pokemon'
username = 'SA'
password = 'Passw0rd2018'



#Making a connection
docker_Pokemon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#Creating a cursor that can execute SQL funtions on connected db
cursor = docker_Pokemon.cursor()

# Executing the SQL
cursor.execute("SELECT * FROM player")

#Getting the rows out of the results of the execution

rows = cursor.fetchall()

description = cursor.description

# print(len(rows))
#
# print(type(rows))



for row in rows:

    print(row.Name)

#
#
def sql_query_no_transaction(sql_query):
    return cursor.execute(sql_query)

