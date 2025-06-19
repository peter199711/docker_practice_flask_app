import os
import pymysql
from flask import Flask, render_template

app = Flask(__name__)

def get_data_from_mysql():
    conn = pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASS', 'P@ssw0rd'),
        database=os.getenv('DB_NAME', 'my_titanic'),
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT pname, age FROM people")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    data = get_data_from_mysql()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
