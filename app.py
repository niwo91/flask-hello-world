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
