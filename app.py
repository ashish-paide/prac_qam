from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from pypyodbc import odbc
import pandas as pd
from pypyodbc import connect

app = Flask(__name__)




# Database configuration
server = 'bootcampjuly1server.database.windows.net'
database = 'bootcampjuly2024db'
username = 'bootcamp'
password = 'Pass@123'

# Define the connection string
connection_str = f'Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'


def retrieve_customer_table():
    # Establish connection
    conn = connect(connection_str)

    # Define your SQL query
    query = 'SELECT TOP 20 * FROM [SalesLT].[Customer]'

    # Execute query
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch all rows from the query result
    dataset = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    pdbd = pd.DataFrame(dataset ,columns=columns)
    # Close cursor and connection
    cursor.close()
    conn.close()

    # Render template or return data as needed
    return pdbd

def retieve_joined_table():
    # Establish connection
    conn = connect(connection_str)

    # Define your SQL query
    query = '''SELECT TOP 20
                p.Name AS product,
                p.Color AS color,
                p.Size AS size,
                p.Weight AS weight
                FROM
                [SalesLT].[ProductCategory] pc
                JOIN
                [SalesLT].[Product] p ON pc.ProductCategoryID = p.ProductCategoryID;'''

    # Execute query
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch all rows from the query result
    dataset = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    pdbd = pd.DataFrame(dataset ,columns=columns)
    # Close cursor and connection
    cursor.close()
    conn.close()

    # Render template or return data as needed
    return pdbd

@app.route('/')
def index():
    images = ['https://th.bing.com/th/id/R.57f3234f65f0f327e7b86860c5cebd71?rik=J70r%2fLnMW4FTWQ&riu=http%3a%2f%2fs1.picswalls.com%2fwallpapers%2f2016%2f06%2f10%2fhd-4k-wallpaper_065239257_309.jpg&ehk=RWo6wC7ClTZZ%2fTcTlBc58QaARl9LC0f4cJz9A0EjB2A%3d&risl=1&pid=ImgRaw&r=0',
              'https://wallpaperaccess.com/full/38580.jpg',
              'https://wallpaperaccess.com/full/2180654.jpg']
    return render_template('task_1.html', images=images)

@app.route('/task_1')
def task_1():
    images = ['https://th.bing.com/th/id/R.57f3234f65f0f327e7b86860c5cebd71?rik=J70r%2fLnMW4FTWQ&riu=http%3a%2f%2fs1.picswalls.com%2fwallpapers%2f2016%2f06%2f10%2fhd-4k-wallpaper_065239257_309.jpg&ehk=RWo6wC7ClTZZ%2fTcTlBc58QaARl9LC0f4cJz9A0EjB2A%3d&risl=1&pid=ImgRaw&r=0',
              'https://wallpaperaccess.com/full/38580.jpg',
              'https://wallpaperaccess.com/full/2180654.jpg']
    
    return render_template('task_1.html', images=images)

@app.route('/task_2')
def task_2():
    
    db = retrieve_customer_table()
    table_html = db.to_html(classes='table table-striped', index=False)
    table_html = [table_html , db]
    print(type(db))
    return render_template('task_2.html', table_html=table_html)

@app.route('/task_3')
def task_3():
    db = retieve_joined_table()

    table_html = db.to_html(classes='table table-striped', index=False)
    table_html = [table_html , db]
    print(type(db))
    return render_template('task_3.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
