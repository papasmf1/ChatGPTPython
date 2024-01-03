#Chap08_ChatGPT가생성한SQL구문.py
import sqlite3

# SQLite 데이터베이스에 연결
conn = sqlite3.connect('products.db')

# 커서 생성
cursor = conn.cursor()

# Products 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                    productID INTEGER PRIMARY KEY,
                    productName TEXT,
                    productPrice TEXT
                )''')

# 데이터 추가 (INSERT)
def add_product(productID, productName, productPrice):
    cursor.execute("INSERT INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)",
                   (productID, productName, productPrice))
    conn.commit()
    print("제품이 추가되었습니다.")

# 데이터 수정 (UPDATE)
def update_product(productID, productName, productPrice):
    cursor.execute("UPDATE Products SET productName = ?, productPrice = ? WHERE productID = ?",
                   (productName, productPrice, productID))
    conn.commit()
    print("제품이 수정되었습니다.")

# 데이터 삭제 (DELETE)
def delete_product(productID):
    cursor.execute("DELETE FROM Products WHERE productID = ?", (productID,))
    conn.commit()
    print("제품이 삭제되었습니다.")

# 데이터 조회 (SELECT)
def get_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products

# 데이터베이스 연결 종료
def close_connection():
    cursor.close()
    conn.close()

# 테스트 예시
add_product(1, "Keyboard", "50")
add_product(2, "Mouse", "20")

update_product(2, "Wireless Mouse", "30")

delete_product(1)

products = get_products()
for product in products:
    print(product)

# 연결 종료
close_connection()
