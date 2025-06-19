import os
import time
import pymysql
import pandas as pd

# 讀取 CSV 並預先處理
df = pd.read_csv("titanic_full_data.csv")
df = df.dropna(subset=['pname', 'age'])

# 嘗試重連 MySQL（最多嘗試 10 次）
max_tries = 10
for i in range(max_tries):
    try:
        conn = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
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
    CREATE TABLE people (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pname VARCHAR(100),
        age INT
    );
""")

for _, row in df.iterrows():
    cursor.execute("INSERT INTO people (pname, age) VALUES (%s, %s)", (row['pname'], int(row['age'])))

conn.commit()
conn.close()
