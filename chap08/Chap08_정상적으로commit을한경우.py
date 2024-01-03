#Chap08_정상적으로commit을한경우.py
# 트랜잭션처리를 하지 않은 경우  
import sqlite3

#연결객체 생성(이번에는 데이터베이스 파일로 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#SQL구문을 실행할 커서 객체 리턴
cur = con.cursor()
cur.execute(
    "create table if not exists PhoneBook " + 
    "(id integer primary key autoincrement, name text, phoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동','010-111-1234');")
#파라메터로 입력 처리 
name = "이순신"
phoneNumber = "010-222-1234"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNumber))

#다중의 데이터를 입력
datalist = (("전우치","010-123-1234"), ("박문수","010-123-5678"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

#결과를 확인
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#정상적으로 커밋
con.commit() 