from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Database connection parameters
dbname = "Project_3"
user = "postgres"
password = "postgres"
host = "localhost"  
port = "5432"       

@app.route('/')
def index():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    
   # Execute a sample SQL query
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM industries_db")
    rows = cursor.fetchall()



    # Close cursor and connection
    cursor.close()
    conn.close()
    # Pass the data to the template
    return render_template('idea.html', rows=rows)
if __name__ == '__main__':
    app.run(debug=True)