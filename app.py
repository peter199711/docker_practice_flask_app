import os
import time
import pymysql
import pandas as pd
from flask import Flask, render_template

# 讀取 CSV 並預先處理
df = pd.read_csv("titanic_full_data.csv")
df = df.dropna(subset=['pname', 'age'])

# 嘗試重連 MySQL（最多嘗試 10 次）
max_tries = 10
for i in range(max_tries):
    try:
        conn = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASS', 'P@ssw0rd'),
            database=os.getenv('DB_NAME', 'my_titanic'),
            charset='utf8mb4'
        )
        print("✅ 成功連接 MySQL")
        break
    except pymysql.err.OperationalError:
        print(f"❌ 第 {i+1} 次連線失敗，1 秒後重試...")
        time.sleep(1)
else:
    raise Exception("❌ 無法連接到 MySQL")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS people;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passengers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pclass INT,
        survived INT,
        pname VARCHAR(100),
        sex VARCHAR(10),
        age FLOAT,
        sibsp INT,
        parch INT,
        ticket VARCHAR(20),
        fare FLOAT,
        cabin VARCHAR(20),
        embarked VARCHAR(10),
        boat VARCHAR(20),
        body INT,
        homedest VARCHAR(100)
    );
""")

for _, row in df.iterrows():
    cursor.execute("INSERT INTO people (id, pclass, survived, pname, sex, age, sibsp, parch, ticket, fare, cabin, embarked, boat, body, homedest) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (row['id'], row['pclass'], row['survived'], row['pname'], row['sex'], row['age'], row['sibsp'], row['parch'], row['ticket'], row['fare'], row['cabin'], row['embarked'], row['boat'], row['body'], row['homedest']))

conn.commit()
conn.close()

app = Flask(__name__)

def get_data_from_mysql():
    conn = pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASS', 'P@ssw0rd'),
        database=os.getenv('DB_NAME', 'my_titanic'),
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    data = get_data_from_mysql()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
