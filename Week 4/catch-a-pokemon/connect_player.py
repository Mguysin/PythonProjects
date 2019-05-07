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
#

#
#
def sql_query_no_transaction(sql_query):
    return cursor.execute(sql_query)

