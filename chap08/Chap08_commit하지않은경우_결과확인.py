#Chap08_commit하지않은경우_결과확인.py
# 트랜잭션처리를 하지 않은 경우  
import sqlite3

#연결객체 생성(이번에는 데이터베이스 파일로 저장)
con = sqlite3.connect("c:\\work\\test.db")
#SQL구문을 실행할 커서 객체 리턴
cur = con.cursor()

#결과를 확인
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
