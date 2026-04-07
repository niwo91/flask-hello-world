from flask import Flask
app = Flask(__name__)
import psycopg2

@app.route('/')
def hello_world():
    return 'Hello World from Nicholas Woody in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://nick:ZwHsLj5AY0n4bZxrIFxL8zZAPUt4DDBD@dpg-d7aj19fkijhs73dodnk0-a/nickdb_lvej")

    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://nick:ZwHsLj5AY0n4bZxrIFxL8zZAPUt4DDBD@dpg-d7aj19fkijhs73dodnk0-a/nickdb_lvej")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Succesfully Created"


@app.route('/db_insert')
def db_test():
    conn = psycopg2.connect("postgresql://nick:ZwHsLj5AY0n4bZxrIFxL8zZAPUt4DDBD@dpg-d7aj19fkijhs73dodnk0-a/nickdb_lvej")
    cur.execute('''                                                                                                                          
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')                                                                                                                                     
    conn.commit() 
    conn.close()
    return "Basketball Table Succesfully Populated"


@app.route('/db_select')
def db_test():
    conn = psycopg2.connect("postgresql://nick:ZwHsLj5AY0n4bZxrIFxL8zZAPUt4DDBD@dpg-d7aj19fkijhs73dodnk0-a/nickdb_lvej")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+=f"<td>{info}</td>"
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def db_test():
    conn = psycopg2.connect("postgresql://nick:ZwHsLj5AY0n4bZxrIFxL8zZAPUt4DDBD@dpg-d7aj19fkijhs73dodnk0-a/nickdb_lvej")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
