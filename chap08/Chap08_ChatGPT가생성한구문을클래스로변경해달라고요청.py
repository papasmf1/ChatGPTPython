#Chap08_ChatGPT가생성한구문을클래스로변경해달라고요청.py
import sqlite3

class Products:
    def __init__(self):
        # SQLite 데이터베이스에 연결
        self.conn = sqlite3.connect('products.db')
        # 커서 생성
        self.cursor = self.conn.cursor()
        # Products 테이블 생성
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                                productID INTEGER PRIMARY KEY,
                                productName TEXT,
                                productPrice TEXT
                            )''')

    def add_product(self, productID, productName, productPrice):
        self.cursor.execute("INSERT INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)",
                            (productID, productName, productPrice))
        self.conn.commit()
        print("제품이 추가되었습니다.")

    def update_product(self, productID, productName, productPrice):
        self.cursor.execute("UPDATE Products SET productName = ?, productPrice = ? WHERE productID = ?",
                            (productName, productPrice, productID))
        self.conn.commit()
        print("제품이 수정되었습니다.")

    def delete_product(self, productID):
        self.cursor.execute("DELETE FROM Products WHERE productID = ?", (productID,))
        self.conn.commit()
        print("제품이 삭제되었습니다.")

    def get_products(self):
        self.cursor.execute("SELECT * FROM Products")
        products = self.cursor.fetchall()
        return products

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


# 테스트 코드
product_manager = Products()

# 데이터 추가
product_manager.add_product(1, "Keyboard", "50")
product_manager.add_product(2, "Mouse", "20")
product_manager.add_product(3, "Monitor", "200")
product_manager.add_product(4, "Headphones", "80")
product_manager.add_product(5, "Laptop", "1000")
product_manager.add_product(6, "Printer", "150")
product_manager.add_product(7, "Speakers", "120")
product_manager.add_product(8, "Tablet", "300")
product_manager.add_product(9, "Smartphone", "600")
product_manager.add_product(10, "Camera", "400")

# 데이터 수정
product_manager.update_product(2, "Wireless Mouse", "30")
product_manager.update_product(7, "Bluetooth Speakers", "150")

# 데이터 삭제
product_manager.delete_product(1)
product_manager.delete_product(4)

# 데이터 조회
products = product_manager.get_products()
for product in products:
    print(product)

# 연결 종료
product_manager.close_connection()
