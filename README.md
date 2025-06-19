# 🧠 Flask + MySQL 資料顯示網站專案

## 📌 專案簡介

這是一個簡單的 Python 網頁應用專案，使用 **Flask 框架** 串接 **MySQL 資料庫**，將本地的 **CSV 檔案（以 Titanic 為例）匯入資料庫後再呈現在 HTML 網頁上**。此專案是資料驅動網站的基本範例，適合初學者理解前後端串接與資料庫應用。

---

## 🎯 創作目的

1. **學習 Flask 全棧開發流程**：從資料讀取 → 資料庫匯入 → 網頁顯示。
2. **練習資料庫操作與資料清洗**：理解如何將 CSV 資料安全、正確地寫入資料庫。
3. **模擬真實應用場景**：像是客戶資料、商品庫存、成績系統等都會有類似流程。

---

## ⚙️ 專案原理與架構

flask_app/<br>
├── app.py                  # Flask 主程式，負責提供網頁與資料<br>
├── import_csv_to_mysql.py  # 匯入 CSV 至 MySQL 的一次性腳本<br>
├── data/<br>
│   └── titanic_full_data.csv  # 原始資料（CSV 格式）<br>
├── templates/<br>
│   └── index.html           # 前端頁面，使用 Jinja2 模板語法<br>
└── requirements.txt         # 套件清單<br>


### 🔁 運作流程：

```text
CSV → pandas 讀取 → 匯入 MySQL → Flask 撈資料 → 傳遞給 HTML → Jinja2 模板顯示

# 1. 安裝虛擬環境（可選）
python -m venv venv
source venv/bin/activate    # 或 Windows: venv\Scripts\activate

# 2. 安裝必要套件
pip install -r requirements.txt

# 3. 匯入 CSV 到 MySQL
python import_csv_to_mysql.py

# 4. 啟動 Flask 網站
python app.py
