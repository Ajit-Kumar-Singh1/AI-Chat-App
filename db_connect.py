import pyodbc

def get_db_connection():
    server = 'DYNAMITE'
    database = 'CMDBTracker'
    username = 'sa'
    password = '5588'
    
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + 
        ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
    )
    return connection

def query_db(query):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()
    return rows
