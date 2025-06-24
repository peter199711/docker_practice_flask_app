FROM python:3.10-slim

WORKDIR /app

COPY . .

# 安裝 cryptography，解決 pymysql 驗證問題
RUN pip install --no-cache-dir -r requirements.txt cryptography

CMD ["python", "app.py"]
