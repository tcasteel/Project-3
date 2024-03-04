import psycopg2

def connect_to_database():
    try:
        #Establish connection parameters
        conn = psycopg2.connect(
            dbname= "Project_3",
            user= "postgres",
            password= "postgres",
            host= "localhost",
            port= "5432"
        )

        print("Connected to database successfully.")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connection to PostgreSQL:", error)
        return None
    
connection = connect_to_database()
if connection:
    # Perform database operations
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "industries_db";')
    records = cursor.fetchall()
    for row in records:
        print(row)

    #close cursor and connection
    cursor.close()
    connection.close()