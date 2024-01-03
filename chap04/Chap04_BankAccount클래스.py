#Chap04_BankAccount클래스.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    #생성자(초기화메서드)
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 
    #입금처리 메서드
    def deposit(self, amount):
        self.balance += amount 
    #출금처리 메서드
    def withdraw(self, amount):
        self.balance -= amount
    #문자열 형태로 인스턴스의 결과를 출력하는 메서드 
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, \
            self.name, self.balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#외부에서 멤버변수에 접근할 수 있는 경우(문제점)
account1.balance = 15000000
print(account1)
