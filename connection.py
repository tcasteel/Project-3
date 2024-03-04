from flask import Flask, render_template
import psycopg2
from flask import request

app = Flask(__name__)

# Database connection parameters
dbname = "Project_3"
user = "postgres"
password = "postgres"
host = "localhost"  
port = "5432"       

@app.route('/', methods =['GET','POST'])
def index():
    if request.method == 'POST':
        selected_year = request.form['year']
        selected_industry = request.form['industry']  

        # Connect to the database
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    
        # Construct dynamic SQL query
        query = "SELECT * FROM industries_db WHERE year = %s AND industry = %s"

        # Execute query with parameters
        cursor = conn.cursor()
        cursor.execute(query, (selected_year, selected_industry))
        rows = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Pass the data to the template
        return render_template('idea.html', rows=rows)
    return render_template('idea.html')

if __name__ == '__main__':
    app.run(debug=True)